# 📘 Praveen Trading (Client) - Instagram AI Setup Guide

Aapke naye client **Praveen Trading** aur unke Instagram account **@praveentradingcompany** ko AI Bot se connect karne ke liye niche diye gaye steps ko ek-ek karke complete karein.

---

## 🛠️ Step 1: Instagram App Settings (Mobile Phone Par)
*Sabse pehle client ke mobile phone par Instagram app mein message access permissions enable karni hogi.*

1. Mobile par **@praveentradingcompany** Instagram Profile open karein.
2. Top-right corner mein **Menu (Three lines)** par click karke **Settings and Privacy** mein jayein.
3. Scroll karke **Messages and Story Replies** -> **Message Controls** par click karein.
4. Niche scroll karke **"Connected Tools"** section mein **"Allow Access to Messages"** ko **ON (Enable)** kar dein.
   > [!IMPORTANT]
   > Agar yeh setting ON nahi hogi, toh AI bot ke paas messages receive nahi honge.

---

## 🔗 Step 2: Facebook Page aur Instagram Account ko Link karna
*Meta Business Suite mein check karein ki Page aur Instagram aapas mein linked hain.*

1. Jo screenshot aapne share kiya hai, wahan left side mein **Accounts** ke andar **Instagram accounts** par click karein.
2. **praveentradingcompany** par click karein aur dekhein ki kya woh **Praveen Trading** (Facebook Page) se connected hai.
3. Agar connected nahi hai, toh wahan "Connect Facebook Page" par click karke use connect karein.

---

## 🔑 Step 3: Permanent Page Access Token Generate Karna
*Temporary tokens expire ho jate hain, isliye hum System User banakar permanent token lenge.*

1. **Meta Business Suite** (Settings) mein left side menu mein **Users** -> **System Users** par jayein.
2. **Add** (Naya User) button par click karein:
   - System User Name: `Insta_AI_System_User`
   - System User Role: **Admin**
3. User create hone ke baad, us user ko select karein aur **Add Assets** par click karein.
4. **Assets Details** window open hogi:
   - **Pages** select karein -> **Praveen Trading** choose karein -> Right side mein **Full Control** (Everything) enable karein.
   - **Instagram Accounts** select karein -> **praveentradingcompany** choose karein -> Right side mein **Full Control** enable karein.
   - **Save Changes** par click karein.
5. Ab usi System User ke samne **Generate New Token** par click karein.
6. Apna Meta App select karein aur niche diye gaye permissions ko **Tick/Check** karein:
   - `instagram_basic`
   - `instagram_manage_messages`
   - `pages_manage_metadata`
   - `pages_messaging`
   - `pages_read_engagement`
7. Niche **Generate Token** par click karein.
8. Ek popup aayega jisme Token hoga. **Ise copy karke kahin safe jagah save kar lein.**
   > [!WARNING]
   > Yeh token sirf ek baar dikhayi deta hai. Agar miss ho gaya toh naya generate karna padega.

---

## 🆔 Step 4: Instagram Business Account ID Hasil Karna
*Humein client ke Instagram ka Unique ID chahiye jo `.env` mein jayega.*

1. [developers.facebook.com](https://developers.facebook.com) par jayein aur apna App open karein.
2. Left menu mein **Messenger** -> **Instagram Settings** par jayein.
3. Wahan apna Instagram Account add karne par aapko **Instagram Business Account ID** (17 digits) dikhegi. Ise copy kar lein.

---

## 📝 Step 5: Environment Variables (.env) Update Karna
*Apne Project folder ke `.env` file (`Insta AI/.env`) ko open karein aur client ke details se update karein.*

```env
# Meta / Instagram Configuration (Praveen Trading Client)
INSTAGRAM_BUSINESS_ACCOUNT_ID=YOUR_NEW_INSTAGRAM_BUSINESS_ACCOUNT_ID
PAGE_ACCESS_TOKEN=YOUR_NEW_PERMANENT_SYSTEM_USER_TOKEN
WEBHOOK_VERIFY_TOKEN=cubemoons_insta_bot
META_APP_SECRET=YOUR_NEW_META_APP_SECRET (App Settings -> Basic se milega)

# OpenAI Configuration
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

---

## 🌐 Step 6: Webhook Configuration & Subscription
*Ab hum Meta App ko humare backend server (ngrok) se connect karenge.*

1. [developers.facebook.com](https://developers.facebook.com) dashboard mein jayein.
2. Left menu se **Webhooks** par click karein.
3. Dropdown mein **Instagram** select karein.
4. **Edit Subscription** par click karein:
   - **Callback URL**: `https://morale-pebble-embellish.ngrok-free.dev/api/v1/webhook`
   - **Verify Token**: `cubemoons_insta_bot`
5. **Verify and Save** par click karein.
6. Save hone ke baad, webhook fields ki list mein niche scroll karein aur in do fields ko **Subscribe** zaroori karein:
   - `messages`
   - `messaging_postbacks`

---

## 🚀 Step 7: Bot Ko Run Aur Test Karna

1. **Backend Server** start karein:
   ```bash
   python -m uvicorn app.main:app --reload
   ```
2. **Ngrok Tunnel** run karein:
   ```bash
   ngrok http --domain=morale-pebble-embellish.ngrok-free.dev 8000
   ```
3. Apne kisi dusre personal account se client ke Instagram `@praveentradingcompany` par DM send karke test karein. Aapko aapke terminal mein logs dikhne lagenge aur AI turant reply dega!

---
*Built with ❤️ for Cubemoons*
