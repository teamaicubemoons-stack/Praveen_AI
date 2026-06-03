# Messenger AI - Facebook Messenger Automation

AI-powered backend for Facebook Page Messenger automation.

## Setup
1. `pip install -r requirements.txt`
2. Fill `.env` with Meta Page credentials and OpenAI API Key.
3. Run: `python -m app.main`
4. Use `ngrok` for webhook exposure.
   Webhook URL: `https://your-url/api/v1/webhook`
   Verify Token: `messenger_ai_verify_token` (default)
