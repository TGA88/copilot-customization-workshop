# TC Format Spec (reference)

> ส่วน `references/` = ความรู้ที่ skill **อ่านเมื่อต้องใช้** (ไม่โหลดเข้า context จนกว่า SKILL.md จะอ้าง)
> ใช้ตีความผลจาก `scripts/check_tc.py` ว่าแต่ละ issue ผิดกฎข้อไหน

## โครงตาราง
ทุก TC อยู่ในตาราง markdown เดียว 6 คอลัมน์ ตามลำดับนี้เป๊ะ:

| คอลัมน์ | กฎ |
|---|---|
| `TC-ID` | format `TC-NN` (เลข 2 หลักขึ้นไป), **ห้ามซ้ำ** |
| `Title` | ประโยคสั้นบอกสิ่งที่ทดสอบ, ห้ามว่าง |
| `AC-Ref` | format `AC-NN`, map ได้ **AC เดียวต่อแถว** |
| `Test Data` | input ที่ใช้ทดสอบ (มี backtick ครอบค่าได้) |
| `Expected Result` | ผลที่คาด, ห้ามว่าง |
| `Label` | 1 ใน 3 ค่าเท่านั้น (ดู [label-guide.md](label-guide.md)) |

## กฎการ map
- **1 TC = 1 แถว = 1 AC** — ห้าม TC เดียว map หลาย AC
- **ผลลัพธ์ต่างกัน = คนละ AC** · input ต่างกันแต่ผลเหมือนกัน = หลาย TC ใน AC เดียวกันได้
- ทุก `AC-Ref` ควรมีอยู่จริงใน scenario ต้นทาง (traceability)

## ระดับความรุนแรงของ issue
- **error** = ผิดกฎที่ทำให้ข้อมูลเชื่อถือไม่ได้ (label ผิด, TC-ID ซ้ำ, คอลัมน์เพี้ยน) → ต้องแก้
- **warning** = ผิด convention แต่ยังอ่านรู้เรื่อง (format ID เพี้ยน, ช่องว่าง) → ควรแก้
