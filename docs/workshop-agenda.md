# Workshop Agenda — GitHub Copilot Customization ใน VS Code

> คู่มือลำดับการสอนสำหรับผู้สอน (instructor guide)
> Theme: ใช้ feature **"ระบบ Login"** เป็น demo ตลอดงาน
> ระยะเวลารวมโดยประมาณ: **~2.5 – 3 ชั่วโมง** (ปรับได้)

---

## 🎯 เป้าหมายของ Workshop

ให้ผู้เรียนเข้าใจและใช้ GitHub Copilot Customization ได้ 5 อย่าง โดยร้อยเรียงผ่าน **workflow จริงของทีม**: Requirements → User Story → User Flow → Scenario → Test Case → Tech Spec

| # | Concept | ไฟล์ที่เกี่ยวข้อง |
|---|---------|-------------------|
| 1 | Custom Instructions | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` |
| 2 | Custom Prompts | `.github/prompts/*.prompt.md` |
| 3 | Skills | `.github/skills/create-scenario/SKILL.md` |
| 4 | MCP (Trello) | `.mcp.json`, `.env` |
| 5 | Agents | โหมด Agent ใน Copilot Chat |

---

## 🧭 แนวคิดหลักที่ต้องสื่อให้ผู้เรียนเข้าใจ

> **"เอกสารทุกอย่างเป็น text ที่ Copilot อ่านต่อกันได้"**
> แต่ละขั้นใน workflow ป้อนผลให้ขั้นถัดไป และ instruction คือ "กฎ" ที่บังคับให้ output แต่ละขั้นมี format ที่ถูกต้อง

```
requirements-notes → user-story → user-flow → scenario → business-tc → tech-spec → qa-test-spec
```

---

## ⏱️ ลำดับการสอน (Session Flow)

### Session 0 — Setup & Warm-up (15 นาที)
**เป้า:** ทุกเครื่องพร้อมก่อนเริ่มจริง

1. ให้ผู้เรียนทำตาม [SETUP.md](../workshop-demo/SETUP.md) ให้ครบ
   - ติดตั้ง extension `github.copilot` + `github.copilot-chat`
   - Sign in GitHub (มี Copilot license)
   - เปิด folder root ใน VS Code
   - ใส่ Trello key ใน `.env` (ทำล่วงหน้าได้)
2. เช็ค checklist ท้าย SETUP.md ว่าผ่านทุกข้อ
3. **Checkpoint:** เปิด Copilot Chat ได้ + เห็นไอคอน active

---

### Session 1 — ทำไมต้อง Customize? (15 นาที) · *บรรยาย*
**เป้า:** ให้เห็นปัญหาก่อนเห็นเครื่องมือ

1. สาธิต Copilot แบบ default: ขอให้สร้าง test case → ได้ format มั่ว ไม่ตรงทีม
2. ชี้ปัญหา: ทีมมี convention (naming, format TC, แยก business/tech) แต่ Copilot ไม่รู้
3. โยงเข้าหา 5 concepts ว่าแต่ละอันแก้ปัญหาอะไร
4. เปิด [README.md](../workshop-demo/README.md) อธิบาย file structure + workflow ของทีม

---

### Session 2 — Custom Instructions (30 นาที) · *Concept 1*
**เป้า:** เข้าใจ instruction ที่โหลดอัตโนมัติตามไฟล์ที่เปิด

1. **บรรยาย:** มี 2 ระดับ
   - Global: [copilot-instructions.md](../.github/copilot-instructions.md) (โหลดทุกครั้ง)
   - Scoped: [instructions/](../.github/instructions/) ที่ใช้ `applyTo` glob
2. เปิด `.github/instructions/scenario.instructions.md` → ชี้ frontmatter `applyTo: "**/*scenario*.md"`
3. **▶️ Exercise 1:** เปิดไฟล์ที่มีคำว่า `scenario` ในชื่อ → เปิด Copilot Chat → ดู panel **References** ว่า `scenario.instructions.md` ถูกโหลดเข้ามาเอง
4. ทดลองเปิดไฟล์ที่ไม่ match glob → instruction หาย → เข้าใจว่า glob ทำงานยังไง
5. **Debug tips:** ถ้าไม่โหลด ดู `.vscode/settings.json` (`useInstructionFiles: true`) + reload window

> 💡 จุดสำคัญที่ต้องย้ำ: แยก responsibility — scenario = มุม user, tech-spec = มุม dev, business-tc = flat list

---

### Session 3 — Skills: สร้าง Scenario (30 นาที) · *Concept 3*
**เป้า:** ให้ Copilot ทำ workflow หลายขั้นตามที่กำหนด

1. เปิด [create-scenario/SKILL.md](../.github/skills/create-scenario/SKILL.md) อ่าน steps ทีละข้อ
2. **▶️ Exercise (สร้าง scenario):** เรียก skill `create-scenario`
   - Copilot อ่าน `user-flow.md` → หา logic path (LP-1…LP-6)
   - สร้าง `scenario-[id]-[name].md` พร้อม AC (Given/When/Then)
   - สร้าง/อัปเดต `scenarios.md` เป็น index
