#!/usr/bin/env python
"""
Test script to verify superuser creation works locally before deployment
"""
import os
import sys
import django
from django.core.management import execute_from_command_line

# Add the project directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Set Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')

# Setup Django
django.setup()

from django.contrib.auth import get_user_model

def test_superuser_creation():
    """Test the superuser creation command"""
    User = get_user_model()
    
    print("Testing superuser creation...")
    
    # Clear any existing superusers for testing
    User.objects.filter(is_superuser=True).delete()
    print("Cleared existing superusers")
    
    # Test 1: With environment variables
    print("\n--- Test 1: With environment variables ---")
    os.environ['DJANGO_SUPERUSER_USERNAME'] = 'testadmin'
    os.environ['DJANGO_SUPERUSER_EMAIL'] = 'test@example.com'
    os.environ['DJANGO_SUPERUSER_PASSWORD'] = 'testpass123'
    
    execute_from_command_line(['manage.py', 'create_superuser_from_env'])
    
    # Verify creation
    if User.objects.filter(username='testadmin', is_superuser=True).exists():
        print("✅ Test 1 PASSED: Superuser created with environment variables")
    else:
        print("❌ Test 1 FAILED: Superuser not created")
    
    # Test 2: Without environment variables (fallback)
    print("\n--- Test 2: Without environment variables (fallback) ---")
    # Clear environment variables
    for key in ['DJANGO_SUPERUSER_USERNAME', 'DJANGO_SUPERUSER_EMAIL', 'DJANGO_SUPERUSER_PASSWORD']:
        if key in os.environ:
            del os.environ[key]
    
    # Clear existing users
    User.objects.filter(is_superuser=True).delete()
    
    execute_from_command_line(['manage.py', 'create_superuser_from_env'])
    
    # Verify fallback creation
    if User.objects.filter(username='admin', is_superuser=True).exists():
        print("✅ Test 2 PASSED: Superuser created with fallback credentials")
    else:
        print("❌ Test 2 FAILED: Superuser not created with fallback")
    
    # Test 3: Skip if exists
    print("\n--- Test 3: Skip if superuser exists ---")
    execute_from_command_line(['manage.py', 'create_superuser_from_env', '--skip-if-exists'])
    
    # Should not create another user
    superuser_count = User.objects.filter(is_superuser=True).count()
    if superuser_count == 1:
        print("✅ Test 3 PASSED: Skipped creation when superuser exists")
    else:
        print(f"❌ Test 3 FAILED: Expected 1 superuser, found {superuser_count}")
    
    print("\n--- Test Summary ---")
    print("All tests completed. Check the output above for results.")
    
    # Clean up
    User.objects.filter(is_superuser=True).delete()
    print("Cleaned up test superusers")

if __name__ == '__main__':
    test_superuser_creation()
