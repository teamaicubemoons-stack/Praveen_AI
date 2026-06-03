#!/usr/bin/env bash
# ==============================================================================
# Praveen Trading Company AI Bot - AWS EC2 Automated Setup Script
# ==============================================================================
# This script automates the production deployment on your Ubuntu EC2 instance.
# Running this will configure: System packages, Virtual Environments,
# Systemd background services, Nginx reverse proxy, and firewall rules.
# ==============================================================================

set -e

DOMAIN="praveen-trading.duckdns.org"
PROJECT_ROOT="/home/ubuntu/Praveen_AI"

echo "=================================================================="
echo "🚀 Starting Automated Setup for Praveen Trading AI Bot"
echo "=================================================================="

# 1. Update and install system dependencies
echo "📦 Installing system packages (Python, Git, Nginx, Certbot)..."
sudo apt update -y
sudo apt install -y python3-pip python3-venv git nginx certbot python3-certbot-nginx

# 2. Setup firewall
echo "🔒 Configuring UFW Firewall..."
sudo ufw allow OpenSSH
sudo ufw allow 'Nginx Full'
echo "y" | sudo ufw enable

# 3. Setup Instagram Bot Virtual Environment
echo "🐍 Setting up Instagram Bot Python Virtual Env..."
cd "$PROJECT_ROOT/Insta AI"
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt

# 4. Setup Facebook Messenger Bot Virtual Environment
echo "🐍 Setting up Facebook Messenger Bot Python Virtual Env..."
cd "$PROJECT_ROOT/FB_Messenger AI"
if [ ! -d ".venv" ]; then
    python3 -m venv .venv
fi
./.venv/bin/pip install --upgrade pip
./.venv/bin/pip install -r requirements.txt

# 5. Create Systemd Service for Instagram Bot
echo "⚙️ Configuring background service for Instagram Bot..."
sudo tee /etc/systemd/system/insta_bot.service > /dev/null <<EOF
[Unit]
Description=Instagram AI Bot FastAPI service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=$PROJECT_ROOT/Insta AI
ExecStart="$PROJECT_ROOT/Insta AI/.venv/bin/uvicorn" app.main:app --port 8000 --host 127.0.0.1
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# 6. Create Systemd Service for Facebook Messenger Bot
echo "⚙️ Configuring background service for Facebook Messenger Bot..."
sudo tee /etc/systemd/system/fb_bot.service > /dev/null <<EOF
[Unit]
Description=Facebook Messenger AI Bot FastAPI service
After=network.target

[Service]
User=ubuntu
WorkingDirectory=$PROJECT_ROOT/FB_Messenger AI
ExecStart="$PROJECT_ROOT/FB_Messenger AI/.venv/bin/uvicorn" app.main:app --port 8001 --host 127.0.0.1
Restart=always

[Install]
WantedBy=multi-user.target
EOF

# 7. Start and Enable Services
echo "🔄 Starting background services..."
sudo systemctl daemon-reload
sudo systemctl restart insta_bot
sudo systemctl enable insta_bot
sudo systemctl restart fb_bot
sudo systemctl enable fb_bot

# 8. Configure Nginx Reverse Proxy
echo "🌐 Configuring Nginx Reverse Proxy for $DOMAIN..."
sudo tee /etc/nginx/sites-available/praveen_bots > /dev/null <<EOF
server {
    listen 80;
    server_name $DOMAIN;

    # Route for Instagram Bot (Strips /instagram/ prefix)
    location /instagram/ {
        proxy_pass http://127.0.0.1:8000/;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }

    # Route for FB Messenger Bot (Strips /messenger/ prefix)
    location /messenger/ {
        proxy_pass http://127.0.0.1:8001/;
        proxy_set_header Host \$host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
    }
}
EOF

# Enable Nginx config and remove default
if [ -f /etc/nginx/sites-enabled/default ]; then
    sudo rm /etc/nginx/sites-enabled/default
fi

if [ ! -f /etc/nginx/sites-enabled/praveen_bots ]; then
    sudo ln -s /etc/nginx/sites-available/praveen_bots /etc/nginx/sites-enabled/
fi

sudo nginx -t
sudo systemctl restart nginx

echo "=================================================================="
echo "✅ Setup Completed Successfully!"
echo "📡 Bots are running locally on ports 8000 and 8001."
echo "🌍 Nginx is serving http://$DOMAIN"
echo "=================================================================="
echo "💡 NEXT STEP: To set up HTTPS (SSL), run the following command:"
echo "   sudo certbot --nginx -d $DOMAIN"
echo "=================================================================="
