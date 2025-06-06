# ChatAI WhatsApp Bot

Bot WhatsApp berbasis GPT‑4 yang menggunakan Twilio + Flask, siap di‑deploy di Railway.

## Cara Deploy

1. Fork repo ini ke GitHub kamu.
2. Masuk ke [Railway](https://railway.app), klik *New Project* ➝ *Deploy from GitHub* ➝ pilih repo ini.
3. Tambahkan variable env di Railway:
   - `OPENAI_API_KEY` = API key dari OpenAI
4. Setelah deploy sukses, dapatkan URL (misal `https://chatai-xxx.up.railway.app/whatsapp`)
5. Masuk ke Twilio Console ➝ WhatsApp Sandbox ➝ isi webhook URL di `When a message comes in`
6. Kirim pesan ke nomor WhatsApp sandbox, nanti ChatAI akan balas!

___

## Pengaturan tambahan

- Ganti prompt system di `app.py` untuk gaya chat yang berbeda
- Tambahkan logging, database, atau validasi sesuai kebutuhan
