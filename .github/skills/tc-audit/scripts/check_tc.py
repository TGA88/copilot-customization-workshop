#!/usr/bin/env python3
"""ตรวจคุณภาพ business-tc.md (Test Case flat list)

ใช้โดย skill `tc-audit` — parse ตาราง markdown แล้วตรวจ format / label / duplicate
จากนั้นพิมพ์ผลเป็น JSON ทาง stdout เพื่อให้ skill เอาไปสรุปต่อ

นี่คือส่วน `scripts/` ของ skill: งานที่ "ตายตัว ตรวจซ้ำได้" ควรเป็นโค้ด
ไม่ใช่ปล่อยให้โมเดลเดา — ทำให้ผลแม่นและถูกทุกครั้ง

Usage:
    python3 check_tc.py [path/to/business-tc.md]
ค่า default: workshop-demo/business-tc.md
Exit code: 0 = ผ่าน, 2 = เจอ error, 1 = รันไม่ได้ (ไฟล์/ตารางหาย)
"""
import json
import re
import sys
from pathlib import Path

ALLOWED_LABELS = {"Happy Path", "Negative", "Edge Case"}
EXPECTED_COLUMNS = ["TC-ID", "Title", "AC-Ref", "Test Data", "Expected Result", "Label"]
REQUIRED_NONEMPTY = ["TC-ID", "Title", "AC-Ref", "Expected Result", "Label"]


def split_row(line):
    """ตัด | หัวท้าย แล้ว split เป็นเซลล์ที่ strip แล้ว"""
    return [c.strip() for c in line.strip().strip("|").split("|")]


def find_header(lines):
    """หา index ของแถว header ที่มีคอลัมน์ TC-ID"""
    for i, line in enumerate(lines):
        if line.strip().startswith("|") and "TC-ID" in line:
            return i
    return None


def main():
    path = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("workshop-demo/business-tc.md")
    result = {"file": str(path), "ok": False, "total_tc": 0,
              "by_label": {}, "issues": [], "summary": ""}

    def add(severity, tc, message):
        result["issues"].append({"severity": severity, "tc": tc, "message": message})

    if not path.exists():
        add("error", None, f"ไม่พบไฟล์ {path}")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1

    lines = path.read_text(encoding="utf-8").splitlines()
    h = find_header(lines)
    if h is None:
        add("error", None, "ไม่พบตาราง TC (header ที่มีคอลัมน์ TC-ID)")
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1

    header = split_row(lines[h])
    if header != EXPECTED_COLUMNS:
        add("warn", None, f"คอลัมน์ไม่ตรง spec — เจอ {header} ต้องการ {EXPECTED_COLUMNS}")

    seen = {}
    by_label = {}
    data_rows = 0
    # ข้าม header (h) + แถว separator |---|---| (h+1) → เริ่มอ่านข้อมูลที่ h+2
    for line in lines[h + 2:]:
        if not line.strip().startswith("|"):
            break  # จบตารางแล้ว
        cells = split_row(line)
        if all(c == "" for c in cells):
            continue
        data_rows += 1
        padded = cells + [""] * (len(EXPECTED_COLUMNS) - len(cells))
        row = dict(zip(EXPECTED_COLUMNS, padded))
        tc = row["TC-ID"]

        if len(cells) != len(EXPECTED_COLUMNS):
            add("error", tc, f"จำนวนคอลัมน์ผิด ({len(cells)} ควรเป็น {len(EXPECTED_COLUMNS)})")

        if not re.fullmatch(r"TC-\d{2,}", tc):
            add("warn", tc, f"TC-ID ไม่ตรง format TC-NN: '{tc}'")
        if tc in seen:
            add("error", tc, f"TC-ID ซ้ำกับแถว {seen[tc]}")
        else:
            seen[tc] = data_rows

        if not re.fullmatch(r"AC-\d{2,}", row["AC-Ref"]):
            add("warn", tc, f"AC-Ref ไม่ตรง format AC-NN: '{row['AC-Ref']}'")

        if row["Label"] not in ALLOWED_LABELS:
            add("error", tc, f"Label ไม่อนุญาต: '{row['Label']}' "
                             f"(ใช้ได้: {', '.join(sorted(ALLOWED_LABELS))})")
        else:
            by_label[row["Label"]] = by_label.get(row["Label"], 0) + 1

        for col in REQUIRED_NONEMPTY:
            if not row[col]:
                add("warn", tc, f"คอลัมน์ '{col}' ว่าง")

    errors = sum(1 for x in result["issues"] if x["severity"] == "error")
    warns = sum(1 for x in result["issues"] if x["severity"] == "warn")
    result["total_tc"] = data_rows
    result["by_label"] = by_label
    result["ok"] = errors == 0
    result["summary"] = f"{data_rows} TC, {errors} error, {warns} warning"

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["ok"] else 2


if __name__ == "__main__":
    sys.exit(main())
