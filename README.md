# Quran Video Generator - Web Version

🎬 Create beautiful Quranic videos with translations and recitations!

## Features

- 🎯 Generate random Quranic verses
- 📖 Select specific verses
- 🔢 Generate range of verses
- 🌍 Multiple language translations (English, Spanish, French, German, Urdu, Turkish, Indonesian)
- 🎙️ Multiple reciters (Mishary Alafasy, Abdul Basit, Hani Ar-Rifai, and more)
- 📱 Responsive design for all devices
- ⚡ Fast video generation
- 💾 Easy download

## Setup Instructions

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 2. Add Background Videos

Place your background videos (MP4 format) in the `backgrounds/` folder. The generator will randomly select from these backgrounds.

### 3. Run Locally

```bash
python app.py
```

Visit `http://localhost:5000` in your browser.

## Deployment

### Free Hosting Options (See Below)

This app can be deployed to various free hosting platforms. See the deployment guide at the end of this README.

## Project Structure

```
web_deploy/
├── app.py                      # Main Flask application
├── quran_video_generator.py    # Video generation logic
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── static/
│   ├── style.css              # Styling
│   └── script.js              # Frontend logic
├── templates/
│   └── index.html             # Main webpage
├── backgrounds/               # Background videos (add your own)
└── web_output/               # Generated videos output
```

## Usage

1. **Random Verse**: Generate videos with random Quranic verses
2. **Specific Verse**: Choose exact Surah and verse numbers
3. **Range**: Generate multiple videos from a range of verses
4. Select your preferred:
   - Second language for translation
   - Reciter for audio
5. Click "Generate Videos" and wait for processing
6. Download your videos when ready

## Technical Details

- **Backend**: Flask (Python)
- **Video Processing**: FFmpeg
- **Frontend**: Vanilla JavaScript, HTML5, CSS3
- **APIs Used**: Quran.com API for verses and translations

## Requirements

- Python 3.8+
- FFmpeg (must be installed on system)
- Internet connection (for fetching Quran data)

## Credits

Made with ❤️ for the Muslim community
May Allah accept this work

---

# FREE HOSTING OPTIONS

## 🌐 Best Free Hosting Platforms for This App

### 1. **Render.com** ⭐ RECOMMENDED
- **Free Tier**: Yes (with 750 hours/month)
- **Why**: Best for Flask apps, automatic deployments
- **Setup**: 
  1. Sign up at https://render.com
  2. Connect your GitHub repository
  3. Create new "Web Service"
  4. Build command: `pip install -r requirements.txt`
  5. Start command: `gunicorn app:app`
  6. Free tier includes 512MB RAM

### 2. **Railway.app** ⭐ EXCELLENT
- **Free Tier**: $5 credit/month (enough for hobby projects)
- **Why**: Zero config deployment, great for Python apps
- **Setup**:
  1. Sign up at https://railway.app
  2. "New Project" → "Deploy from GitHub"
  3. Select your repository
  4. Railway auto-detects Flask and deploys!

### 3. **PythonAnywhere** 💚 BEGINNER-FRIENDLY
- **Free Tier**: Yes (with limitations)
- **Why**: Designed specifically for Python apps
- **Setup**:
  1. Sign up at https://www.pythonanywhere.com
  2. Upload your files via "Files" tab
  3. Configure Web app with Flask
  4. Free tier: yourname.pythonanywhere.com

### 4. **Fly.io** 🚀 FAST
- **Free Tier**: Yes (good resources)
- **Why**: Fast global deployment
- **Setup**:
  1. Install flyctl CLI
  2. `fly launch` in project directory
  3. Auto-generates config
  4. `fly deploy` to deploy

### 5. **Heroku** (Still Available)
- **Free Tier**: No longer free, but cheap ($5-7/month)
- **Why**: Established platform, easy to use
- **Note**: Changed to paid plans in 2022

---

## 📝 Quick Deployment Guide (Render.com)

### Step 1: Prepare Your Code
1. Make sure all files are in the `web_deploy` folder
2. Ensure `requirements.txt` is present
3. Add backgrounds videos to `backgrounds/` folder

### Step 2: Create GitHub Repository
```bash
cd web_deploy
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin YOUR_GITHUB_URL
git push -u origin main
```

### Step 3: Deploy to Render
1. Go to https://render.com and sign up
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: quran-video-generator
   - **Environment**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Instance Type**: Free
5. Click "Create Web Service"
6. Wait 5-10 minutes for deployment
7. Your app will be live at: `https://quran-video-generator.onrender.com`

### Step 4: Configure Environment Variables (if needed)
- In Render dashboard, go to "Environment"
- Add any needed variables

---

## 🎯 Recommended: Render.com

**Why Render.com is the best for this project:**
- ✅ Free tier with 512MB RAM
- ✅ Automatic SSL (HTTPS)
- ✅ Easy GitHub integration
- ✅ Automatic deployments on push
- ✅ Built-in environment for Python/Flask
- ✅ No credit card required for free tier
- ✅ Good uptime and performance

**Limitations to know:**
- ⚠️ Free services sleep after 15 min of inactivity (takes 30s to wake up)
- ⚠️ 750 hours/month limit (plenty for personal use)
- ⚠️ Limited storage for generated videos

---

## 💡 Pro Tips

1. **For Heavy Usage**: Consider Railway.app (better performance)
2. **For Simplicity**: Use PythonAnywhere (no Git needed)
3. **For Speed**: Use Fly.io (global edge network)
4. **Storage**: Consider using cloud storage (AWS S3, Cloudinary) for generated videos
5. **Background Videos**: Keep them small (<50MB) to fit in free tiers

---

## 🔧 Troubleshooting

### "App not loading"
- Check if service is sleeping (free tier limitation)
- Visit the URL to wake it up

### "Out of memory"
- Reduce video quality settings
- Use smaller background videos
- Consider upgrading to paid tier

### "FFmpeg not found"
- Make sure FFmpeg is installed on the hosting platform
- For Render: Add buildpack or install in build command

---

## 📞 Support

For issues or questions:
- Check hosting platform documentation
- Review app logs in hosting dashboard
- Test locally first with `python app.py`

**May your deployment be successful! 🚀**
cd web_deploy
git init
git add .
git commit -m "Initial commit"
# Create repo on GitHub, then:
git remote add origin YOUR_GITHUB_URL
git push -u origin main