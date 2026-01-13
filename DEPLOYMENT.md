# ADA Mock API - Cloud Deployment Guide

Deploy the mock API server to the cloud for 24/7 availability without needing your Mac running.

---

## 🚀 Quick Deploy Options

### Option 1: Render.com (Recommended - Easiest)

**Pros:** Free tier, auto-deploys from GitHub, HTTPS included, no credit card needed
**Time:** 5 minutes

#### Steps:

1. **Sign up:** https://render.com/

2. **Create New Web Service:**
   - Click "New +" → "Web Service"
   - Connect your GitHub account
   - Select repository: `ghifiardi/ada-mobile-ui`
   - Click "Connect"

3. **Configure:**
   - Name: `ada-mock-api`
   - Region: Oregon (or nearest)
   - Branch: `main`
   - Build Command: (leave blank - uses Dockerfile)
   - Start Command: (leave blank - uses Dockerfile)
   - Plan: **Free**

4. **Deploy:**
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment

5. **Get Your URL:**
   - Copy the URL (e.g., `https://ada-mock-api.onrender.com`)
   - Update your mobile UI with this URL
   - Share with colleagues!

**Your Permanent URLs:**
- **API:** `https://ada-mock-api.onrender.com`
- **Mobile UI:** `https://ghifiardi.github.io/ada-mobile-ui/`

---

### Option 2: Railway.app (Alternative)

**Pros:** Free $5 credit monthly, fast deploys, easy to use
**Time:** 5 minutes

#### Steps:

1. **Sign up:** https://railway.app/

2. **Deploy:**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose `ghifiardi/ada-mobile-ui`
   - Railway auto-detects Dockerfile

3. **Get URL:**
   - Click "Settings" → "Generate Domain"
   - Copy your URL (e.g., `https://ada-mock-api.up.railway.app`)

---

### Option 3: Fly.io (Advanced)

**Pros:** Free tier, global edge network, fast
**Time:** 10 minutes

#### Steps:

```bash
# Install flyctl
brew install flyctl

# Login
flyctl auth login

# Navigate to your repo
cd ~/CascadeProjects/Investment\ 2025/Banking\ Deep\ Fake\ and\ Voice\ Cloning/huggingface-deploy/ada-media-integrity/ada-mobile-ui

# Initialize and deploy
flyctl launch --name ada-mock-api
flyctl deploy
```

Your URL: `https://ada-mock-api.fly.dev`

---

### Option 4: Heroku (Classic)

**Pros:** Well-known, reliable
**Cons:** Requires credit card (won't charge on free tier)
**Time:** 10 minutes

#### Steps:

```bash
# Install Heroku CLI
brew install heroku/brew/heroku

# Login
heroku login

# Create app
cd ~/CascadeProjects/Investment\ 2025/Banking\ Deep\ Fake\ and\ Voice\ Cloning/huggingface-deploy/ada-media-integrity/ada-mobile-ui
heroku create ada-mock-api

# Deploy
git push heroku main
```

Your URL: `https://ada-mock-api.herokuapp.com`

---

## 🔧 After Deployment

### Update Mobile UI Default URL

Edit `index.html` line 459:

```html
<!-- Change from: -->
value="http://localhost:8000"

<!-- To your cloud URL: -->
value="https://ada-mock-api.onrender.com"
```

Commit and push:

```bash
git add index.html
git commit -m "Update default API URL to cloud deployment"
git push origin main
```

Now GitHub Pages will use your cloud API by default!

---

## 📱 Share with Colleagues

After deployment, share:

**Mobile UI:**
```
https://ghifiardi.github.io/ada-mobile-ui/
```

**API URL:**
```
https://ada-mock-api.onrender.com
```
(or your chosen platform's URL)

They don't need to enter anything - it just works! ✨

---

## ⚙️ Environment Variables (Optional)

If you want to customize the mock server:

**Render.com / Railway:**
- Go to Settings → Environment Variables
- Add: `PORT=8000`

---

## 🔍 Monitoring

### Check if API is running:

```bash
# Test health endpoint
curl https://ada-mock-api.onrender.com/health

# Should return:
# {"status":"healthy","service":"ADA Media Integrity Mock API","version":"2.0"}
```

### View API Documentation:

```
https://ada-mock-api.onrender.com/docs
```

---

## 💰 Cost Comparison

| Platform | Free Tier | Limitations | Best For |
|----------|-----------|-------------|----------|
| **Render** | ✅ Free forever | Sleeps after 15min inactivity, restarts on request | Testing, demos |
| **Railway** | ✅ $5/month credit | ~100 hours/month | Light production |
| **Fly.io** | ✅ Free tier | 3 shared VMs | Global deployments |
| **Heroku** | ✅ Free tier (credit card) | Sleeps after 30min | Classic choice |

**Recommendation:** Start with **Render.com** - no credit card, permanently free, auto-deploys.

---

## 🔄 Auto-Deploy from GitHub

All platforms support auto-deployment:
- Push to `main` branch
- Platform automatically rebuilds and deploys
- New version live in 2-3 minutes

---

## 🆘 Troubleshooting

### API not responding?
```bash
# Check logs on Render
# Go to Dashboard → ada-mock-api → Logs

# Or test locally first:
docker build -t ada-mock-api .
docker run -p 8000:8000 ada-mock-api
curl http://localhost:8000/health
```

### Mobile UI can't connect?
1. Verify API URL is HTTPS (not HTTP)
2. Check API is actually running: `curl YOUR_API_URL/health`
3. Clear browser cache and refresh

---

## 🎉 Result

After deployment:
- ✅ API runs 24/7 in the cloud
- ✅ No need for your Mac to be running
- ✅ No need for ngrok
- ✅ Permanent HTTPS URL
- ✅ Auto-restarts if it crashes
- ✅ Works from anywhere in the world

Your colleagues can test anytime without you doing anything!
