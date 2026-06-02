# Copilot Instructions — Workshop: GitHub Copilot Customization

## Project Overview

โปรเจกต์นี้เป็น **workshop สอนการใช้ GitHub Copilot Customization ใน VS Code**
ครอบคลุม 5 concepts: Custom Instructions, Custom Prompts, Skills, MCP (GitHub), Agents
ใช้ feature "ระบบ Login" เป็น demo ตลอด workshop

## Tech Stack

- **Language:** TypeScript
- **Runtime:** Node.js
- **E2E Test:** Playwright
- **Format เอกสาร:** Markdown (Mermaid สำหรับ diagram)

## Document Workflow ของทีม

เอกสารถูกสร้างตามลำดับนี้ (อย่าข้ามขั้น):

```
requirements-notes.md      → บันทึก requirement ดิบจาก interview
   → user-story.md         → Statement + Conditions (Business Rule / Constraint)
   → user-flow.md          → Mermaid flow ครอบคลุมทุก logic path + Field Definitions
   → scenarios.md          → index ของ scenario ทั้งหมด
   → scenario-[id].md       → Logic Path + Acceptance Criteria (Given/When/Then)
   → business-tc.md         → Flat list Test Case map กับ AC
   → frontend-tech-spec.md  → technical spec ฝั่ง UI
   / backend-tech-spec.md   → technical spec ฝั่ง API/DB
   → qa-test-spec.md        → spec สำหรับ automated test
```

## Conventions

- **Naming:** ใช้ **kebab-case** กับทุกไฟล์ (เช่น `user-flow.md`, `scenario-01-login-success.md`)
- **ภาษา:** เนื้อหาเอกสารใช้ภาษาไทยได้ แต่ technical term / field name / TC-ID เป็นภาษาอังกฤษ
- **ID format:** Scenario = `scenario-[NN]-[name]`, AC = `AC-[NN]`, TC = `TC-[NN]`, Condition = `COND-[NN]`
- **ห้ามสร้างไฟล์นอก document structure ที่กำหนดข้างต้น** ถ้าไม่แน่ใจให้ถามก่อน
- ทุกเอกสารต้อง reference กลับไปยัง document ต้นทาง (traceability)

## Separation of Concerns

- เอกสาร **scenario** = มุมมอง user (ห้ามมี implementation detail)
- เอกสาร **tech-spec** = มุมมอง developer (ห้ามมี business rule ที่ยังไม่ sign off)
- เอกสาร **business-tc** = flat list ที่ map AC ↔ TC แบบ 1:1 ต่อแถว
