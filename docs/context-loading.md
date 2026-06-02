# Context Window — Instruction / Prompt / Skill โหลดเข้า context ยังไง

> เอกสารอ้างอิงสำหรับผู้สอน — สรุปว่าแต่ละ customization ถูก "โหลดเข้า context window"
> ตอนไหน, สะสมมั้ย, และเต็มแล้วเกิดอะไร อ้างอิงจากเอกสาร official (ดู Sources ท้ายไฟล์)
> ตรวจสอบล่าสุด: มิ.ย. 2026 · คู่กับ [agent-skills-reference.md](agent-skills-reference.md)

---

## หลักการพื้นฐาน: ทุก request "ประกอบ context ใหม่"

Copilot **ไม่ได้** โหลดของเข้า context แล้วแช่ไว้ถาวร — แต่ละครั้งที่คุณส่งข้อความ มัน**สร้าง package ใหม่ทั้งก้อน**:

```
[ request ปัจจุบัน ] = instruction ที่ match ตอนนี้
                     + ประวัติบทสนทนา (turn ก่อน ๆ + tool output)
                     + ข้อความใหม่ของคุณ
                     + ไฟล์/บริบทที่แนบ
```

→ สิ่งที่ทำให้ context เต็มคือ **ประวัติบทสนทนาที่โตขึ้น** (turn, tool output, ไฟล์แนบ)
ไม่ใช่ instruction เล็ก ๆ ที่ส่งซ้ำ — และเมื่อจวนเต็ม VS Code จะ **compact (สรุปย่อ)** ของเก่าทิ้งอัตโนมัติ

---

## เทียบ 3 อย่าง: โหลดตอนไหน + สะสมมั้ย

| | ตอน **ไม่ได้ใช้** | ตอน **ใช้** | เรียกซ้ำ → สะสมมั้ย |
|---|---|---|---|
| **Instruction** (`*.instructions.md`) | อยู่ใน context ถ้าไฟล์ match `applyTo` | ทั้งก้อน (re-inject ต่อ request) | ❌ ชุดเดียวต่อ request — ไม่กองซ้อน |
| **Prompt** (`*.prompt.md`) | ❌ ไม่อยู่เลย (โมเดลไม่รู้ด้วยซ้ำ) | เนื้อ prompt เฉพาะ turn ที่พิมพ์ `/` | ✅ แต่ละครั้งเป็น turn ใหม่ → สะสมในประวัติ |
| **Skill** (`SKILL.md`) | แค่ `description` จิ๋ว ๆ (always-on) | body + ไฟล์ที่อ้างถึง ตอนถูกเรียก | ✅ default สะสม · ❌ ถ้า `context: fork` |

### จุดต่างที่ต้องเข้าใจ
- **Instruction** = "ป้ายกฎติดผนัง" — มองเห็นชุดเดียวตลอด ประกอบใหม่ทุก request **ไม่ทับกัน**
- **Prompt** = "ตะโกนสั่งใหม่ทุกครั้ง" — เสียงค้างในห้อง เรียกซ้ำ = เนื้อ prompt กองในประวัติ
- **Skill** = "คู่มือในลิ้นชัก" — หยิบมาอ่านเฉพาะตอนใช้ (progressive disclosure)

---

## เจาะลึก Skill: script vs asset โหลดต่างกัน

| องค์ประกอบ | โมเดลทำอะไร | อะไรเข้า context |
|---|---|---|
| `references/`, `assets/` (ไฟล์ข้อความ) | **อ่าน** | **เนื้อไฟล์ทั้งอัน** |
| `scripts/*.py` | **รัน** | **แค่ output (stdout)** — ตัวโค้ดไม่ถูกโหลด |

→ script ประหยัดสุด: โค้ดยาวแค่ไหน context ก็เห็นแค่ "ผลลัพธ์" (เช่น JSON จาก `check_tc.py`)

