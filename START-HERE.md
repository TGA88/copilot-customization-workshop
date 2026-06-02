# Workshop Prep — Copy prompt นี้ไปวางใน Claude Code ได้เลย

---

```
ฉันกำลังเตรียม workshop สอนการใช้ GitHub Copilot Customization ใน VS Code
ครอบคลุม: Custom Instructions, Custom Prompts, Skills, MCP (Trello)
โดยใช้ workflow ของทีม: Requirements → User Story → Development
workshop demo ใช้ feature "ระบบ Login" เป็นตัวอย่าง

project folder นี้มี placeholder files วางไว้แล้ว งานของแกคือ
สร้างเนื้อหาจริงให้ครบทุกไฟล์ในคราวเดียว ตามลำดับนี้:

─────────────────────────────────────
TASK 1 — สร้างเนื้อหาไฟล์จำลองใน workshop-demo/
─────────────────────────────────────

workshop-demo/requirements-notes.md
- บันทึก requirements ดิบจาก user interview สำหรับระบบ Login
- Business Rules อย่างน้อย 3 ข้อ เช่น: จำนวนครั้ง login ที่ทำได้ก่อน lock,
  session timeout, password expiry
- Constraints อย่างน้อย 2 ข้อ เช่น: PDPA (เก็บ log ไม่เกิน X วัน),
  password complexity ตาม policy องค์กร
- format: bullet list แบ่งหัวข้อชัดเจน

workshop-demo/user-story.md
- Statement: As a [user] I want to [action] So that [benefit]
- Conditions ระบุ Type ชัดเจน: Business Rule / Constraint
- Related Documents section (ว่างไว้)

workshop-demo/user-flow.md
- Mermaid flowchart ครอบคลุมทุก logic path:
  Happy Path: login สำเร็จ → redirect dashboard
  Negative: password ผิด → error message, Negative: email ไม่มีในระบบ → error
  Edge Case: login ผิดครบ 5 ครั้ง → lock account + แสดง unlock instructions
- Field Definitions: email, password, attempt_count, locked_until, session_token

workshop-demo/business-tc.md
- Flat list TC format: | TC-ID | Title | AC-Ref | Test Data | Expected Result | Label |
- Label: Happy Path / Negative / Edge Case
- ครอบคลุมทุก path ใน user-flow.md อย่างน้อย 8 TC

─────────────────────────────────────
TASK 2 — สร้างเนื้อหา GitHub Copilot Custom Instructions
─────────────────────────────────────

.github/copilot-instructions.md (repository-wide global)
เนื้อหา:
- Project overview: workshop สอน GitHub Copilot Customization ใน VS Code
- Tech stack: TypeScript, Node.js, Playwright สำหรับ E2E test
- Document workflow ของทีม:
  requirements-notes.md → user-story.md → user-flow.md
  → scenarios.md → scenario-[id].md → business-tc.md
  → frontend-tech-spec.md / backend-tech-spec.md → qa-test-spec.md
- Naming convention: kebab-case ทุกไฟล์
- ห้ามสร้างไฟล์นอก structure ที่กำหนด

.github/instructions/scenario.instructions.md
frontmatter: applyTo: "**/*scenario*.md"
เนื้อหา:
- Responsibility: เขียน Logic Path และ Acceptance Criteria (AC)
- Scope: แตก scenario จาก user-flow, เขียน AC ในมุม user ไม่ใช่ system
- Must NOT contain: technical implementation detail, code, API spec
- AC format: Given / When / Then
- ทุก AC ต้องมี Title และ reference Condition ที่เกี่ยวข้อง
- ครอบคลุม Happy Path, Negative, Edge Case

.github/instructions/tech-spec.instructions.md
frontmatter: applyTo: "**/*-tech-spec.md"
เนื้อหา:
- Responsibility: เขียน technical specification สำหรับ dev implement
- Frontend scope: UI Components, elementId, States, Handlers, Business Logic, Test Spec
- Backend scope: API Spec (endpoint, request, response), DB Schema, Business Logic, Test Spec
- Must NOT contain: business rule ที่ยังไม่ได้ sign off จาก user
- ทุก task ต้องมี Effort estimation (minutes)
- API Contract ต้องตรงกันระหว่าง frontend และ backend spec

.github/instructions/business-tc.instructions.md
frontmatter: applyTo: "**/*business-tc*.md"
เนื้อหา:
- Responsibility: Flat list TC ทั้งหมดของ story
- Format: table | TC-ID | Title | AC-Ref | Test Data | Expected Result | Label |
- 1 TC = 1 แถว, map กับ AC เดียวเท่านั้น
- Label ที่อนุญาต: Happy Path / Negative / Edge Case เท่านั้น
- ผลลัพธ์ต่างกัน = AC คนละข้อ, input ต่างกันผลเหมือนกัน = TC หลายแถวใน AC เดียว

─────────────────────────────────────
TASK 3 — สร้าง Copilot Custom Prompts และ Skills
─────────────────────────────────────

.github/prompts/create-tc.prompt.md
---
name: create-tc
description: สร้าง Business TC จาก AC ใน scenario ที่กำหนด
---
prompt body:
- รับ input scenarioId: #input:scenarioId
- อ่านไฟล์ scenario-{scenarioId}.md
- สร้าง TC สำหรับทุก AC ใน scenario นั้น
- format ตาม business-tc.instructions.md เป๊ะ
- append ใน workshop-demo/business-tc.md (ไม่ลบ TC เดิม)
- สรุปจำนวน TC ที่เพิ่มหลังเสร็จ

.github/prompts/review-coverage.prompt.md
---
name: review-coverage
description: ตรวจ TC coverage เทียบกับ user-flow
---
prompt body:
- อ่าน workshop-demo/user-flow.md และ workshop-demo/business-tc.md
- map แต่ละ logic path กับ TC ที่มี
- output เป็น markdown checklist: ✅ มี TC แล้ว / ❌ ยังขาด
- สรุปสัดส่วน coverage เป็น % ท้ายสุด

.github/skills/create-scenario/SKILL.md
---
name: create-scenario
description: สร้าง scenario file จาก logic path ใน user-flow.md
---
steps:
1. อ่าน workshop-demo/user-flow.md ระบุ logic path ทั้งหมด
2. เช็คว่า path ไหนยังไม่มี scenario file
3. สร้าง workshop-demo/scenario-[id]-[name].md สำหรับ path นั้น
   format: Logic Path section + AC section (Given/When/Then) + Condition Coverage
4. เพิ่ม entry ใน workshop-demo/scenarios.md (สร้างถ้ายังไม่มี)
5. แต่ละ AC ต้องครอบคลุมผลลัพธ์ที่ต่างกัน ไม่ใช่แค่ input ต่างกัน

─────────────────────────────────────
TASK 4 — อัปเดต .mcp.json และ .env.example
─────────────────────────────────────

.mcp.json มี placeholder อยู่แล้ว ให้ตรวจว่า JSON valid
และเพิ่ม comment บน .env.example อธิบาย step การขอ key:
1. ไปที่ https://trello.com/app-key → copy API Key
2. กด "Generate a Token" → copy Token
3. ใส่ใน .env (copy จาก .env.example)

─────────────────────────────────────
TASK 5 — สร้าง workshop-demo/README.md และ SETUP.md
─────────────────────────────────────

workshop-demo/README.md — guide สำหรับผู้เรียน:
1. Workshop นี้สอนอะไร (5 concepts: Instructions, Prompts, Skills, MCP, Agents)
2. File structure ของ workshop-demo/ พร้อมอธิบายแต่ละไฟล์
3. Exercise flow 4 ข้อ:
   Ex1: เปิด scenario-01.md → สังเกต instruction โหลดอัตโนมัติใน References
   Ex2: /create-tc → ใส่ scenario ID → ดู TC ที่ Copilot สร้าง
   Ex3: /review-coverage → ดู coverage report
   Ex4: MCP Trello → สั่ง Copilot สร้าง card จาก business-tc.md
4. Tips การ debug เมื่อ instruction ไม่ load

workshop-demo/SETUP.md — guide setup ก่อน workshop:
1. ติดตั้ง VS Code extension: github.copilot + github.copilot-chat
2. Sign in GitHub account ที่มี Copilot license
3. เปิด folder นี้ใน VS Code → .vscode/settings.json จะ apply อัตโนมัติ
4. ใส่ TRELLO_API_KEY และ TRELLO_TOKEN ใน .env (copy จาก .env.example)
5. verify: เปิด Copilot Chat → เปิด scenario file → ดู References panel

─────────────────────────────────────
สุดท้าย — Verify และสรุป
─────────────────────────────────────

หลังเสร็จทุก task:
1. แสดง tree ของ project ทั้งหมด
2. ตรวจ applyTo glob ทุก .instructions.md ว่าถูกต้อง
3. ตรวจ .mcp.json ว่าเป็น valid JSON
4. สรุป "สิ่งที่ต้องทำเองก่อนสอน" เป็น checklist สั้นๆ
```
