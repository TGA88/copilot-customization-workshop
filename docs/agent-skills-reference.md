# Agent Skills — เอกสารอ้างอิง (GitHub Copilot & Claude Code)

> เอกสารอ้างอิงเชิงเทคนิคสำหรับผู้สอน — Prompt vs Skill, SKILL.md รองรับไฟล์อะไรบ้าง
> และเทียบ GitHub Copilot กับ Claude Code อ้างอิงจากเอกสาร official (ดู Sources ท้ายไฟล์)
> ตรวจสอบล่าสุด: มิ.ย. 2026
>
> 📝 ถ้าต้องการ **สคริปต์ demo หน้า class** (บทพูด 2 นาที) ดู [prompt-vs-skill.md](prompt-vs-skill.md) แทน

---

## 1. ใน Copilot — Skill เป็น slash command เหมือน Prompt มั้ย?

**ใช่** — พิมพ์ `/` ใน Copilot Chat จะเห็น **ทั้ง skills และ prompts** อยู่ในลิสต์เดียวกัน เลือกเรียกได้เลย (เช่น `/create-scenario`, `/create-tc`)

แต่ **skill ทำได้มากกว่า** prompt เพราะถูกเรียกได้ 2 ทาง และ bundle ไฟล์ได้:

| | เรียกด้วย `/` (manual) | โมเดล/Agent เรียกเองอัตโนมัติ | bundle ไฟล์ประกอบ | จำนวนขั้นตอน |
|---|:---:|:---:|:---:|---|
| **Prompt** (`.prompt.md`) | ✅ | ❌ | ❌ | template สั่งครั้งเดียว |
| **Skill** (`SKILL.md`)   | ✅ | ✅ (จาก `description`) | ✅ | workflow หลายขั้น |

> ❌ **เข้าใจผิดที่พบบ่อย:** "prompt เรียกด้วย slash, skill เรียกในโหมด Agent"
> ความจริง: **เรียกด้วย `/` ได้ทั้งคู่** — จุดต่างคือ skill เพิ่ม auto-invoke + bundle ไฟล์ + multi-step

**คุม invocation ของ skill ได้ด้วย frontmatter:**
- `disable-model-invocation: true` → ปิด auto, ให้เรียก manual ผ่าน `/` เท่านั้น
- `user-invocable: false` → ซ่อนจากเมนู `/`, ให้เป็น background knowledge ที่โมเดลหยิบเอง

---

## 2. นอกจาก SKILL.md แล้ว skill รองรับไฟล์อื่นมั้ย?

**รองรับ** — skill คือ **โฟลเดอร์** ที่ bundle ไฟล์ประกอบได้ ไม่ใช่ไฟล์เดี่ยว และโหลดแบบ **progressive disclosure** (ประหยัด token):

1. **description** → โหลดเข้า context เสมอ (เพื่อให้โมเดลรู้ว่ามี skill อะไรบ้าง)
2. **เนื้อ SKILL.md** → โหลดเฉพาะตอน skill ถูกเรียก
3. **ไฟล์ประกอบ** → โหลดเมื่อ SKILL.md อ้างถึง (ผ่าน relative path) เท่านั้น

ตัวอย่างไฟล์ประกอบ: scripts (เช่น `.py`, `.sh`, `.js`), templates, example/sample directories, reference markdown, data/assets

```
.github/skills/create-scenario/
├── SKILL.md            ← entrypoint (frontmatter + ขั้นตอน)
├── scripts/            ← (ออปชัน) สคริปต์ที่ skill เรียกใช้
├── templates/          ← (ออปชัน) เทมเพลตผลลัพธ์
└── examples/           ← (ออปชัน) ตัวอย่างอ้างอิง
```

---

## 3. GitHub Copilot vs Claude Code — เทียบกัน

| | **GitHub Copilot** | **Claude Code** |
|---|---|---|
| **ไฟล์ประกอบ** | scripts, templates, examples, resources (relative path) | reference markdown, scripts (py/bash), templates, assets |
| **ที่เก็บ (project)** | `.github/skills/`, `.claude/skills/`, `.agents/skills/` | `.claude/skills/` |
| **ที่เก็บ (personal)** | `~/.copilot/skills/`, `~/.claude/skills/`, `~/.agents/skills/` | `~/.claude/skills/` |
| **frontmatter (required)** | `name`, `description` | `name`, `description` |
| **frontmatter (optional)** | `argument-hint`, `user-invocable`, `disable-model-invocation`, `context` | ข้างซ้าย + `allowed-tools`, `disallowed-tools`, `model`, `effort`, `agent`, `hooks`, `paths`, `arguments`, `when_to_use`, `shell` |
| **invocation** | `/` manual + auto จาก description | เหมือนกัน (`.claude/commands/` ถูกรวมเข้า skills system แล้ว) |

> **กุญแจสำคัญ:** Agent Skills เป็น **open standard** (https://agentskills.io) ใช้ข้าม agent ได้ —
> ทั้ง GitHub Copilot (VS Code / CLI / cloud agent) และ Claude
> นี่คือเหตุผลที่ Copilot อ่าน `.claude/skills/` ได้ และ format `SKILL.md` ใช้ร่วมกัน
> (Claude Code รองรับ frontmatter เฉพาะตัวเพิ่มเติมมากกว่า เช่น `allowed-tools`, `model`, `hooks`)

---

## 4. แล้ว Prompt / Instructions / Custom Agent ต่างกันยังไง? (ภาพรวม Copilot)

| ฟีเจอร์ | ไฟล์ | เรียกยังไง | ใช้ตอนไหน |
|---|---|---|---|
| **Custom Instructions** | `.github/copilot-instructions.md`, `.github/instructions/*.instructions.md` | โหลดเอง (auto ตาม `applyTo` glob) | "กฎ/บริบท" ที่อยากให้ติดตลอด |
| **Prompt** | `.github/prompts/*.prompt.md` | `/` manual เท่านั้น | template งานซ้ำ ๆ สั่งครั้งเดียวจบ |
| **Skill** | `.github/skills/*/SKILL.md` | `/` + auto-invoke | workflow หลายขั้น + bundle ไฟล์ |
| **Custom Agent** (chat mode) | `.github/agents/*.agent.md` | เลือกเป็น mode ของ session | persona + ชุด tool + โมเดล สำหรับทั้งบทสนทนา |

---

## Sources

- [VS Code — Use Agent Skills in VS Code](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [VS Code — Customize AI in Visual Studio Code (overview)](https://code.visualstudio.com/docs/copilot/customization/overview)
- [GitHub Docs — Prompt files](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files)
- [Claude Code — Skills](https://code.claude.com/docs/en/skills)
- [Agent Skills — open standard](https://agentskills.io)
