---
name: review-coverage
description: ตรวจ TC coverage เทียบกับ user-flow
---

# Review Test Coverage

ตรวจสอบว่า Test Case ครอบคลุมทุก logic path ใน user flow หรือยัง

ทำตามขั้นตอนนี้:

1. อ่าน `workshop-demo/user-flow.md` — ดึง **logic path ทั้งหมด** (LP-1, LP-2, ...)
2. อ่าน `workshop-demo/business-tc.md` — ดึง TC ทั้งหมดพร้อม AC-Ref และ Label
3. Map แต่ละ logic path เข้ากับ TC ที่ครอบคลุม path นั้น
4. Output เป็น **markdown checklist**:

   ```
   - ✅ LP-1 (Happy Path) — ครอบคลุมโดย TC-01, TC-09
   - ❌ LP-X (...) — ยังขาด TC
   ```

5. ระบุ logic path ที่ยังไม่มี TC อย่างชัดเจน พร้อมแนะนำ TC ที่ควรเพิ่ม
6. สรุปท้ายสุดเป็น **% coverage** = (จำนวน logic path ที่มี TC / logic path ทั้งหมด) × 100
