# Business TC — ระบบ Login

> Flat list ของ Test Case ทั้งหมดของ story นี้
> 1 TC = 1 แถว, map กับ AC เดียวเท่านั้น
> Label ที่อนุญาต: Happy Path / Negative / Edge Case

---

| TC-ID | Title | AC-Ref | Test Data | Expected Result | Label |
|-------|-------|--------|-----------|-----------------|-------|
| TC-01 | Login สำเร็จด้วย credential ที่ถูกต้อง | AC-01 | email=`user@test.com`, password=`Passw0rd!` (รหัสไม่หมดอายุ) | สร้าง session_token, reset attempt_count=0, redirect ไป dashboard | Happy Path |
| TC-02 | Login ด้วย password ผิด (ครั้งที่ 1) | AC-02 | email=`user@test.com`, password=`wrongpass` | แสดง error "email หรือ password ไม่ถูกต้อง", attempt_count=1 | Negative |
| TC-03 | Login ด้วย password ผิดซ้ำ (ครั้งที่ 2-4) | AC-02 | email=`user@test.com`, password ผิด 3 ครั้งติด | แสดง error ทุกครั้ง, attempt_count เพิ่มเป็น 4, account ยังไม่ lock | Negative |
| TC-04 | Login ด้วย email ที่ไม่มีในระบบ | AC-03 | email=`notfound@test.com`, password=`anything` | แสดง error กลาง ๆ "email หรือ password ไม่ถูกต้อง" ไม่บอกว่า email ไม่มี | Negative |
| TC-05 | Login ผิดครบ 5 ครั้ง → lock account | AC-04 | email=`user@test.com`, password ผิดครั้งที่ 5 | set locked_until = now+30 นาที, แสดง unlock instructions | Edge Case |
| TC-06 | พยายาม login ขณะ account ถูก lock อยู่ | AC-05 | email=`locked@test.com` (locked_until ยังไม่ถึง), password ถูกต้อง | ปฏิเสธทันที, แสดงข้อความ account ถูกล็อก + วิธี unlock, ไม่ตรวจ password | Edge Case |
| TC-07 | Login หลัง locked_until ผ่านไปแล้ว | AC-05 | email=`locked@test.com` (เลย locked_until), password ถูกต้อง | อนุญาตให้ตรวจ password ต่อ, login สำเร็จ, reset attempt_count=0 | Edge Case |
| TC-08 | Login สำเร็จแต่ password หมดอายุ 90 วัน | AC-06 | email=`expired@test.com`, password ถูกต้อง, password_updated_at > 90 วัน | redirect ไปหน้าเปลี่ยนรหัสผ่าน ไม่สร้าง session ปกติ | Edge Case |
| TC-09 | reset attempt_count หลัง login สำเร็จ | AC-01 | email=`user@test.com` ที่ attempt_count=3 อยู่, password ถูกต้อง | login สำเร็จ, attempt_count กลับเป็น 0 | Happy Path |
| TC-10 | ปฏิเสธ credential ที่ส่งผ่าน HTTP (ไม่ใช่ HTTPS) | AC-07 | request login ผ่าน `http://` | ปฏิเสธ request, ไม่ประมวลผล login | Negative |
