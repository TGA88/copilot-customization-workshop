# User Flow — ระบบ Login

---

## Flowchart

```mermaid
flowchart TD
    Start([ผู้ใช้เปิดหน้า Login]) --> Input[กรอก email + password]
    Input --> Submit[กดปุ่ม Login]
    Submit --> CheckEmail{email มีในระบบ?}

    CheckEmail -- ไม่มี --> ErrEmail[แสดง error: email หรือ password ไม่ถูกต้อง]
    ErrEmail --> Input

    CheckEmail -- มี --> CheckLock{account ถูก lock อยู่?}
    CheckLock -- ใช่ และยังไม่ถึง locked_until --> ErrLocked[แสดงข้อความ account ถูกล็อก + วิธี unlock]
    ErrLocked --> End2([จบ: รอปลดล็อก])

    CheckLock -- ไม่ / เลย locked_until แล้ว --> CheckPwd{password ถูกต้อง?}

    CheckPwd -- ผิด --> Incr[attempt_count += 1]
    Incr --> Check5{attempt_count >= 5?}
    Check5 -- ใช่ --> Lock[set locked_until = now + 30 นาที + แสดง unlock instructions]
    Lock --> End2
    Check5 -- ยังไม่ถึง --> ErrPwd[แสดง error: email หรือ password ไม่ถูกต้อง]
    ErrPwd --> Input

    CheckPwd -- ถูกต้อง --> Reset[reset attempt_count = 0]
    Reset --> CheckExpiry{password หมดอายุ 90 วัน?}
    CheckExpiry -- ใช่ --> ForceChange[redirect หน้าเปลี่ยนรหัสผ่าน]
    ForceChange --> End3([จบ: ต้องเปลี่ยนรหัส])
    CheckExpiry -- ไม่ --> CreateSession[สร้าง session_token]
    CreateSession --> Dashboard([redirect ไปหน้า Dashboard])
```

---

## Logic Paths สรุป

| Path ID | ประเภท | คำอธิบาย |
|---------|--------|----------|
| LP-1 | Happy Path | email มี + password ถูก + รหัสไม่หมดอายุ → สร้าง session → dashboard |
| LP-2 | Negative | password ผิด (ยังไม่ครบ 5) → error + attempt_count +1 |
| LP-3 | Negative | email ไม่มีในระบบ → error กลาง ๆ |
| LP-4 | Edge Case | login ผิดครบ 5 ครั้ง → lock account + unlock instructions |
| LP-5 | Edge Case | account ถูก lock อยู่ (ยังไม่ถึง locked_until) → ปฏิเสธทันที |
| LP-6 | Edge Case | password ถูกต้องแต่หมดอายุ 90 วัน → บังคับเปลี่ยนรหัส |

---

## Field Definitions

| Field | Type | คำอธิบาย |
|-------|------|----------|
| `email` | string | อีเมลผู้ใช้ ใช้เป็น identifier ในการ login (ต้องเป็นรูปแบบ email ที่ถูกต้อง) |
| `password` | string | รหัสผ่าน ส่งแบบเข้ารหัส ฝั่ง server เก็บเป็น hash เท่านั้น |
| `attempt_count` | integer | จำนวนครั้งที่ใส่รหัสผิดติดต่อกัน reset เป็น 0 เมื่อ login สำเร็จ |
| `locked_until` | datetime / null | เวลาที่ account จะปลดล็อก ถ้า null = ไม่ถูก lock |
| `session_token` | string | token ที่ออกให้หลัง login สำเร็จ ใช้ยืนยันตัวตนในแต่ละ request หมดอายุตาม session timeout |
