#!/usr/bin/env python3
"""
MongoDB Atlas Setup Helper Script
"""
import os
import re

def validate_connection_string(uri):
    """Validate MongoDB Atlas connection string format"""
    pattern = r'^mongodb\+srv://[^:]+:[^@]+@[^/]+/[^?]+\?.*$'
    return bool(re.match(pattern, uri))

def setup_mongodb_atlas():
    """Interactive setup for MongoDB Atlas"""
    print("🗄️  MongoDB Atlas Setup Helper")
    print("=" * 40)
    
    print("\n📋 Prerequisites:")
    print("1. MongoDB Atlas account (free tier available)")
    print("2. Cluster created in MongoDB Atlas")
    print("3. Database user with read/write permissions")
    print("4. Network access configured (IP whitelist)")
    
    print("\n🔗 Connection String Format:")
    print("mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority")
    
    print("\n" + "=" * 40)
    
    # Get connection string from user
    while True:
        connection_string = input("\nEnter your MongoDB Atlas connection string: ").strip()
        
        if not connection_string:
            print("❌ Connection string cannot be empty")
            continue
            
        if not validate_connection_string(connection_string):
            print("❌ Invalid connection string format")
            print("Expected format: mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority")
            continue
            
        break
    
    # Extract database name from connection string
    db_name_match = re.search(r'/([^/?]+)(?:\?|$)', connection_string)
    db_name = db_name_match.group(1) if db_name_match else 'roical_db'
    
    # Create .env file content
    env_content = f"""# Django Settings
SECRET_KEY=django-insecure-change-this-in-production
DEBUG=True

# MongoDB Atlas Settings
MONGODB_ATLAS_URI={connection_string}
DB_NAME={db_name}

# Alternative: Individual MongoDB Settings (for local or other MongoDB)
DB_HOST=localhost
DB_PORT=27017
DB_USERNAME=
DB_PASSWORD=
"""
    
    # Write to .env file
    with open('.env', 'w') as f:
        f.write(env_content)
    
    print(f"\n✅ Configuration saved to .env file")
    print(f"📊 Database name: {db_name}")
    
    print("\n🚀 Next Steps:")
    print("1. Test the connection: python manage.py runserver")
    print("2. Run migrations: python manage.py migrate")
    print("3. Test the API: python test_api.py")
    
    print("\n⚠️  Security Notes:")
    print("- Never commit .env file to version control")
    print("- Keep your connection string secure")
    print("- Use different users for development and production")

if __name__ == "__main__":
    setup_mongodb_atlas()
