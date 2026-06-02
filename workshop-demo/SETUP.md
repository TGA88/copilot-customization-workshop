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

## 4. ตั้งค่า Trello MCP Key

1. ไปที่ https://trello.com/app-key → copy **API Key**
2. กด **"Generate a Token"** → copy **Token**
3. copy ไฟล์ตัวอย่างเป็น `.env` แล้วใส่ค่าจริง:
   ```bash
   cp .env.example .env
   ```
4. แก้ `.env`:
   ```
   TRELLO_API_KEY=<API Key ของคุณ>
   TRELLO_TOKEN=<Token ของคุณ>
   ```

> `.env` ถูก ignore ใน git อยู่แล้ว — ปลอดภัย ไม่หลุดขึ้น repo

---

## 5. Verify ว่าพร้อม

- [ ] เปิด Copilot Chat ได้ (`Cmd/Ctrl+Alt+I` หรือไอคอน chat)
- [ ] เปิดไฟล์ `scenario-*.md` ใด ๆ → ดู panel **References** เห็น `scenario.instructions.md` โหลดเข้ามา
- [ ] พิมพ์ `/` ใน Chat แล้วเห็น prompt `create-tc` และ `review-coverage`
- [ ] โหมด Agent มองเห็น MCP server `trello` (ตรวจที่ MCP / tools list)

ถ้าครบทุกข้อ = พร้อมเรียน 🎉 (ถ้าติดข้อไหน ดู Tips ใน README.md)
