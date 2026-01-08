# Web UI Deployment Guide
## Share Your Mobile Link via GitHub Pages or Hugging Face

This is a standalone HTML file that anyone can access from their phone's browser!

---

## 🎯 What This Is

A **single HTML file** (`index.html`) that provides a mobile-friendly web interface for your ADA Media Integrity system.

**Features:**
- ✅ Works on any phone (iOS/Android)
- ✅ No installation needed
- ✅ Just open the link in browser
- ✅ Beautiful mobile UI
- ✅ Connects to your API server

---

## 🚀 Deployment Options

### **Option 1: GitHub Pages (Recommended)**

#### Step 1: Create GitHub Repository

```bash
# Navigate to web-deploy folder
cd web-deploy

# Initialize git
git init
git add index.html README.md
git commit -m "Add ADA mobile web UI"

# Create repo on GitHub (or use existing)
# Then push
git remote add origin https://github.com/YOUR-USERNAME/ada-mobile-ui.git
git branch -M main
git push -u origin main
```

#### Step 2: Enable GitHub Pages

1. Go to your repository on GitHub
2. Click **Settings**
3. Scroll to **Pages** (left sidebar)
4. Under **Source**, select **main** branch
5. Click **Save**

#### Step 3: Get Your Link

Your link will be:
```
https://YOUR-USERNAME.github.io/ada-mobile-ui/
```

**Share this link with anyone!** 🎉

---

### **Option 2: Hugging Face Spaces**

#### Step 1: Create Space

1. Go to https://huggingface.co/spaces
2. Click **Create new Space**
3. Name: `ada-mobile-ui`
4. License: Apache 2.0
5. Select: **Static** (HTML/CSS/JS)

#### Step 2: Upload Files

```bash
# Clone your space
git clone https://huggingface.co/spaces/YOUR-USERNAME/ada-mobile-ui
cd ada-mobile-ui

# Copy files
cp ../web-deploy/index.html .
cp ../web-deploy/README.md .

# Commit and push
git add .
git commit -m "Add ADA mobile UI"
git push
```

#### Step 3: Get Your Link

Your link will be:
```
https://huggingface.co/spaces/YOUR-USERNAME/ada-mobile-ui
```

**Share this link with anyone!** 🎉

---

### **Option 3: Netlify (Alternative)**

#### Quick Deploy

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Deploy
cd web-deploy
netlify deploy --prod
```

Follow prompts and get your link!

---

## 📱 How Users Access It

### **Step 1: You Share Link**
```
https://your-username.github.io/ada-mobile-ui/
```

### **Step 2: They Open on Phone**
- Open link in Safari (iOS) or Chrome (Android)
- No app installation needed!

### **Step 3: They Enter Server URL**
They need to enter YOUR server URL:
```
http://YOUR-IP:8000
or
https://your-ngrok-url.ngrok.io
```

### **Step 4: They Upload & Test**
- Upload video from phone
- Select mode
- Get results!

---

## 🔧 Configuration

### **Default Server URL**

Edit `index.html` line 117:
```javascript
value="http://localhost:8000"  // Change to your default server
```

Change to:
```javascript
value="https://your-server.com"  // Your permanent server URL
```

### **Custom Branding**

Edit these lines in `index.html`:

```html
<!-- Title -->
<h1>🛡️ ADA Media Integrity</h1>

<!-- Subtitle -->
<p class="subtitle">AI-Powered Deepfake & Liveness Detection</p>

<!-- Footer -->
<p>Powered by ADA Media Integrity v2.0</p>
```

---

## 🌐 Setup Complete Flow

### **Your Setup (One Time)**

```bash
# 1. Deploy web UI to GitHub Pages
cd web-deploy
git init
git add .
git commit -m "Deploy"
git push

# 2. Enable GitHub Pages in settings

# 3. Start your API server
cd ..
./setup-mobile-access.sh
```

### **User Experience (Every Time)**

1. Open: `https://your-username.github.io/ada-mobile-ui/`
2. Enter server URL you provided
3. Upload video
4. Get results!

---

## 📊 Architecture

```
┌─────────────────────────────────────────┐
│         USER'S PHONE (Browser)          │
│                                         │
│  https://your-username.github.io/       │
│  ada-mobile-ui/                         │
│                                         │
│  [Web UI - index.html]                  │
└──────────────┬──────────────────────────┘
               │
               │ HTTPS Request
               │
               ▼
┌─────────────────────────────────────────┐
│      YOUR API SERVER                    │
│                                         │
│  http://your-ip:8000                    │
│  or                                     │
│  https://your-ngrok-url.ngrok.io        │
│                                         │
│  [ADA Media Integrity API]              │
└─────────────────────────────────────────┘
```

