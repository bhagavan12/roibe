@echo off
echo 🚀 Preparing to deploy ROI Calculator Backend to GitHub...
echo.

echo 📝 Initializing Git repository...
git init

echo 📦 Adding all files to Git...
git add .

echo 💾 Creating initial commit...
git commit -m "Initial commit - ROI Calculator Backend with MongoDB Atlas"

echo.
echo 🔗 Please create a new repository on GitHub and then run:
echo.
echo git remote add origin https://github.com/bhagavan12/roibackend.git
echo git branch -M main
echo git push -u origin main
echo.
echo 📋 Next steps:
echo 1. Go to https://github.com
echo 2. Create a new repository
echo 3. Copy the repository URL
echo 4. Replace YOUR_USERNAME and YOUR_REPO_NAME in the commands above
echo 5. Run the commands to push to GitHub
echo.
echo 🎯 After pushing to GitHub, follow the DEPLOYMENT.md guide to deploy on Render.com
pause
