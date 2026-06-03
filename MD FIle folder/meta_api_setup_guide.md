# Meta Developer Portal: Step-by-Step Setup Guide

This guide is designed for **non-technical users** to help them obtain the necessary API credentials (IDs and Tokens) for Instagram, Facebook Messenger, and WhatsApp automation.

---

## **Prerequisites (Pehle Yeh Taiyar Rakhein)**
Before starting, ensure you have:
1.  A **Personal Facebook Account**.
2.  A **Facebook Business Page**.
3.  (For Instagram) An **Instagram Business/Creator Account** linked to your Facebook Page.
4.  (For WhatsApp) A **Phone Number** that is NOT currently used for a regular WhatsApp app.

---

## **Phase 1: Meta Developer Account Register Karein**
1.  Go to [developers.facebook.com](https://developers.facebook.com).
2.  Top right mein **"Get Started"** ya **"Log In"** par click karein.
3.  Apne Facebook account se login karein.
4.  Register karne ke liye prompts follow karein (Role mein "Developer" ya "Business Owner" select karein).

---

## **Phase 2: Naya App Create Karein**
1.  Dashboard mein **"My Apps"** par click karein.
2.  **"Create App"** button par click karein.
3.  **"Other"** select karein aur Next karein.
4.  App Type mein **"Business"** select karein (Yeh zaroori hai Instagram/WhatsApp ke liye).
5.  App ka naam rakhein (e.g., `My AI Automation`) aur apni email daalein.
6.  **"Create App"** par click karein.

---

## **Phase 3: Instagram & Messenger Setup**
1.  App Dashboard mein niche scroll karein aur **"Messenger"** product ke **"Set Up"** par click karein.
2.  Left menu mein **"Messenger" -> "Settings"** mein jayein.
3.  **"App Settings"** section mein apni Facebook Page add karein.
4.  **Generate Token**: Page ke samne "Generate Token" par click karein. Is token ko copy karke apne `.env` file mein `PAGE_ACCESS_TOKEN` mein daalein.
5.  **Instagram Settings**: Niche **"Instagram Settings"** section mein jayein aur apna Instagram account link karein. Wahan aapko `INSTAGRAM_BUSINESS_ACCOUNT_ID` milega.

---

## **Phase 4: WhatsApp Setup**
1.  App Dashboard (Left Menu) mein niche **"Add Product"** ya direct **"WhatsApp"** par click karke **"Set Up"** karein.
2.  **"API Setup"** par click karein.
3.  Yahan aapko:
    *   **Phone Number ID**: Ise copy karein (`WHATSAPP_PHONE_NUMBER_ID`).
    *   **WhatsApp Business Account ID**: Ise bhi copy karein.
    *   **Temporary Access Token**: Shuruat mein ise use karein, lekin yeh 24 ghante mein expire ho jayega. (Permanent token ke liye niche dekhein).

---

## **Phase 5: Webhook Configuration (Backend Connection)**
1.  Left menu mein **"Webhooks"** par click karein.
2.  Dropdown mein **"Instagram"** (ya "Permissions") select karein.
3.  **Callback URL**: Apna ngrok URL daalein (e.g., `https://xyz.ngrok.app/api/v1/webhook`).
4.  **Verify Token**: Jo aapne `.env` mein rakha hai (e.g., `insta_ai_verify_token`).
5.  **Verify and Save** par click karein.
6.  Save hone ke baad, **"messages"** aur **"messaging_postbacks"** ko **Subscribe** zaroori karein.

---

## **Phase 6: Permanent Token Kaise Le? (Very Important)**
Temporary tokens expire ho jate hain. Permanent token ke liye:
1.  [Meta Business Suite](https://business.facebook.com/settings/system-users) mein jayein.
2.  **System Users** mein ek naya user add karein (Role: Admin).
3.  Us user par click karke **"Add Assets"** karein aur apni Page select karke "Full Control" dein.
4.  Ab **"Generate New Token"** par click karein.
5.  Permissions mein `whatsapp_business_messaging`, `pages_messaging`, `instagram_manage_messages` select karein.
6.  Jo token milega, woh **Permanent** hoga aur kabhi expire nahi hoga.

---

## **Phase 7: Checklist for .env File**
In steps ke baad aapke paas yeh sab hona chahiye:
*   [ ] `PAGE_ACCESS_TOKEN` (Messenger/Insta ke liye)
*   [ ] `INSTAGRAM_BUSINESS_ACCOUNT_ID`
*   [ ] `WHATSAPP_PHONE_NUMBER_ID`
*   [ ] `WHATSAPP_ACCESS_TOKEN`
*   [ ] `WEBHOOK_VERIFY_TOKEN` (Aapka banaya hua code)
*   [ ] `OPENAI_API_KEY` (OpenAI Dashboard se)

---
**Tip**: Agar kisi step mein problem aaye, to step ka screenshot le kar mujhse puchein!
