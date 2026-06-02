---
name: create-scenario
description: สร้าง scenario file จาก logic path ใน user-flow.md
---

# Create Scenario Skill

สร้างไฟล์ scenario จาก logic path ที่ยังไม่มี scenario โดยอ้างอิง `user-flow.md`

## Steps

1. อ่าน `workshop-demo/user-flow.md` ระบุ **logic path ทั้งหมด** (LP-1, LP-2, ...)
2. เช็คใน `workshop-demo/` ว่า logic path ไหน **ยังไม่มี** scenario file รองรับ
3. สำหรับ path ที่ยังไม่มี สร้าง `workshop-demo/scenario-[id]-[name].md`
   (เช่น `scenario-01-login-success.md`) ตาม format ด้านล่าง
4. เพิ่ม entry ลงใน `workshop-demo/scenarios.md` (ถ้ายังไม่มีไฟล์นี้ ให้สร้างใหม่เป็น index table)
5. ตรวจว่าแต่ละ AC ครอบคลุม **ผลลัพธ์ที่ต่างกัน** ไม่ใช่แค่ input ต่างกัน

## Scenario File Format

```markdown
# Scenario [id]: [ชื่อ scenario]

## Logic Path
- อ้างอิง: LP-X จาก user-flow.md
- คำอธิบาย path สั้น ๆ

## Acceptance Criteria

### AC-01: <Title>
- **Given** <สถานะตั้งต้น>
- **When** <การกระทำ user>
- **Then** <ผลลัพธ์ที่ user สังเกตได้>
- **Covers:** COND-X

## Condition Coverage
| COND | ครอบคลุมโดย AC |
|------|----------------|
| COND-X | AC-01 |
```

## Rules
- เขียนในมุมมอง user เท่านั้น ห้ามใส่ implementation detail (ดู scenario.instructions.md)
- ทุก AC ต้อง reference Condition จาก user-story.md
- naming ไฟล์เป็น kebab-case
