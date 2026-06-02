# Speaker Notes — สคริปต์พูดสำหรับผู้สอน

> ใช้คู่กับ [workshop-agenda.md](workshop-agenda.md)
> 🗣️ = บทพูด (พูดตามได้เลยหรือดัดแปลง) · 🎬 = สิ่งที่ทำหน้าจอ · ❓ = คำถามชวนคุย · ⚠️ = จุดที่มักพลาด

---

## Session 0 — Setup & Warm-up (15 นาที)

🗣️ "ก่อนเริ่ม ขอให้ทุกคนเปิด VS Code แล้วทำตาม SETUP.md ให้ครบก่อนนะครับ เดี๋ยวเราจะเช็คทีละข้อพร้อมกัน เพราะถ้า setup ไม่ผ่าน เดี๋ยว exercise จะทำไม่ได้"

🎬 ฉาย [SETUP.md](../workshop-demo/SETUP.md) บนจอ เดินทีละข้อ
🎬 ให้ทุกคนเปิด Copilot Chat (`Cmd/Ctrl+Alt+I`) ยกมือถ้าเห็นหน้าต่าง chat

⚠️ Setup คือช่วงที่ช้าที่สุดเสมอ — เผื่อเวลา อย่าเพิ่งเริ่มเนื้อหาจนกว่าจะเห็นว่าส่วนใหญ่พร้อม
⚠️ คนที่ไม่มี Copilot license จะติดตรงนี้ — เตรียมบัญชีสำรองหรือจับคู่กับเพื่อน

❓ "ใครเห็นไอคอน Copilot ติดเขียวที่มุมล่างขวาแล้วบ้าง?"

---

## Session 1 — ทำไมต้อง Customize? (15 นาที)

🗣️ "ก่อนจะไปดูเครื่องมือ ผมอยากให้เห็นปัญหาก่อน Copilot เก่งนะ แต่มันไม่รู้จัก convention ของทีมเรา"

🎬 **Live demo แบบ default:** เปิด chat ธรรมดา พิมพ์ "ช่วยสร้าง test case สำหรับหน้า login"
🎬 ให้ผู้เรียนดูผลลัพธ์ที่ได้ — format มั่ว ไม่มี TC-ID ไม่มี Label ไม่ตรงทีม

🗣️ "เห็นไหมครับ มันสร้างได้ แต่ format ไม่ตรงที่ทีมเราใช้เลย ถ้าเราต้องมานั่งแก้เองทุกครั้งก็ไม่ต่างจากเขียนเอง วันนี้เราจะสอน Copilot ให้รู้กฎของทีม ผ่าน 5 อย่าง"

🎬 เปิด [README.md](../workshop-demo/README.md) ชี้ตาราง 5 concepts + workflow pipeline

🗣️ "หัวใจของวันนี้คือประโยคเดียว — **'เอกสารทุกอย่างเป็น text ที่ Copilot อ่านต่อกันได้'** ผลของขั้นนึงเป็น input ของขั้นถัดไป requirements → user story → flow → scenario → test case"

❓ "ใครเคยเจอปัญหา Copilot ตอบไม่ตรง style ทีมบ้าง?" (ดึงให้เล่าประสบการณ์)

---

## Session 2 — Custom Instructions (30 นาที)

🗣️ "เริ่มจากตัวพื้นฐานที่สุด — Instructions คือ 'กฎ' ที่ Copilot จะอ่านเองอัตโนมัติ มี 2 ระดับ"

🎬 เปิด [copilot-instructions.md](../.github/copilot-instructions.md)
🗣️ "ตัวนี้คือ global โหลดทุกครั้งไม่ว่าทำงานไฟล์ไหน — ใส่ภาพรวมโปรเจกต์ tech stack convention การตั้งชื่อ"

🎬 เปิด [scenario.instructions.md](../.github/instructions/scenario.instructions.md) ชี้บรรทัดแรก
🗣️ "ดูตรง frontmatter นี้ครับ `applyTo: \"**/*scenario*.md\"` แปลว่า instruction นี้จะโผล่มา **เฉพาะตอนเราเปิดไฟล์ที่ชื่อมีคำว่า scenario** เท่านั้น — นี่คือความฉลาดของมัน กฎมาถูกที่ถูกเวลา"

🎬 **▶️ Exercise 1:**
1. ให้ทุกคนเปิดไฟล์อะไรก็ได้ที่มีคำว่า `scenario` ในชื่อ
2. เปิด Copilot Chat → ชี้ panel **References**
🗣️ "เห็นไหมครับ scenario.instructions.md โผล่มาเองใน References โดยที่เราไม่ได้สั่ง"

🎬 ทดลองเปิดไฟล์อื่นที่ไม่มีคำว่า scenario → instruction หายไป
🗣️ "พอเปลี่ยนไฟล์ที่ไม่ match glob มันก็หาย — นี่คือ scoped instruction"

