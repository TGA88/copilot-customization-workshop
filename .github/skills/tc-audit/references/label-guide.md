# Label Guide (reference)

> นิยาม Label ที่อนุญาต **3 ค่าเท่านั้น** — ใช้ตัดสินว่า TC แต่ละแถวติด label ถูกมั้ย

| Label | ใช้เมื่อ | ตัวอย่างจาก login |
|---|---|---|
| **Happy Path** | flow ปกติที่ทุกอย่างถูกต้อง → สำเร็จตามคาด | login ด้วย credential ถูก → ได้ session, redirect dashboard |
| **Negative** | input ผิด/ไม่ผ่าน validation → ระบบปฏิเสธอย่างถูกต้อง | password ผิด, email ไม่มีในระบบ, ส่งผ่าน HTTP |
| **Edge Case** | เงื่อนไขขอบเขต/สถานะพิเศษ ที่ต้องจัดการเฉพาะ | ผิดครบ 5 ครั้ง → lock, login ตอน account ถูก lock, password หมดอายุ |

## เส้นแบ่งที่มักสับสน
- **Negative vs Edge Case:** ถ้าเป็น "input ผิดธรรมดา" = Negative · ถ้าเป็น "ถึงเกณฑ์/เปลี่ยนสถานะระบบ" (เช่นครบจำนวนครั้งแล้ว lock) = Edge Case
- **Happy Path ต้องสำเร็จเสมอ** — ถ้าจบด้วย error/ปฏิเสธ ไม่ใช่ Happy Path

## ค่าที่ "ไม่อนุญาต" (พบบ่อย → error)
`Positive`, `Boundary`, `Sad Path`, `Error`, `Smoke` ฯลฯ — ให้ map กลับเป็น 3 ค่าข้างบน