### Progressive disclosure 3 ชั้นของ skill
1. **Discovery** — `name` + `description` โหลดเสมอ (จิ๋ว) ให้โมเดลรู้ว่ามี skill นี้ + ควรใช้ตอนไหน
2. **Body** — เนื้อ `SKILL.md` โหลดตอนถูกเรียก
3. **Resources** — ไฟล์ใน `scripts/` `references/` `assets/` โหลดเมื่อ **SKILL.md อ้างถึงและโมเดลใช้จริง** เท่านั้น

---

## `context: fork` — เก็บแค่ result ไม่สะสมรายละเอียด

ตั้ง `context: fork` ใน frontmatter ของ `SKILL.md` → skill รันใน **subagent แยก**:

> *"the skill executes in a dedicated subagent and **only its final result is returned** to the parent agent... its temporary context is discarded."*

| | default (ไม่ fork) | `context: fork` |
|---|---|---|
| body / อ่าน references / script output | เข้า **main context** | เข้า **subagent** แล้วทิ้ง |
| main chat ได้อะไร | ทุกขั้น | **แค่ผลลัพธ์สุดท้าย** |
| เรียกซ้ำ 3 รอบ | สะสม 3 ชุด | main เก็บแค่ 3 ผลลัพธ์ |

→ skill หนัก (script + references เยอะ) อย่าง `tc-audit` ตั้ง `context: fork` ไว้ → main context สะอาด เรียกกี่รอบก็ไม่บวม

### ⚠️ `context: fork` ไม่ใช่ทุก agent (vendor-specific)
ตัว SKILL.md หลัก (name/description/scripts/references/assets) เป็น **open standard** ใช้ได้ทุก agent
แต่ `context: fork` เป็น **extension** ที่ต้องอาศัย subagent — **รองรับไม่เท่ากัน**:

