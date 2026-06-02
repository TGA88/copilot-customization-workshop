<!--
ส่วน `assets/` = เทมเพลต/ทรัพยากรที่ skill เอาไป "เติมแล้วส่งออก"
แทนค่าใน {{...}} ด้วยผลจริงจาก check_tc.py + การตีความตาม references/
-->
# TC Audit Report — {{file}}

> ตรวจเมื่อ: {{date}} · โดย skill `tc-audit`

## สรุป
- Test case ทั้งหมด: **{{total_tc}}**
- ผลรวม: **{{errors}} error · {{warnings}} warning**
- สถานะ: {{✅ ผ่าน | ❌ ต้องแก้}}

## การกระจาย Label
| Label | จำนวน |
|---|---|
| Happy Path | {{n}} |
| Negative | {{n}} |
| Edge Case | {{n}} |

## รายการปัญหา
| severity | TC | ปัญหา | กฎที่ผิด (อ้าง references) | ข้อเสนอแก้ไข |
|---|---|---|---|---|
| {{error/warn}} | {{TC-ID}} | {{message}} | {{tc-format.md / label-guide.md ข้อไหน}} | {{ควรแก้เป็น...}} |

## ข้อเสนอภาพรวม
- {{สรุปสิ่งที่ควรแก้ก่อน เรียงตามความสำคัญ}}
