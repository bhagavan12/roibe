# ROI Calculator Django Backend

A Django REST API backend for the ROI Calculator application with MongoDB integration, JWT authentication, and user management.

## Features

- **User Authentication**: JWT-based authentication with login/signup
- **ROI Calculations Storage**: Save and retrieve both quick and full ROI calculations
- **MongoDB Integration**: Flexible document storage for calculation inputs and results
- **Export Functionality**: Export calculation results as CSV
- **CORS Support**: Configured for frontend integration
- **Admin Interface**: Django admin for data management

## API Endpoints

### Authentication
- `POST /api/token/` - Login (get JWT token)
- `POST /api/token/refresh/` - Refresh JWT token
- `POST /api/register/` - User registration
- `GET /api/profile/` - Get user profile

### Results Management
- `GET /api/results/` - Get all user's results
- `POST /api/results/` - Save new calculation result
- `GET /api/results/{id}/` - Get specific result
- `DELETE /api/results/{id}/` - Delete specific result
- `GET /api/results/export/` - Export all results as CSV

## Setup Instructions

### Prerequisites
- Python 3.8+
- MongoDB Atlas account (recommended) or local MongoDB
- pip

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd roical-backend
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Environment Configuration**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Database Setup**
   - **MongoDB Atlas (Recommended)**: Follow the [MongoDB Atlas Setup Guide](MONGODB_ATLAS_SETUP.md)
   - **Local MongoDB**: Ensure MongoDB is running on localhost:27017
   - Database name: `roical_db` (configurable in .env)

6. **Run Migrations**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Create Superuser (Optional)**
   ```bash
   python manage.py createsuperuser
   ```

8. **Run Development Server**
   ```bash
   python manage.py runserver
   ```

The API will be available at `http://localhost:8000/api/`

## Environment Variables

Create a `.env` file with the following variables:

```env
SECRET_KEY=your-secret-key-here
DEBUG=True

# MongoDB Atlas (Recommended)
MONGODB_ATLAS_URI=mongodb+srv://username:password@cluster.mongodb.net/roical_db?retryWrites=true&w=majority
DB_NAME=roical_db

# Local MongoDB (Alternative)
DB_HOST=localhost
DB_PORT=27017
DB_USERNAME=
DB_PASSWORD=
```

## Frontend Integration

Update your frontend API configuration to use the Django backend:

```typescript
const API_BASE_URL = 'http://localhost:8000/api';

// For authentication
const login = async (email: string, password: string) => {
  const response = await fetch(`${API_BASE_URL}/token/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, password }),
  });
  const data = await response.json();
  if (response.ok) {
    localStorage.setItem('token', data.access);
  }
  return response.ok;
};

// For API calls with authentication
const getAuthHeaders = () => {
  const token = localStorage.getItem('token');
  return {
    'Content-Type': 'application/json',
    ...(token && { 'Authorization': `Bearer ${token}` }),
  };
};
```

## Data Models

### User Model
- `id`: Primary key
- `username`: Unique username
- `email`: Unique email (used for login)
- `password`: Hashed password

### Result Model
- `id`: Primary key
- `user`: Foreign key to User
- `timestamp`: Auto-generated timestamp
- `type`: 'quick' or 'full'
- `inputs`: JSON field for calculation inputs
- `results`: JSON field for calculation results

## Admin Interface

Access the Django admin at `http://localhost:8000/admin/` to:
- Manage users
- View and manage calculation results
- Export data

## Development

### Running Tests
```bash
python manage.py test
```

### Code Formatting
```bash
# Install black for code formatting
pip install black
black .
```

## Production Deployment

For production deployment:

1. Set `DEBUG=False` in environment variables
2. Use a strong `SECRET_KEY`
3. Configure MongoDB with authentication
4. Set up proper CORS origins
5. Use a production WSGI server (Gunicorn, uWSGI)
6. Set up reverse proxy (Nginx)

## License

This project is licensed under the MIT License.