| Agent | SKILL.md หลัก | `context: fork` |
|---|:---:|:---:|
| GitHub Copilot (VS Code) | ✅ | ✅ |
| Claude Code | ✅ | ✅ (มี caveat บาง path — [issue #17283](https://github.com/anthropics/claude-code/issues/17283)) |
| OpenAI Codex CLI | ✅ | ❌ **ignore → รัน inline** |
| Gemini CLI / Cursor | ✅ | ❌ ส่วนใหญ่ ignore |

→ field ที่ไม่รองรับถูก **ignore เฉย ๆ ไม่พัง** — skill ยัง portable แต่บน Codex ตัว `tc-audit`
จะ**รัน inline** (output + การอ่านไฟล์เข้า main context และสะสม เหมือนไม่ได้ตั้ง fork)

### isolate context ต้องใช้ fork/subagent — ไม่ใช่ "สลับ custom agent"
**สลับไปใช้ Custom Agent (chat mode) ไม่ได้แยก context** — ยังเป็น main chat เดิม
context isolation มาจากการ **delegate เป็น subagent** (ผ่าน `context: fork`) เท่านั้น
อยากได้ทั้ง isolation + tool จำกัด (เช่น read-only) → fork เข้า custom **sub**agent ผ่าน field `agent:` (vendor-specific)

> ถ้า agent ไม่ honor `context: fork` (เช่น Codex) แต่มี subagent → **สั่ง delegate เอง** ตอนเรียก
> ("ใช้ subagent รัน skill นี้") โดยใช้ subagent **built-in** ก็ได้ ไม่ต้องสร้าง custom agent
> custom agent จำเป็นก็ต่อเมื่ออยาก **ล็อก persona/model/tool/sandbox ให้แน่นอน**

---

## subagent ใช้ model อะไร + คุมยังไง

- **default ทุก platform:** subagent ใช้ **model ของ parent session** (ไม่ระบุ = inherit)
- **prompt/instruction คุม model ไม่ได้** — model เป็น **config-level** ไม่ใช่ prompt-level
- **วิธีดู:** ไม่มี UI มาตรฐานบอกชัด ๆ ว่า subagent รัน model ไหน → verify จาก **config เอง** (frontmatter / agent def / env var)

### คุม model ของ skill/subagent — อยู่คนละที่ในแต่ละ platform
| | คุม model ที่ SKILL.md ได้เลย | ต้องมี custom agent แยก | global override |
|---|:---:|---|---|
| **Claude Code** | ✅ `model:` ใน SKILL.md (+ `context: fork` + `agent:`) | ไม่ต้อง | env `CLAUDE_CODE_SUBAGENT_MODEL` |
| **GitHub Copilot** | ❌ (skill ไม่มี field `model`) | ต้องตั้งที่ custom agent (`.agent.md`) | — |
| **OpenAI Codex** | ❌ (ignore fork/model ที่ skill) | delegate explicit + custom agent TOML (`model`, `model_reasoning_effort`) | profiles |

> **ตกผลึก:** "model = config ไม่ใช่ prompt" จริงทุก platform — แต่ **"config" อยู่คนละที่**
> Claude Code วางที่ SKILL.md ได้เลย (เบาสุด) · Copilot/Codex ต้องไปที่ custom agent
> → บน Claude Code **ไม่ต้องสร้าง custom agent เพื่อคุม model** แค่ใส่ `model:` ใน skill

ตัวอย่าง Claude Code (คุม model + isolate ครบที่ frontmatter เดียว):
```yaml
---
name: tc-audit
model: sonnet           # คุม model ของ skill
context: fork           # isolate ใน subagent
agent: general-purpose  # (ออปชัน) เลือกชนิด subagent
---
```

---

## กฎเลือกใช้ + ประหยัด token

| สถานการณ์ | เลือก | เพราะ |
|---|---|---|
| กฎที่ต้องมีเสมอกับไฟล์ชนิดหนึ่ง | **Instruction (scoped `applyTo`)** | โหลดเฉพาะ request ที่เกี่ยว ไม่ถ่วงทุกบทสนทนา |
| งานเรียกเป็นครั้ง ๆ อินพุตตรง | **Prompt** | 0 token จนกว่าจะเรียก |
| ความสามารถใหญ่ + มี script/ไฟล์ ใช้บางที | **Skill** (+ `context: fork`) | จ่ายแค่ description ตอนพัก, ขยายตอนใช้, fork กัน main บวม |

**ข้อควรระวัง:**
- `copilot-instructions.md` (global) ถูกส่ง **ทุก request** ไม่ว่าทำไฟล์อะไร → เขียนให้กระชับ
- เรียก prompt เดิมซ้ำหลายรอบในแชตเดียว → เนื้อสะสม → ถ้าไม่ต่อเนื่องให้ **เปิด chat ใหม่**
- งานหนักที่ output เยอะ → ใช้ skill + `context: fork` เพื่อกัน main context

---

## ⚠️ ส่วนที่ docs ไม่ได้ระบุละเอียด (ไม่ assert เกินจริง)
- ต้อง "เปิดไฟล์" หรือแค่ "อ้างถึง/มีใน context" ก็ทริก `applyTo` ได้ — ไม่ได้บอกชัด
- การนับ token แบบ turn-by-turn / รายละเอียด compaction — อยู่นอกขอบเขตที่ doc เผยแพร่
- พฤติกรรมที่สรุปไว้คือ "per-request assembly + progressive disclosure + fork" ตามที่ doc ระบุและสังเกตได้

---

## Sources
- [VS Code — Use custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [VS Code — Agent Skills (progressive disclosure + forked context)](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [VS Code — Subagents](https://code.visualstudio.com/docs/copilot/agents/subagents)
- [VS Code — Manage context for AI (compaction)](https://code.visualstudio.com/docs/copilot/chat/copilot-chat-context)
- [GitHub Docs — Prompt files](https://docs.github.com/en/copilot/tutorials/customization-library/prompt-files)
