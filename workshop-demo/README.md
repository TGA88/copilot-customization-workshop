# Workshop — GitHub Copilot Customization ใน VS Code

guide สำหรับผู้เรียน 👋 ใช้ feature **"ระบบ Login"** เป็น demo ตลอด workshop

---

## 1. Workshop นี้สอนอะไร (5 Concepts)

| # | Concept | คืออะไร |
|---|---------|---------|
| 1 | **Custom Instructions** | กฎ/บริบทที่ Copilot โหลดอัตโนมัติตามไฟล์ที่กำลังทำงาน (`.github/instructions/*.instructions.md` + `copilot-instructions.md`) |
| 2 | **Custom Prompts** | template สั่งครั้งเดียว เรียก `/` แบบ manual เช่น `/create-tc` (`.github/prompts/*.prompt.md`) |
| 3 | **Skills** | workflow หลายขั้น + bundle ไฟล์ได้ — เรียก `/` ก็ได้ Agent หยิบเองก็ได้ (`.github/skills/*/SKILL.md`) · ดู [agent-skills-reference.md](../docs/agent-skills-reference.md) |
| 4 | **MCP** | ต่อ Copilot เข้ากับเครื่องมือภายนอก — workshop นี้ใช้ **GitHub** (สร้าง Issue, `.mcp.json`) |
| 5 | **Agents** | ให้ Copilot ทำงานหลายขั้นตอนต่อเนื่องเองในโหมด Agent |

---

## 2. File Structure ของ workshop-demo/

```
workshop-demo/
├── README.md              ← ไฟล์นี้ — guide ผู้เรียน
├── SETUP.md               ← ขั้นตอน setup ก่อนเริ่ม
├── requirements-notes.md  ← requirement ดิบจาก interview (จุดเริ่มต้น workflow)
├── user-story.md          ← Statement + Conditions (Business Rule / Constraint)
├── user-flow.md           ← Mermaid flow ทุก logic path + Field Definitions
├── scenarios.md           ← (สร้างโดย skill) index ของ scenario ทั้งหมด
├── scenario-[id]-[name].md← (สร้างโดย skill create-scenario) Logic Path + AC
└── business-tc.md         ← Flat list Test Case map กับ AC
```

> instruction files อยู่ที่ `.github/instructions/` และจะ **โหลดอัตโนมัติ** ตาม `applyTo` glob เมื่อเปิดไฟล์ที่ตรง pattern

---

## 3. Exercise Flow (5 กิจกรรม — เรียงตามลำดับสอน)

> ลำดับตรงกับ Session ใน [workshop-agenda.md](../docs/workshop-agenda.md) (concept order **1→3→2→4/5**)
> เลข Ex ตรงกับ agenda/speaker-notes — ตัว `create-scenario` เป็น skill จึงไม่มีเลข Ex แต่เป็น **กิจกรรมเต็มตัว** (อย่ามองข้าม)

### Ex1 — Custom Instructions โหลดอัตโนมัติ · *Session 2*
1. เปิดไฟล์ใด ๆ ที่มีคำว่า `scenario` ในชื่อ
2. เปิด Copilot Chat → สังเกตที่ panel **References**
3. จะเห็น `scenario.instructions.md` ถูกโหลดเข้ามาเองเพราะ filename ตรง glob `**/*scenario*.md`

### 🛠️ Skill — `create-scenario` (สร้าง scenario) · *Session 3*
> **หัวใจของ demo** — ต้องมี scenario ก่อน ถึงจะทำ Ex2 `/create-tc` ในขั้นถัดไปได้
1. เรียก skill ด้วย `/create-scenario` (หรือปล่อยให้ Agent หยิบใช้เองจาก description)
2. Copilot อ่าน `user-flow.md` → หา logic path → สร้าง `scenario-[id]-[name].md` พร้อม AC (Given/When/Then)
3. สร้าง/อัปเดต `scenarios.md` เป็น index
4. เปิดไฟล์ scenario ที่ได้ → ยืนยันว่าไม่มี implementation detail (เคารพ instruction จาก Ex1)

### Ex2 — Custom Prompt `/create-tc` · *Session 4*
1. พิมพ์ `/create-tc` ใน Copilot Chat
2. ใส่ scenario ID (เช่น `01`)
3. ดู Copilot อ่าน scenario → สร้าง TC ตาม format → append ลง `business-tc.md`

### Ex3 — Custom Prompt `/review-coverage` · *Session 4*
1. พิมพ์ `/review-coverage`
2. ดู coverage report เป็น checklist ✅ / ❌ และ % coverage เทียบกับ logic path ใน user-flow

### Ex4 — MCP GitHub + Agent · *Session 5*
1. ตรวจว่า sign in GitHub แล้ว + รู้ repo เป้าหมาย (ดู SETUP.md)
2. สั่ง Copilot (โหมด Agent):
   > "อ่าน business-tc.md แล้วสร้าง GitHub Issue หนึ่งอันต่อหนึ่ง TC ใน repo `TGA88/copilot-workshop-issues-demo`"
   - 🛠️ **แบบ hands-on:** เปลี่ยน repo เป็น `<username-ของคุณ>/<repo-ของคุณ>`
3. ดู issue ถูกสร้างบน GitHub ผ่าน MCP (มี label ตาม Label ของ TC ได้)

> 💡 Bonus (ถ้าเหลือเวลา): สั่งต่อให้จัด issue เข้า **GitHub Projects board** เป็นคอลัมน์ตาม Label

---

## 4. Tips — Debug เมื่อ Instruction ไม่ Load

- เช็ค `.vscode/settings.json` ว่า `github.copilot.chat.codeGeneration.useInstructionFiles: true`
- เช็ค `applyTo` glob ใน frontmatter ว่าตรงกับ **ชื่อไฟล์ที่กำลังเปิด** จริง ๆ
- ชื่อไฟล์ scenario ต้องมีคำว่า `scenario` (glob = `**/*scenario*.md`)
- เปิด Copilot Chat แล้วดู panel **References** — ถ้าไม่ขึ้น instruction แปลว่า glob ไม่ match
- reload VS Code window (`Cmd/Ctrl+Shift+P` → "Developer: Reload Window") หลังแก้ settings
- ต้อง sign in ด้วย GitHub account ที่มี Copilot license
