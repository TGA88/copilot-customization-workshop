---
name: create-tc
description: สร้าง Business TC จาก AC ใน scenario ที่กำหนด
---

# Create Test Cases from Scenario

รับ scenario ID: **#input:scenarioId**

ทำตามขั้นตอนนี้:

1. อ่านไฟล์ `workshop-demo/scenario-{scenarioId}.md`
   - ถ้าหาไฟล์ไม่เจอ ให้แจ้งผู้ใช้และหยุด (อย่าเดา)
2. ดึง Acceptance Criteria (AC) ทั้งหมดในไฟล์นั้น
3. สำหรับ **ทุก AC** สร้าง Test Case ครอบคลุม:
   - กรณีผลลัพธ์หลักของ AC นั้น
   - ถ้ามี input หลายแบบที่ให้ผลเหมือนกัน ให้แตกเป็นหลาย TC ภายใต้ AC เดียว
4. จัด format ให้ตรงตาม `.github/instructions/business-tc.instructions.md` เป๊ะ:
   `| TC-ID | Title | AC-Ref | Test Data | Expected Result | Label |`
   - Label ต้องเป็น Happy Path / Negative / Edge Case เท่านั้น
   - TC-ID ต่อเนื่องจาก TC ล่าสุดที่มีอยู่แล้วใน business-tc.md (ห้ามชนกัน)
5. **Append** ลงใน `workshop-demo/business-tc.md` (ห้ามลบหรือแก้ TC เดิม)
6. หลังเสร็จ สรุปจำนวน TC ที่เพิ่ม และ list TC-ID ที่สร้างใหม่
