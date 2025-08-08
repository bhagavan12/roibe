#!/usr/bin/env python3
"""
Setup script for ROI Calculator Django Backend
"""
import os
import subprocess
import sys

def run_command(command, description):
    """Run a command and handle errors"""
    print(f"Running: {description}")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✓ {description} completed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ {description} failed: {e}")
        print(f"Error output: {e.stderr}")
        return False

def create_env_file():
    """Create .env file if it doesn't exist"""
    if not os.path.exists('.env'):
        print("Creating .env file...")
        with open('.env', 'w') as f:
            f.write("""# Django Settings
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True

# Database Settings
DB_NAME=roical_db
DB_HOST=localhost
DB_PORT=27017
DB_USERNAME=
DB_PASSWORD=
""")
        print("✓ .env file created")
    else:
        print("✓ .env file already exists")

def main():
    print("Setting up ROI Calculator Django Backend...")
    print("=" * 50)
    
    # Check if virtual environment exists
    if not os.path.exists('venv'):
        print("Creating virtual environment...")
        if not run_command("python -m venv venv", "Creating virtual environment"):
            return False
    else:
        print("✓ Virtual environment already exists")
    
    # Activate virtual environment and install requirements
    if sys.platform == "win32":
        activate_cmd = "venv\\Scripts\\activate"
        pip_cmd = "venv\\Scripts\\pip"
    else:
        activate_cmd = "source venv/bin/activate"
        pip_cmd = "venv/bin/pip"
    
    if not run_command(f"{pip_cmd} install -r requirements.txt", "Installing requirements"):
        return False
    
    # Create .env file
    create_env_file()
    
    # Run migrations
    if not run_command(f"{activate_cmd} && python manage.py makemigrations", "Creating migrations"):
        return False
    
    if not run_command(f"{activate_cmd} && python manage.py migrate", "Running migrations"):
        return False
    
    print("\n" + "=" * 50)
    print("Setup completed successfully!")
    print("\nNext steps:")
    print("1. Ensure MongoDB is running on localhost:27017")
    print("2. Run: python manage.py runserver")
    print("3. Access the API at: http://localhost:8000/api/")
    print("4. Access admin at: http://localhost:8000/admin/")
    print("\nOptional: Create a superuser with: python manage.py createsuperuser")

if __name__ == "__main__":
    main()
