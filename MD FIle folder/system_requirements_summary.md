# AI Automation Systems - Unified Requirements Guide

This document summarizes the technical requirements, API credentials, and setup needs for all three automation systems (Instagram, Facebook Messenger, and WhatsApp).

---

## 1. Instagram Automation System (`Insta AI`)
To automate Instagram Direct Messages (DMs), you need an Instagram Professional account linked to a Facebook Page.

### **API & Meta Credentials:**
*   **Instagram Business Account ID**: Found in the Meta Developer Portal under "Instagram Settings".
*   **Page Access Token**: Generated for the Facebook Page linked to the Instagram account.
*   **Meta App Secret**: Found in your App's basic settings on Meta Dashboard.
*   **Webhook Verify Token**: A custom string you create (e.g., `insta_ai_verify_token`).
*   **Required Permissions**:
    *   `instagram_basic`
    *   `instagram_manage_messages`
    *   `pages_manage_metadata`
    *   `pages_show_list`

---

## 2. Facebook Messenger Automation System (`Messenger AI`)
To automate Facebook Page messages, you need a Meta Business App with the Messenger product enabled.

### **API & Meta Credentials:**
*   **Facebook Page ID**: The ID of your business page.
*   **Page Access Token**: Generated for the specific page.
*   **Meta App Secret**: Used for signature verification.
*   **Webhook Verify Token**: A custom string (e.g., `messenger_ai_verify_token`).
*   **Required Permissions**:
    *   `pages_messaging`
    *   `pages_manage_metadata`
    *   `pages_show_list`

---

## 3. WhatsApp Automation System (`WhatsApp AI`)
To automate WhatsApp messages, you must use the official WhatsApp Cloud API (Meta).

### **API & Meta Credentials:**
*   **WhatsApp Phone Number ID**: Found in the WhatsApp "Getting Started" section in Meta Dashboard.
*   **WhatsApp Business Account ID**: Found in the same dashboard.
*   **WhatsApp Access Token**: A permanent token is recommended for production.
*   **Webhook Verify Token**: A custom string (e.g., `whatsapp_ai_verify_token`).
*   **Required Setup**:
    *   Register a phone number in the Meta Developer Portal.
    *   Add a Payment Method to the Meta Business account (even for free tier).

---

## 4. Common Technical Requirements (For All Systems)

### **OpenAI Configuration:**
*   **OpenAI API Key**: Required for intent detection and response generation.
*   **Model Selection**: `gpt-4o` or `gpt-3.5-turbo` (recommended for cost-efficiency).

### **Infrastructure:**
*   **Python 3.10+**: Core programming language.
*   **FastAPI**: Web framework for high-performance handling of webhooks.
*   **HTTPS Server / Tunnel**: Meta webhooks **must** be sent to a secure `https://` URL.
    *   *Development*: Use `ngrok` or `zrok`.
    *   *Production*: Use VPS (AWS/DigitalOcean) with SSL (Let's Encrypt).

### **Environment Variables Summary:**
Each system requires a `.env` file with these keys (as structured in your project folders):
| System | Key Variables |
| :--- | :--- |
| **Instagram** | `INSTAGRAM_BUSINESS_ACCOUNT_ID`, `PAGE_ACCESS_TOKEN` |
| **Facebook** | `PAGE_ID`, `PAGE_ACCESS_TOKEN` |
| **WhatsApp** | `WHATSAPP_PHONE_NUMBER_ID`, `WHATSAPP_ACCESS_TOKEN` |
| **All** | `OPENAI_API_KEY`, `WEBHOOK_VERIFY_TOKEN` |

---

## 5. Webhook Endpoints
When setting up the Meta Webhook, use the following paths based on your deployment:
*   **Instagram**: `https://your-domain.com/api/v1/webhook` (Port 8000)
*   **Messenger**: `https://your-domain.com/api/v1/webhook` (Port 8001)
*   **WhatsApp**: `https://your-domain.com/api/v1/webhook` (Port 8002)
