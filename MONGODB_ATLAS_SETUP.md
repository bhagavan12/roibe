# 🗄️ MongoDB Atlas Setup Guide

This guide will help you set up MongoDB Atlas for your ROI Calculator Django backend.

## 📋 Prerequisites

- MongoDB Atlas account (free tier available)
- Your Django backend project

## 🚀 Step-by-Step Setup

### 1. **Create MongoDB Atlas Account**

1. Go to [MongoDB Atlas](https://www.mongodb.com/atlas)
2. Click "Try Free" or "Sign Up"
3. Create your account

### 2. **Create a Cluster**

1. **Choose Plan**: Select "FREE" tier (M0)
2. **Cloud Provider**: Choose your preferred provider (AWS, Google Cloud, or Azure)
3. **Region**: Select the region closest to your users
4. **Cluster Name**: Give it a name (e.g., "roical-cluster")
5. Click "Create"

### 3. **Configure Database Access**

1. Go to **Database Access** in the left sidebar
2. Click **"Add New Database User"**
3. **Authentication Method**: Choose "Password"
4. **Username**: Create a username (e.g., "roical_user")
5. **Password**: Create a strong password
6. **Database User Privileges**: Select "Read and write to any database"
7. Click **"Add User"**

### 4. **Configure Network Access**

1. Go to **Network Access** in the left sidebar
2. Click **"Add IP Address"**
3. **Access List Entry**: 
   - For development: Click **"Allow Access from Anywhere"** (0.0.0.0/0)
   - For production: Add your server's IP address
4. Click **"Confirm"**

### 5. **Get Connection String**

1. Go to **Database** in the left sidebar
2. Click **"Connect"** on your cluster
3. Choose **"Connect your application"**
4. **Driver**: Python
5. **Version**: 3.6 or later
6. Copy the connection string

### 6. **Update Your .env File**

Replace the placeholder in your `.env` file:

```env
# Replace with your actual MongoDB Atlas connection string
MONGODB_ATLAS_URI=mongodb+srv://roical_user:your_password@cluster.mongodb.net/roical_db?retryWrites=true&w=majority
DB_NAME=roical_db
```

**Important**: Replace `your_password` with the actual password you created in step 3.

### 7. **Test the Connection**

Run the Django server to test the connection:

```bash
python manage.py runserver
```

If successful, you should see the server start without database errors.

## 🔧 Configuration Options

### Environment Variables

```env
# MongoDB Atlas (Recommended)
MONGODB_ATLAS_URI=mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority

# Local MongoDB (Alternative)
DB_HOST=localhost
DB_PORT=27017
DB_USERNAME=your_username
DB_PASSWORD=your_password
DB_NAME=roical_db
```

### Connection String Format

```
mongodb+srv://username:password@cluster.mongodb.net/database_name?retryWrites=true&w=majority
```

**Components:**
- `username`: Your database user
- `password`: Your database password
- `cluster`: Your cluster address
- `database_name`: Your database name (roical_db)

## 🛡️ Security Best Practices

### 1. **Environment Variables**
- Never commit your `.env` file to version control
- Use environment variables in production

### 2. **Network Access**
- For production: Only allow specific IP addresses
- For development: You can allow all IPs (0.0.0.0/0)

### 3. **Database User**
- Use strong passwords
- Give minimal required privileges
- Create separate users for different environments

### 4. **Connection String**
- Keep your connection string secure
- Rotate passwords regularly
- Use different users for development and production

## 🚨 Troubleshooting

### Common Issues

1. **Connection Refused**
   - Check if your IP is whitelisted in Network Access
   - Verify username and password

2. **Authentication Failed**
   - Double-check username and password
   - Ensure user has correct privileges

3. **Timeout Errors**
   - Check your internet connection
   - Verify cluster is running

4. **SSL Certificate Errors**
   - This is normal for MongoDB Atlas
   - The connection is secure despite warnings

### Testing Connection

You can test your connection using the MongoDB Compass tool:

1. Download [MongoDB Compass](https://www.mongodb.com/products/compass)
2. Use your connection string to connect
3. Verify you can see your database

## 📊 Monitoring

### MongoDB Atlas Dashboard

- **Metrics**: Monitor database performance
- **Logs**: View database logs
- **Alerts**: Set up alerts for issues

### Free Tier Limits

- **Storage**: 512MB
- **RAM**: Shared
- **Connections**: 500 connections
- **Operations**: 500 operations per second

## 🎯 Next Steps

1. **Test your connection** with the Django server
2. **Run migrations** to create your database schema
3. **Test the API** to ensure everything works
4. **Deploy to production** when ready

Your Django backend is now ready to use MongoDB Atlas! 🚀