**Key Points:**
- Web UI hosted on GitHub (free)
- API server runs on your computer
- Users access UI from anywhere
- UI connects to your API

---

## 🔒 Security Considerations

### **Option A: Public Web UI + Private Server**

✅ Web UI is public (GitHub Pages)
✅ Server URL is private (you share it)
✅ Only people with server URL can use it

### **Option B: Password Protected**

Add to your API server (in `enhanced_main.py`):

```python
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from secrets import compare_digest

security = HTTPBasic()

@app.post("/analyze/upload/hybrid")
async def analyze_upload_hybrid(
    credentials: HTTPBasicCredentials = Depends(security),
    ...
):
    if not (credentials.username == "user" and credentials.password == "pass123"):
        raise HTTPException(status_code=401, detail="Unauthorized")
    # ... rest of code
```

### **Option C: Rate Limiting**

Already prepared in the API code!

---

## 🎨 Customization

### **Change Colors**

Edit CSS in `index.html`:

```css
/* Main gradient */
background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);

/* Change to your brand colors */
background: linear-gradient(135deg, #YOUR-COLOR-1 0%, #YOUR-COLOR-2 100%);
```

### **Add Logo**

```html
<!-- Add before <h1> tag -->
<img src="your-logo.png" style="width: 100px; display: block; margin: 0 auto 20px;">
<h1>Your Company Name</h1>
```

### **Change Modes**

Edit the mode buttons:

```html
<button class="mode-btn selected" data-mode="quick">
    ⚡ Fast Mode  <!-- Change name -->
    <div class="mode-info">Quick scan (~10 seconds)</div>  <!-- Change description -->
</button>
```

---

## 📱 Testing Your Deployment

### **Step 1: Test Locally**

```bash
# Open in browser
open web-deploy/index.html

# Or use simple server
cd web-deploy
python -m http.server 8080
# Open: http://localhost:8080
```

### **Step 2: Test on Phone**

1. Deploy to GitHub Pages
2. Open link on your phone
3. Enter your server URL
4. Upload a test video
5. Verify results

### **Step 3: Share with Colleague**

1. Send them the GitHub Pages link
2. Send them your server URL (ngrok or IP)
3. They test from their phone
4. Collect feedback

---

## 🚀 Quick Deploy Commands

### **GitHub Pages**

```bash
cd "Banking Deep Fake and Voice Cloning/web-deploy"

# Initialize and deploy
git init
git add .
git commit -m "Deploy ADA mobile UI"
git remote add origin https://github.com/YOUR-USERNAME/ada-mobile-ui.git
git push -u origin main

# Enable Pages in GitHub settings
# Your link: https://YOUR-USERNAME.github.io/ada-mobile-ui/
```

### **Hugging Face**

```bash
# Create space at https://huggingface.co/spaces
# Then:
git clone https://huggingface.co/spaces/YOUR-USERNAME/ada-mobile-ui
cd ada-mobile-ui
cp ../web-deploy/index.html .
git add .
git commit -m "Deploy"
git push

# Your link: https://huggingface.co/spaces/YOUR-USERNAME/ada-mobile-ui
```

---

## ✅ Checklist

### **Before Sharing**

- [ ] Web UI deployed to GitHub Pages/HF
- [ ] API server running
- [ ] Server URL accessible (ngrok or public IP)
- [ ] Tested on your phone
- [ ] Tested upload works
- [ ] Results display correctly
- [ ] Link works from different network

### **When Sharing**

- [ ] Share web UI link
- [ ] Share server URL separately
- [ ] Provide instructions
- [ ] Test with one person first
- [ ] Monitor server logs

---

## 🎉 Result

After deployment, you can share:

**Web UI Link:**
```
https://your-username.github.io/ada-mobile-ui/
```

**Server URL (tell them privately):**
```
https://your-ngrok-url.ngrok.io
```

**Instructions to send:**
```
1. Open: https://your-username.github.io/ada-mobile-ui/
2. Enter server URL: https://your-ngrok-url.ngrok.io
3. Upload a video
4. Select mode and analyze!
```

---

## 📞 Support

**Web UI not loading?**
- Check GitHub Pages is enabled
- Wait 1-2 minutes after deploy
- Clear browser cache

**Can't connect to server?**
- Check server is running
- Verify URL is correct
- Check firewall/network settings

**Upload not working?**
- Check file size (<50MB)
- Check file format (MP4, WAV, etc.)
- Try different browser

---

**🎊 Your users can now test from any phone by just opening a link! 🎊**
