#!/usr/bin/env python3
"""
Fix .env file with proper MongoDB Atlas connection string
"""

def fix_env_file():
    """Fix the .env file with proper formatting"""
    
    # Your MongoDB Atlas connection string (replace with your actual one)
    connection_string = "mongodb+srv://admin:admin@cluster0.vr23ljt.mongodb.net/roi-cal?retryWrites=true&w=majority&appName=Cluster0"
    
    env_content = f"""# Django Settings
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True

# MongoDB Atlas Settings
MONGODB_ATLAS_URI={connection_string}
DB_NAME=roi-cal

# Alternative: Individual MongoDB Settings (for local or other MongoDB)
DB_HOST=localhost
DB_PORT=27017
DB_USERNAME=
DB_PASSWORD=
"""
    
    # Write to .env file
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print("✅ .env file fixed with proper MongoDB Atlas connection string")
    print(f"📊 Database name: roi-cal")
    print("\n🚀 Next Steps:")
    print("1. Test the connection: python manage.py runserver")
    print("2. Test the API: python test_api.py")

if __name__ == "__main__":
    fix_env_file()
