# Insta AI - Instagram Automation Backend

This project is a robust, AI-powered backend for Instagram DM automation using Python FastAPI and OpenAI.

## Features
- **Official Meta API**: Uses the official Instagram Graph API.
- **AI-Powered**: Intent classification and response generation using OpenAI GPT-4o.
- **FastAPI**: High-performance, asynchronous backend.
- **Robust Architecture**: Organized service-based structure.

## Setup Instructions

1. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Configure Environment**:
   Edit the `.env` file and add your credentials:
   - `OPENAI_API_KEY`
   - `INSTAGRAM_BUSINESS_ACCOUNT_ID`
   - `PAGE_ACCESS_TOKEN`
   - `WEBHOOK_VERIFY_TOKEN`

3. **Run the Server**:
   ```bash
   python -m app.main
   ```

4. **Expose Webhook**:
   Use a tool like `ngrok` to expose your local server (port 8000) to the internet and set the URL in the Meta Developer Dashboard.
   URL: `https://your-ngrok-url/api/v1/webhook`

## Workflow
1. User sends a DM on Instagram.
2. Meta triggers the Webhook.
3. Backend processes the message text with OpenAI.
4. AI determines the intent and generates a response.
5. Backend sends the response back via Meta API.
