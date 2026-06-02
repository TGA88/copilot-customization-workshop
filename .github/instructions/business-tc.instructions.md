---
applyTo: "**/*business-tc*.md"
---

# Business Test Case Instructions

## Responsibility
รวบรวม **Flat list Test Case ทั้งหมด** ของ story ไว้ในไฟล์เดียว เพื่อใช้ track coverage

## Format
ตารางเดียว flat list ทุก TC:

```
| TC-ID | Title | AC-Ref | Test Data | Expected Result | Label |
```

## Rules
- **1 TC = 1 แถว**
- แต่ละ TC **map กับ AC เดียวเท่านั้น** (ใส่ AC-ID ใน AC-Ref)
- **Label ที่อนุญาตมีแค่:** `Happy Path` / `Negative` / `Edge Case` (ห้ามใช้ค่าอื่น)
- TC-ID เรียงต่อเนื่อง `TC-01`, `TC-02`, ... ห้ามซ้ำ

## หลักการแยก AC vs TC
- **ผลลัพธ์ต่างกัน → คนละ AC** (เช่น "login สำเร็จ" กับ "ถูก lock" เป็นคนละ AC)
- **input ต่างกันแต่ผลลัพธ์เหมือนกัน → หลาย TC ภายใต้ AC เดียวกัน** (เช่น password ผิดครั้งที่ 1, 2, 3 ผลเหมือนกัน = หลาย TC ของ AC เดียว)
- Test Data ต้องเป็นข้อมูลที่ทดสอบได้จริง (concrete) ไม่ใช่คำอธิบายลอย ๆ
