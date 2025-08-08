# 🚀 Deployment Guide - ROI Calculator Backend

This guide will help you deploy your Django ROI Calculator backend to Render.com.

## 📋 Prerequisites

1. **GitHub Account**: Your code should be pushed to GitHub
2. **Render.com Account**: Sign up at [render.com](https://render.com)
3. **MongoDB Atlas**: Your database should be set up and running

## 🔧 Step 1: Prepare Your Code for GitHub

### 1.1 Initialize Git Repository
```bash
git init
git add .
git commit -m "Initial commit - ROI Calculator Backend"
```

### 1.2 Create GitHub Repository
1. Go to [GitHub](https://github.com)
2. Create a new repository
3. Follow the instructions to push your code

```bash
git remote add origin https://github.com/yourusername/roi-calculator-backend.git
git branch -M main
git push -u origin main
```

## 🌐 Step 2: Deploy to Render.com

### 2.1 Create Render Account
1. Go to [render.com](https://render.com)
2. Sign up with your GitHub account
3. Connect your GitHub repository

### 2.2 Create New Web Service
1. Click "New +" → "Web Service"
2. Connect your GitHub repository
3. Configure the service:

**Basic Settings:**
- **Name**: `roi-calculator-backend`
- **Environment**: `Python 3`
- **Region**: Choose closest to your users
- **Branch**: `main`
- **Root Directory**: Leave empty (if code is in root)
- **Build Command**: `./build.sh`
- **Start Command**: `gunicorn roical_backend.wsgi:application`

### 2.3 Environment Variables
Add these environment variables in Render dashboard:

```env
# Django Settings
SECRET_KEY=your-super-secret-key-here-make-it-long-and-random
DEBUG=False
ALLOWED_HOST=your-app-name.onrender.com

# MongoDB Atlas Settings
MONGODB_ATLAS_URI=mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority
DB_NAME=roi_calculator_db

# Alternative: Local MongoDB (if not using Atlas)
DB_HOST=localhost
DB_PORT=27017
DB_USERNAME=
DB_PASSWORD=
```

### 2.4 Advanced Settings
- **Auto-Deploy**: Enable (recommended)
- **Health Check Path**: `/api/` (optional)

## 🔧 Step 3: Update Requirements

Make sure your `requirements.txt` includes:

```txt
Django==4.1.13
djangorestframework==3.14.0
django-cors-headers==4.3.1
djongo==1.3.6
pymongo==3.12.3
python-decouple==3.8
djangorestframework-simplejwt==5.3.0
sqlparse==0.2.4
gunicorn==21.2.0
whitenoise==6.6.0
```

## 🌍 Step 4: Update Frontend Configuration

Once deployed, update your frontend API base URL:

```typescript
// Update this in your frontend code
const API_BASE_URL = 'https://your-app-name.onrender.com/api';
```

## 🔍 Step 5: Test Your Deployment

### 5.1 Check Health
Visit: `https://your-app-name.onrender.com/api/`

### 5.2 Test API Endpoints
```bash
# Test registration
curl -X POST https://your-app-name.onrender.com/api/register/ \
  -H "Content-Type: application/json" \
  -d '{"username":"test","email":"test@example.com","password":"testpass","confirm_password":"testpass"}'

# Test login
curl -X POST https://your-app-name.onrender.com/api/token/ \
  -H "Content-Type: application/json" \
  -d '{"email":"test@example.com","password":"testpass"}'
```

## 🛠️ Troubleshooting

### Common Issues:

1. **Build Fails**
   - Check build logs in Render dashboard
   - Ensure all dependencies are in `requirements.txt`
   - Verify Python version in `runtime.txt`

2. **Database Connection Fails**
   - Verify MongoDB Atlas connection string
   - Check network access in MongoDB Atlas
   - Ensure database user has correct permissions

3. **CORS Errors**
   - Update `CORS_ALLOWED_ORIGINS` in production settings
   - Add your frontend domain to allowed origins

4. **Static Files Not Loading**
   - Ensure `STATIC_ROOT` is set correctly
   - Check if `collectstatic` runs in build script

### Debug Commands:
```bash
# Check logs
render logs

# SSH into instance (if available)
render ssh

# Check environment variables
echo $SECRET_KEY
echo $MONGODB_ATLAS_URI
```

## 🔒 Security Checklist

- [ ] `DEBUG=False` in production
- [ ] Strong `SECRET_KEY` generated
- [ ] MongoDB Atlas properly configured
- [ ] CORS origins restricted to your domains
- [ ] HTTPS enabled (automatic on Render)
- [ ] Environment variables secured

## 📊 Monitoring

### Render Dashboard
- Monitor application health
- View logs and errors
- Check resource usage

### MongoDB Atlas
- Monitor database performance
- Check connection metrics
- Review query performance

## 🚀 Custom Domain (Optional)

1. **Add Custom Domain in Render**
   - Go to your service settings
   - Add custom domain
   - Update DNS records

2. **Update Environment Variables**
   ```env
   ALLOWED_HOST=yourdomain.com
   ```

3. **Update CORS Settings**
   ```python
   CORS_ALLOWED_ORIGINS = [
       "https://yourdomain.com",
       "https://www.yourdomain.com",
   ]
   ```

## 📝 Environment Variables Reference

| Variable | Description | Required |
|----------|-------------|----------|
| `SECRET_KEY` | Django secret key | Yes |
| `DEBUG` | Debug mode (False for production) | Yes |
| `ALLOWED_HOST` | Your app domain | Yes |
| `MONGODB_ATLAS_URI` | MongoDB Atlas connection string | Yes |
| `DB_NAME` | Database name | Yes |
| `DB_HOST` | Database host (fallback) | No |
| `DB_PORT` | Database port (fallback) | No |
| `DB_USERNAME` | Database username (fallback) | No |
| `DB_PASSWORD` | Database password (fallback) | No |

## 🎯 Next Steps

1. **Monitor Performance**: Use Render's built-in monitoring
2. **Set Up Alerts**: Configure notifications for downtime
3. **Scale Up**: Upgrade plan if needed
4. **Backup Strategy**: Ensure MongoDB Atlas backups are enabled
5. **SSL Certificate**: Automatic on Render, but verify

Your ROI Calculator backend is now deployed and ready to serve your frontend! 🚀
