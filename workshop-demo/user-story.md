# User Story — ระบบ Login

---

## Statement

> **As a** ผู้ใช้งานที่มีบัญชีในระบบ
> **I want to** เข้าสู่ระบบด้วย email และ password
> **So that** ฉันสามารถเข้าถึงหน้า dashboard และข้อมูลส่วนตัวได้อย่างปลอดภัย

---

## Conditions

| # | Condition | Type |
|---|-----------|------|
| COND-1 | ผู้ใช้ใส่รหัสผ่านผิดได้ไม่เกิน 5 ครั้งติดต่อกัน ครั้งที่ 5 lock account | Business Rule |
| COND-2 | account ที่ถูก lock ปลดล็อกอัตโนมัติหลัง 30 นาที | Business Rule |
| COND-3 | session หมดอายุหลังไม่มี activity 30 นาที | Business Rule |
| COND-4 | login สำเร็จต้อง reset attempt_count เป็น 0 | Business Rule |
| COND-5 | รหัสผ่านมีอายุ 90 วัน ครบกำหนดต้องเปลี่ยนก่อนเข้าใช้ | Business Rule |
| COND-6 | เก็บ access log ได้ไม่เกิน 90 วัน (PDPA) | Constraint |
| COND-7 | รหัสผ่านต้อง ≥ 8 ตัว มีพิมพ์ใหญ่/เล็ก/ตัวเลข/อักขระพิเศษ | Constraint |
| COND-8 | ทุก request ต้องผ่าน HTTPS เท่านั้น | Constraint |
| COND-9 | ข้อความ error ไม่เปิดเผยว่า email มีอยู่ในระบบหรือไม่ | Constraint |

---

## Related Documents

<!-- เว้นว่างไว้ — จะถูกเติมเมื่อสร้าง scenario / tech-spec / qa-test-spec -->

- user-flow.md —
- scenarios.md —
- business-tc.md —
- frontend-tech-spec.md —
- backend-tech-spec.md —
