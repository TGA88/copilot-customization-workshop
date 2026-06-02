# SETUP — เตรียมก่อนเริ่ม Workshop

ทำตามขั้นตอนนี้ให้ครบ **ก่อน** workshop เริ่ม เพื่อไม่เสียเวลาตอนสอน

---

## 1. ติดตั้ง VS Code Extension

ติดตั้ง 2 ตัวนี้ (VS Code จะแนะนำให้อัตโนมัติจาก `.vscode/extensions.json`):

- `github.copilot`
- `github.copilot-chat`

> เปิด Extensions panel (`Cmd/Ctrl+Shift+X`) → ค้นหา → Install

---

## 2. Sign in GitHub

- Sign in ด้วย **GitHub account ที่มี Copilot license**
- ตรวจสถานะที่ status bar ด้านล่างขวา ต้องเห็นไอคอน Copilot เป็น active

---

## 3. เปิด Folder นี้ใน VS Code

- เปิด **โฟลเดอร์ root ของ workshop** (โฟลเดอร์ที่มี `.github/` และ `.vscode/`)
- `.vscode/settings.json` จะ apply อัตโนมัติ (เปิด instruction / prompt / skills / MCP / agent)

---

## 4. ตั้งค่า GitHub MCP (Remote + OAuth)

workshop นี้ใช้ **GitHub MCP server แบบ Remote** ตั้งค่าไว้แล้วใน `.mcp.json`
(`https://api.githubcopilot.com/mcp/`) — **ไม่ต้องสร้าง `.env` หรือใส่ key เอง**

1. ตรวจว่า sign in GitHub ใน VS Code แล้ว (จากข้อ 2)
2. ครั้งแรกที่โหมด Agent เรียก GitHub tool → VS Code จะเด้งให้ **"Sign in / Authorize"** → กดอนุญาต
3. เตรียม **repo เป้าหมาย** ไว้ 1 อัน (repo ที่คุณมีสิทธิ์ push) สำหรับให้ Agent สร้าง issue
   - จะ push โฟลเดอร์ workshop นี้ขึ้น GitHub เป็น repo เป้าหมายก็ได้

> ไม่ต้องจัดการ token เอง — OAuth จัดการให้ และ scope จะถูกขอตอน authorize

---

## 5. Verify ว่าพร้อม

- [ ] เปิด Copilot Chat ได้ (`Cmd/Ctrl+Alt+I` หรือไอคอน chat)
- [ ] เปิดไฟล์ `scenario-*.md` ใด ๆ → ดู panel **References** เห็น `scenario.instructions.md` โหลดเข้ามา
- [ ] พิมพ์ `/` ใน Chat แล้วเห็น prompt `create-tc` และ `review-coverage`
- [ ] โหมด Agent มองเห็น MCP server `github` (ตรวจที่ MCP / tools list)

ถ้าครบทุกข้อ = พร้อมเรียน 🎉 (ถ้าติดข้อไหน ดู Tips ใน README.md)
