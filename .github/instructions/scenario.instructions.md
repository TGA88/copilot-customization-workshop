---
applyTo: "**/*scenario*.md"
---

# Scenario Authoring Instructions

## Responsibility
เขียน **Logic Path** และ **Acceptance Criteria (AC)** สำหรับแต่ละ scenario ของ story

## Scope
- แตก scenario ออกมาจาก logic path ใน `user-flow.md`
- เขียน AC ในมุมมองของ **user** ไม่ใช่ system ("ผู้ใช้เห็นอะไร / ทำอะไรได้")
- 1 scenario file = 1 logic path หลัก

## Must NOT contain
- technical implementation detail (เช่น ชื่อ function, library, framework)
- โค้ดทุกชนิด
- API spec, DB schema, endpoint, payload
- การออกแบบ UI ระดับ component/elementId

## AC Format
ทุก AC ต้องเขียนในรูปแบบ **Given / When / Then**:

```
### AC-01: <Title สั้น ๆ ที่สื่อผลลัพธ์>
- **Given** <สถานะ/เงื่อนไขตั้งต้น>
- **When** <การกระทำของ user>
- **Then** <ผลลัพธ์ที่ user สังเกตได้>
- **Covers:** COND-X
```

## Rules
- ทุก AC ต้องมี **Title** และ **reference Condition** (COND-X) ที่เกี่ยวข้องจาก `user-story.md`
- scenario ต้องครอบคลุมทั้ง **Happy Path**, **Negative**, และ **Edge Case** ตามที่ logic path กำหนด
- แต่ละ AC ต้องครอบคลุม **ผลลัพธ์ที่ต่างกัน** ไม่ใช่แค่ input ที่ต่างกัน (input ต่างผลเหมือน = TC หลายแถวใน AC เดียว ไม่ใช่ AC ใหม่)
