# 🚀 Cubemoons Insta AI - Execution Guide

Follow these steps to start your Instagram AI bot every time you start your system.

## 1. Start the Backend Server (Terminal 1)

Open a terminal in the `Insta AI` folder and run:

```bash
python -m uvicorn app.main:app --reload
```

## 2. Start the Ngrok Tunnel (Terminal 2)

Open a second terminal and run your static domain tunnel:

```bash
ngrok http --domain=morale-pebble-embellish.ngrok-free.dev 8000
```

---

## 🔗 Webhook Configuration (Static)

You do **NOT** need to change the Callback URL in the Meta Developer Portal anymore. Your permanent URL is:

**Callback URL:**
`https://morale-pebble-embellish.ngrok-free.dev/api/v1/webhook`

**Verify Token:**
`cubemoons_insta_bot`

---

## 🛠️ Maintenance Tips

- **Hinglish/English Prompt:** To update how the AI talks, edit `app/services/openai_service.py`.
- **Environment Variables:** All keys are stored in the `.env` file (do not share this file).
- **Logs:** Check the Uvicorn terminal (Terminal 1) to see real-time AI processing logs.

---

*Built with ❤️ for Cubemoons*
