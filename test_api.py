#!/usr/bin/env python3
"""
Simple test script to verify API endpoints
"""
import requests
import json

BASE_URL = "http://localhost:8000/api"

def test_register():
    """Test user registration"""
    print("Testing user registration...")
    data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "confirm_password": "testpass123"
    }
    
    response = requests.post(f"{BASE_URL}/register/", json=data)
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        print("✓ Registration successful")
        return True
    else:
        print(f"✗ Registration failed: {response.text}")
        return False

def test_login():
    """Test user login"""
    print("\nTesting user login...")
    data = {
        "email": "test@example.com",
        "password": "testpass123"
    }
    
    response = requests.post(f"{BASE_URL}/token/", json=data)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        token_data = response.json()
        print("✓ Login successful")
        return token_data['access']
    else:
        print(f"✗ Login failed: {response.text}")
        return None

def test_save_result(token):
    """Test saving a calculation result"""
    print("\nTesting save result...")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    data = {
        "type": "quick",
        "inputs": {
            "annualRevenue": 1000000,
            "annualCloudSpend": 100000,
            "numEngineers": 10
        },
        "results": {
            "roi": 150,
            "savings": 50000
        }
    }
    
    response = requests.post(f"{BASE_URL}/results/", json=data, headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 201:
        print("✓ Save result successful")
        return True
    else:
        print(f"✗ Save result failed: {response.text}")
        return False

def test_get_results(token):
    """Test getting user results"""
    print("\nTesting get results...")
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    
    response = requests.get(f"{BASE_URL}/results/", headers=headers)
    print(f"Status: {response.status_code}")
    if response.status_code == 200:
        results = response.json()
        print(f"✓ Get results successful - Found {len(results)} results")
        return True
    else:
        print(f"✗ Get results failed: {response.text}")
        return False

def main():
    print("Testing ROI Calculator API")
    print("=" * 40)
    
    # Test registration
    if not test_register():
        print("Registration failed, stopping tests")
        return
    
    # Test login
    token = test_login()
    if not token:
        print("Login failed, stopping tests")
        return
    
    # Test saving result
    if not test_save_result(token):
        print("Save result failed")
        return
    
    # Test getting results
    if not test_get_results(token):
        print("Get results failed")
        return
    
    print("\n" + "=" * 40)
    print("All tests passed! API is working correctly.")

if __name__ == "__main__":
    main()
