---
name: tc-audit
description: ตรวจคุณภาพ business-tc.md (format/label/duplicate) แล้วออกรายงาน + ร่าง issue ต่อปัญหาที่เจอ
argument-hint: "[path ของ business-tc.md (ออปชัน)]"
# หมายเหตุ: frontmatter ยังมี field อื่นอีก (allowed-tools, model, user-invocable, ...)
# ดูครบที่ docs/agent-skills-reference.md — ตรงนี้ใช้แค่ที่ GitHub Copilot รองรับ
---

# TC Audit Skill

ตรวจว่า `business-tc.md` ถูกต้องตาม format ทีมมั้ย แล้วสรุปเป็นรายงาน
สาธิต **โครงสร้าง skill ครบทุกส่วน** — ดูว่าแต่ละส่วนทำหน้าที่ต่างกันยังไง:

```
tc-audit/
├── SKILL.md        ← ไฟล์นี้: "สมอง" สั่งลำดับงาน (instructions)
├── scripts/        ← โค้ดที่รันจริง (deterministic) — parse + ตรวจ format
│   └── check_tc.py
├── references/     ← ความรู้ที่อ่านเมื่อต้องใช้ — กฎ format + นิยาม label
│   ├── tc-format.md
│   └── label-guide.md
└── assets/         ← เทมเพลต/ทรัพยากรไว้ผลิต output
    ├── audit-report-template.md
    └── github-issue-template.md
```

## Steps

1. **รัน script ตรวจอัตโนมัติ** — เรียก `scripts/check_tc.py` กับไฟล์เป้าหมาย
   (default: `workshop-demo/business-tc.md` หรือ path ที่ผู้ใช้ระบุ):
   ```bash
   python3 .github/skills/tc-audit/scripts/check_tc.py workshop-demo/business-tc.md
   ```
   script จะคืน **JSON** ที่มี: จำนวน TC, การกระจาย label, และรายการ issue (error/warning)

2. **ตีความผลด้วย references** — อ่าน `references/tc-format.md` และ
   `references/label-guide.md` เพื่อเข้าใจกฎ แล้วอธิบายว่าแต่ละ issue ผิดกฎข้อไหน
   และควรแก้ยังไง (อย่าตัดสินจาก JSON ดิบอย่างเดียว)

3. **ออกรายงาน** — ใช้โครง `assets/audit-report-template.md` เติมผลจากขั้น 1-2
   ให้ครบทุกช่อง (สรุปคะแนน, ตาราง issue, ข้อเสนอแก้ไข)

4. **(ออปชัน) ร่าง GitHub Issue** — ถ้าผู้ใช้ขอ ให้แปลงแต่ละ issue ที่ severity = error
   เป็น issue body ตามโครง `assets/github-issue-template.md` (ยังไม่สร้างจริงจน user ยืนยัน)

## Rules
- **อย่าแก้ `business-tc.md` เอง** — skill นี้ "ตรวจ + รายงาน" เท่านั้น การแก้เป็นหน้าที่ผู้ใช้
- ถ้า script รันไม่ได้ (เช่นไม่มี python) ให้ fallback ไปตรวจด้วยตาตามกฎใน `references/`
  แล้วบอกผู้ใช้ว่าไม่ได้รันแบบอัตโนมัติ
- Label ที่อนุญาตมีแค่ 3 ค่า — ยึดตาม `references/label-guide.md` เท่านั้น