⚠️ ถ้าใครไม่เห็น References: เช็ค `.vscode/settings.json` ว่า `useInstructionFiles: true` แล้ว reload window
🗣️ "จุดที่อยากย้ำ: เราแยกหน้าที่ชัดเจน — scenario เขียนมุม user, tech-spec มุม dev, business-tc เป็น flat list กฎพวกนี้กันไม่ให้ Copilot เอา technical detail ไปปนใน scenario"

❓ "ถ้าผมอยากให้ instruction โหลดเฉพาะไฟล์ใน folder backend จะเขียน glob ยังไง?" (ชวนคิด `**/backend/**`)

---

## Session 3 — Skills: สร้าง Scenario (30 นาที)

🗣️ "Instruction คือกฎ แต่ Skill คือ 'ขั้นตอนการทำงาน' — เราบอก Copilot เป็น step ว่าทำ 1-2-3-4 ยังไง"

🎬 เปิด [SKILL.md](../.github/skills/create-scenario/SKILL.md) อ่าน steps ทีละข้อให้ฟัง
🗣️ "ดูนะครับ step 1 อ่าน user-flow, step 2 เช็คว่า path ไหนยังไม่มี scenario, step 3 สร้างไฟล์, step 4 อัปเดต index — เป็น workflow ที่ทำซ้ำได้"

🎬 **▶️ Exercise — สร้าง scenario:** เรียก skill `create-scenario`
🗣️ "สังเกตนะครับ มันไปอ่าน user-flow.md เอง เจอ logic path LP-1 ถึง LP-6 แล้วสร้าง scenario file พร้อม AC แบบ Given/When/Then"

🎬 เปิดไฟล์ scenario ที่เพิ่งสร้าง ชี้ให้ดูว่า:
- ไม่มี implementation detail (เคารพ instruction จาก Session 2!)
- AC อ้างอิง COND กลับไปที่ user-story

🗣️ "เห็นพลังของมันไหมครับ Skill ทำงานตาม step แต่ก็ยังเคารพ instruction ที่เราตั้งไว้ สองอย่างทำงานร่วมกัน"

⚠️ scenario ไม่ได้เตรียมไว้ล่วงหน้า — ถ้าใครเห็นไฟล์ scenario อยู่แล้วแปลว่าทำ exercise ซ้ำ ให้ลบก่อน
🗣️ "ตอนนี้เรามี scenario พร้อม AC แล้ว — เดี๋ยว session หน้าเราจะเอา AC พวกนี้ไปสร้าง test case"

---

## Session 4 — Custom Prompts: สร้าง & ตรวจ TC (30 นาที)

🗣️ "Prompt คือ 'template คำสั่งสำเร็จรูป' พิมพ์ `/` เรียก ทำงานครั้งเดียวจบ เหมาะกับงานที่ทำบ่อย ๆ (เดี๋ยว Session หน้าจะเทียบให้ชัดว่าต่างจาก skill ยังไง)"

🎬 **▶️ Exercise 2 — `/create-tc`:**
1. พิมพ์ `/create-tc` ใน chat
2. ใส่ scenario ID เช่น `01`
🗣️ "มันอ่าน scenario นั้น แล้วสร้าง TC ทุก AC แล้ว **append** ต่อท้าย business-tc.md ไม่ลบของเดิม"

🎬 เปิด [business-tc.md](../workshop-demo/business-tc.md) ชี้ TC ใหม่
🗣️ "ดู format นะครับ — TC-ID, AC-Ref, Label เป็น Happy/Negative/Edge เป๊ะตาม instruction เพราะ prompt มันสั่งให้ทำตาม business-tc.instructions.md"

🎬 **▶️ Exercise 3 — `/review-coverage`:**
🗣️ "ทีนี้เราอยากรู้ว่า test ครบทุก path ยัง — พิมพ์ `/review-coverage`"
🎬 ดู output checklist ✅/❌ + % coverage
🗣️ "มัน map logic path กับ TC ให้ แล้วบอกเลยว่าขาด path ไหน คิด % ให้ด้วย — นี่คือพลังของการมีเอกสารที่ Copilot อ่านต่อกันได้"

❓ "ใครพอบอกได้ว่า Prompt กับ Skill ต่างกันยังไง?"
🗣️ (เฉลย) "ทั้งคู่เรียกด้วย `/` ได้เหมือนกันนะครับ — จุดต่างจริง ๆ คือ **prompt** เป็น template สั่งครั้งเดียว เรียก manual อย่างเดียว ส่วน **skill** เป็น workflow หลายขั้น **bundle ไฟล์ประกอบได้** และ **Agent หยิบไปใช้เองอัตโนมัติ**จาก description ได้ด้วย"
⚠️ อย่าบอกว่า "prompt เรียกด้วย slash, skill เรียกในโหมด Agent" — ผิด! ใน Copilot skill ก็โผล่ในเมนู `/` เหมือนกัน

