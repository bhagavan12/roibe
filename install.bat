@echo off
echo Setting up ROI Calculator Django Backend...
echo ================================================

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment and install requirements
echo Installing requirements...
call venv\Scripts\activate
pip install -r requirements.txt

REM Create .env file if it doesn't exist
if not exist ".env" (
    echo Creating .env file...
    copy env.example .env
)

REM Run migrations
echo Running migrations...
python manage.py makemigrations
python manage.py migrate

echo.
echo ================================================
echo Setup completed successfully!
echo.
echo Next steps:
echo 1. Optional: Ensure MongoDB is running on localhost:27017
echo 2. Run: python manage.py runserver
echo 3. Access the API at: http://localhost:8000/api/
echo 4. Access admin at: http://localhost:8000/admin/
echo.
echo Optional: Create a superuser with: python manage.py createsuperuser
pause
