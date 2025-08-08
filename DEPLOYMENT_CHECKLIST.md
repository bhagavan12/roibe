# ✅ Deployment Checklist

## 🚀 Quick Deployment Steps

### 1. GitHub Setup
- [ ] Run `deploy_to_github.bat` or manually:
  ```bash
  git init
  git add .
  git commit -m "Initial commit"
  ```
- [ ] Create GitHub repository
- [ ] Push to GitHub:
  ```bash
  git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
  git branch -M main
  git push -u origin main
  ```

### 2. Render.com Setup
- [ ] Sign up at [render.com](https://render.com)
- [ ] Connect GitHub account
- [ ] Create new Web Service
- [ ] Select your repository

### 3. Render Configuration
- [ ] **Name**: `roi-calculator-backend`
- [ ] **Environment**: `Python 3`
- [ ] **Build Command**: `./build.sh`
- [ ] **Start Command**: `gunicorn roical_backend.wsgi:application`

### 4. Environment Variables (Add in Render Dashboard)
```env
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOST=your-app-name.onrender.com
MONGODB_ATLAS_URI=mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority
DB_NAME=roi_calculator_db
```

### 5. Test Deployment
- [ ] Visit: `https://your-app-name.onrender.com/api/`
- [ ] Should see: `{"status": "healthy", "message": "ROI Calculator API is running"}`
- [ ] Test registration: `POST /api/register/`
- [ ] Test login: `POST /api/token/`

### 6. Update Frontend
- [ ] Change API_BASE_URL to: `https://your-app-name.onrender.com/api`
- [ ] Update CORS settings if needed

## 🔧 Files Created for Deployment
- ✅ `build.sh` - Build script for Render
- ✅ `runtime.txt` - Python version specification
- ✅ `roical_backend/production_settings.py` - Production settings
- ✅ `requirements.txt` - Updated with production dependencies
- ✅ `DEPLOYMENT.md` - Detailed deployment guide
- ✅ `deploy_to_github.bat` - GitHub setup script

## 🚨 Common Issues & Solutions

### Build Fails
- Check `requirements.txt` has all dependencies
- Verify Python version in `runtime.txt`
- Check build logs in Render dashboard

### Database Connection Fails
- Verify MongoDB Atlas connection string
- Check network access in MongoDB Atlas
- Ensure database user has correct permissions

### CORS Errors
- Update `CORS_ALLOWED_ORIGINS` in production settings
- Add your frontend domain to allowed origins

## 📞 Support
- Render Documentation: https://render.com/docs
- MongoDB Atlas Documentation: https://docs.atlas.mongodb.com
- Django Documentation: https://docs.djangoproject.com

## 🎯 Success Indicators
- ✅ Health check returns 200 OK
- ✅ User registration works
- ✅ User login works
- ✅ Results can be saved and retrieved
- ✅ Frontend can connect to backend
- ✅ HTTPS is working
- ✅ No CORS errors in browser console
