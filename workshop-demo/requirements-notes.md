# Requirements Notes — ระบบ Login

> บันทึก requirements ดิบจาก user interview (raw notes) ก่อนเรียบเรียงเป็น User Story

---

## 1. ภาพรวมจาก Interview

- ผู้ใช้ต้องการเข้าสู่ระบบด้วย **email + password** เพื่อเข้าถึงหน้า dashboard ส่วนตัว
- ระบบมีผู้ใช้ทั้งพนักงานภายในและลูกค้าภายนอก แต่ workshop นี้โฟกัสที่ flow login พื้นฐานก่อน
- ทีม security ขอให้ป้องกัน brute-force attack ด้วยการ lock account
- ทีม legal ย้ำเรื่อง PDPA สำหรับการเก็บ log การเข้าถึง

---

## 2. Business Rules (กฎทางธุรกิจ)

- **BR-1 — Login Attempt Limit:** ผู้ใช้ใส่รหัสผ่านผิดได้ไม่เกิน **5 ครั้งติดต่อกัน** ครั้งที่ 5 ที่ผิด ระบบจะ lock account
- **BR-2 — Account Lock Duration:** เมื่อ account ถูก lock จะปลดล็อกอัตโนมัติหลัง **30 นาที** (`locked_until`) หรือผู้ใช้กดขอลิงก์ปลดล็อกทาง email
- **BR-3 — Session Timeout:** session หมดอายุหลังไม่มี activity **30 นาที** ผู้ใช้ต้อง login ใหม่
- **BR-4 — Password Expiry:** รหัสผ่านมีอายุ **90 วัน** หลังครบกำหนดต้องเปลี่ยนรหัสก่อนเข้าใช้งาน
- **BR-5 — Reset Attempt Counter:** เมื่อ login สำเร็จ ระบบ reset `attempt_count` กลับเป็น 0

---

## 3. Constraints (ข้อจำกัด)

- **C-1 — PDPA Log Retention:** เก็บ access log (เวลา login, IP, ผลลัพธ์) ได้ไม่เกิน **90 วัน** จากนั้นต้องลบหรือ anonymize
- **C-2 — Password Complexity:** รหัสผ่านต้องยาวอย่างน้อย **8 ตัวอักษร** ประกอบด้วยตัวพิมพ์ใหญ่ ตัวพิมพ์เล็ก ตัวเลข และอักขระพิเศษอย่างละ 1 ตัว (ตาม policy องค์กร)
- **C-3 — Transport Security:** ทุก request ต้องผ่าน HTTPS เท่านั้น ห้ามส่ง credential ผ่าน HTTP
- **C-4 — No Plaintext Storage:** ห้ามเก็บรหัสผ่านเป็น plaintext ต้อง hash ด้วย bcrypt/argon2

---

## 4. คำถามค้างคา (Open Questions)

- รองรับ SSO / social login ในเฟสถัดไปหรือไม่?
- ต้องมี 2FA สำหรับ admin หรือไม่?
- ข้อความ error ควรบอกแค่ "email หรือ password ไม่ถูกต้อง" รวม ๆ เพื่อไม่เปิดเผยว่า email มีในระบบหรือไม่ (security best practice) — รอ confirm กับทีม security
