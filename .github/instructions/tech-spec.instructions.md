---
applyTo: "**/*-tech-spec.md"
---

# Technical Specification Instructions

## Responsibility
เขียน **technical specification** ที่ developer นำไป implement ได้ทันที โดยอ้างอิงจาก scenario + AC ที่ sign off แล้ว

## Frontend Scope (`frontend-tech-spec.md`)
แต่ละ spec ต้องระบุ:
- **UI Components** — รายการ component และโครงสร้าง
- **elementId** — id ที่ใช้อ้างอิงใน test (เช่น `#login-email`, `#login-submit`)
- **States** — สถานะของ UI (idle / loading / error / locked)
- **Handlers** — event handler และพฤติกรรม (เช่น `onSubmit`)
- **Business Logic** — logic ฝั่ง client (validation, แสดง error)
- **Test Spec** — สิ่งที่ Playwright ต้องตรวจ

## Backend Scope (`backend-tech-spec.md`)
แต่ละ spec ต้องระบุ:
- **API Spec** — endpoint, HTTP method, request body, response (success/error), status code
- **DB Schema** — ตาราง, column, type, index ที่เกี่ยวข้อง
- **Business Logic** — ลำดับการประมวลผล (เช่น เช็ค lock → เช็ค password → reset count)
- **Test Spec** — case ที่ต้องทดสอบฝั่ง server

## Must NOT contain
- business rule ที่ **ยังไม่ได้ sign off** จาก user (ถ้าจำเป็นต้องเพิ่ม ให้ใส่ section "Open / Needs Sign-off" แยก)

## Rules
- ทุก task ต้องมี **Effort estimation (หน่วยเป็น minutes)**
- **API Contract ต้องตรงกัน** ระหว่าง frontend และ backend spec (request/response shape เดียวกัน field name เดียวกัน)
- อ้างอิง AC-ID ที่ spec นี้รองรับเสมอ