3. ชี้ให้เห็นว่า scenario ที่ได้ **เคารพ instruction** (ไม่มี implementation detail, AC อ้าง COND)
4. **เชื่อมโยง:** ตอนนี้เรามี scenario แล้ว → พร้อมสร้าง TC ใน session ถัดไป

> ⚠️ scenario files ไม่ได้เตรียมไว้ล่วงหน้า — ผู้เรียนสร้างเองตรงนี้ คือหัวใจของ demo

---

### Session 4 — Custom Prompts: สร้าง & ตรวจ TC (30 นาที) · *Concept 2*
**เป้า:** ใช้คำสั่งสำเร็จรูปเรียกงานซ้ำ ๆ ด้วย `/`

1. **▶️ Exercise 2 — `/create-tc`:**
   - พิมพ์ `/create-tc` → ใส่ scenario ID (เช่น `01`)
   - Copilot อ่าน scenario → สร้าง TC ตาม format → **append** ลง [business-tc.md](../workshop-demo/business-tc.md)
   - ชี้ให้เห็น TC ใหม่ใช้ format ตรงตาม `business-tc.instructions.md` (Label = Happy/Negative/Edge เท่านั้น)
2. **▶️ Exercise 3 — `/review-coverage`:**
   - พิมพ์ `/review-coverage`
   - Copilot map logic path ↔ TC → output checklist ✅/❌ + % coverage
3. **อภิปราย:** ความต่างระหว่าง prompt (งานครั้งเดียวจบ) กับ skill (workflow หลายขั้น)

---

### Session 5 — MCP: ต่อกับ Trello (30 นาที) · *Concept 4 + 5*
**เป้า:** ให้ Copilot ใช้เครื่องมือภายนอก + ทำงานต่อเนื่องในโหมด Agent

1. **บรรยาย MCP:** เปิด [.mcp.json](../.mcp.json) อธิบาย server `trello` + env key
2. ตรวจว่า `.env` มี key จริง (ทำใน Session 0) → โหมด Agent มองเห็น MCP server
3. **▶️ Exercise 4:** สั่ง Copilot (โหมด Agent):
   > "อ่าน business-tc.md แล้วสร้าง Trello card หนึ่งใบต่อหนึ่ง TC"
   - ดู Copilot เรียก MCP tool สร้าง card บน Trello board จริง
4. **สรุป Agents:** จุดต่างจากโหมด chat ปกติ — Agent วางแผน + เรียก tool หลายขั้นเองได้

---

### Session 6 — Wrap-up & Q&A (15 นาที)
1. ทบทวน 5 concepts ผ่านสิ่งที่เพิ่งทำมือ
2. แผนภาพรวม: instruction (กฎ) + prompt (คำสั่งซ้ำ) + skill (workflow) + MCP (เครื่องมือ) + agent (ตัวขับ)
3. แนะนำการนำไปใช้กับ repo จริงของทีม
4. Q&A + แจก checklist debug จาก README.md

---

## 📊 สรุปตารางเวลา

| Session | หัวข้อ | Concept | เวลา | Exercise |
|---------|--------|---------|------|----------|
| 0 | Setup & Warm-up | — | 15 น. | — |
| 1 | ทำไมต้อง Customize | (intro) | 15 น. | — |
| 2 | Custom Instructions | 1 | 30 น. | Ex1 |
| 3 | Skills: create-scenario | 3 | 30 น. | สร้าง scenario |
| 4 | Custom Prompts | 2 | 30 น. | Ex2, Ex3 |
| 5 | MCP + Agents | 4, 5 | 30 น. | Ex4 |
| 6 | Wrap-up & Q&A | — | 15 น. | — |
| | **รวม** | | **~2.5 ชม.** | |

> ลำดับ concept สอนเป็น **1 → 3 → 2 → 4/5** โดยตั้งใจ เพราะต้องมี scenario (จาก skill) ก่อน ถึงจะสร้าง TC (จาก prompt) ได้ — ทำให้ flow ต่อเนื่องเป็นเรื่องเดียวกัน

---

## ✅ Checklist ผู้สอนก่อนเริ่ม

- [ ] ทดสอบ run ทุก exercise ด้วยตัวเองจนจบ (โดยเฉพาะ MCP Trello)
- [ ] เตรียม Trello board เปล่าไว้ demo Ex4
- [ ] เตรียม key สำรอง / บัญชี Copilot สำรอง เผื่อผู้เรียนติดปัญหา
- [ ] เตรียมตัวอย่าง "Copilot แบบ default ทำพัง" ไว้เปิด Session 1
- [ ] เผื่อเวลา buffer ตอน Setup (มักช้าสุด)