---

## Session 5 — MCP + Agents: ต่อกับ GitHub (30 นาที)

🗣️ "สี่อย่างที่ผ่านมาอยู่ในไฟล์ของเราเอง MCP คือการต่อ Copilot ออกไปหา 'เครื่องมือภายนอก' วันนี้เราต่อกับ GitHub"

🎬 เปิด [.mcp.json](../.mcp.json) อธิบาย server `github` (Remote + OAuth)
🗣️ "สังเกตว่าไม่มี key ในไฟล์เลย — ตัวนี้เป็น remote server ของ GitHub เอง พอ Agent เรียกครั้งแรก VS Code จะเด้งให้เรา authorize ด้วย GitHub account ที่ sign in อยู่ ปลอดภัยกว่าและไม่ต้องไปจัดการ token เอง"

🗣️ "ทีนี้เราจะใช้ **โหมด Agent** — ต่างจาก chat ปกติตรงที่ Agent วางแผนเองและเรียก tool หลายครั้งต่อเนื่องได้"

🎬 **▶️ Exercise 4:** สลับเป็นโหมด Agent แล้วสั่ง:
> "อ่าน business-tc.md แล้วสร้าง GitHub Issue หนึ่งอันต่อหนึ่ง TC ใน repo `TGA88/copilot-workshop-issues-demo`"
🎬 ให้ดู Copilot เรียก MCP tool สร้าง issue บน repo จริง
🗣️ (ถ้าจัด hands-on) "ใครจะลองเองให้เปลี่ยนชื่อ repo เป็นของตัวเองนะครับ ไม่งั้น issue จะไปกองรวมกันที่ repo ผม"

🗣️ "เห็นไหมครับ มันอ่านไฟล์ของเรา แล้วเอาไปสร้าง issue บน GitHub จริง ๆ นี่คือ MCP + Agent ทำงานร่วมกัน — ข้อมูลจาก workflow ของเราไหลออกไปสู่เครื่องมือที่ทีมใช้จริง"

🗣️ (Bonus ถ้าเหลือเวลา) "สั่งต่อให้มันจัด issue เข้า GitHub Projects board เป็นคอลัมน์ตาม Label ก็ได้ — เหมือนเทบอร์ดงานให้อัตโนมัติ"

⚠️ เตรียม repo เป้าหมายเปล่า ๆ ไว้ก่อน + ทดสอบ run เองมาแล้ว เพราะ MCP พังง่ายสุด (authorize ไม่ผ่าน / ระบุ repo ผิด / network)
⚠️ ครั้งแรกต้องกด authorize OAuth ก่อน — เผื่อเวลาตรงนี้ อย่าให้ผู้เรียนตกใจ popup
⚠️ ถ้า MCP ใช้ไม่ได้สด ๆ ให้มี screenshot/วิดีโอสำรองไว้ฉาย

---

## Session 6 — Wrap-up & Q&A (15 นาที)

🗣️ "วันนี้เราเดินครบ 5 อย่างแล้ว ลองทบทวนเป็นภาพเดียวกันนะครับ"

🎬 วาด/ฉายภาพสรุป:
- **Instruction** = กฎ (Copilot อ่านเอง)
- **Prompt** = template สั่งครั้งเดียว (เรียก `/` manual เท่านั้น)
- **Skill** = workflow หลายขั้น + bundle ไฟล์ได้ (เรียก `/` ก็ได้ Agent หยิบเองก็ได้)
- **MCP** = เครื่องมือภายนอก
- **Agent** = ตัวขับที่ร้อยทุกอย่างเข้าด้วยกัน

🗣️ "ที่สำคัญที่สุด — ทั้งหมดนี้ทำงานได้เพราะเอกสารเราเป็น text ที่ต่อกันเป็น pipeline ลองเอาแนวคิดนี้ไปปรับใช้กับ repo จริงของทีมดูนะครับ เริ่มจาก copilot-instructions.md ไฟล์เดียวก่อนก็ได้"

❓ เปิด Q&A
🎬 แจก/ชี้ checklist debug ท้าย [README.md](../workshop-demo/README.md) ให้เอาไปใช้ต่อ

🗣️ "ขอบคุณทุกคนครับ 🎉"

---

## 💡 Tips การควบคุมจังหวะ (สำหรับผู้สอน)

- ถ้าเวลาเหลือ: ให้ผู้เรียนลองแก้ instruction เองแล้วดูผลเปลี่ยน
- ถ้าเวลาน้อย: ตัด Exercise 3 (`/review-coverage`) ออกได้ เพราะ optional
- ถ้ากลุ่มไม่ technical: เน้น Session 2 + 4 (instruction + prompt) ข้าม MCP เป็น demo ดูอย่างเดียว
- คอยถามย้ำหลังแต่ละ exercise: "ใครติดตรงไหนยกมือ" ก่อนไปต่อ
