#!/bin/bash

# Railway deployment script
# This script runs database operations that require a live database connection

set -e  # Exit on any error

echo "Starting Railway deployment script..."

# Check environment variables
echo "Checking environment variables..."
echo "DATABASE_URL is set: $([ -n "$DATABASE_URL" ] && echo "YES" || echo "NO")"
if [ -n "$DATABASE_URL" ]; then
    echo "DATABASE_URL starts with: $(echo $DATABASE_URL | cut -c1-20)..."
fi

# Function to check database configuration
check_db_config() {
    echo "Checking database configuration..."
    python -c "
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')
django.setup()
from django.conf import settings

print('Database configuration:')
db_config = settings.DATABASES['default']
print(f'  Engine: {db_config.get(\"ENGINE\", \"Not set\")}')
print(f'  Name: {db_config.get(\"NAME\", \"Not set\")}')
print(f'  Host: {db_config.get(\"HOST\", \"Not set\")}')
print(f'  Port: {db_config.get(\"PORT\", \"Not set\")}')
print(f'  User: {db_config.get(\"USER\", \"Not set\")}')
"
}

# Function to wait for database with retries
wait_for_db() {
    echo "Waiting for database to be ready..."

    # If no DATABASE_URL, skip database operations
    if [ -z "$DATABASE_URL" ]; then
        echo "WARNING: DATABASE_URL not set. Skipping database operations."
        echo "This will use SQLite fallback. Make sure to add PostgreSQL service in Railway."
        return 0
    fi

    local max_attempts=10  # Reduced attempts
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        echo "Database connection attempt $attempt/$max_attempts..."

        if python -c "
import django
import os
import sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'amazon.settings')
django.setup()
from django.db import connection
try:
    connection.ensure_connection()
    print('Database connection successful')
    sys.exit(0)
except Exception as e:
    print(f'Database connection failed: {e}')
    sys.exit(1)
" 2>/dev/null; then
            echo "Database is ready!"
            return 0
        fi

        echo "Database not ready, waiting 3 seconds..."
        sleep 3
        attempt=$((attempt + 1))
    done

    echo "WARNING: Database connection failed after $max_attempts attempts"
    echo "Continuing with SQLite fallback..."
    return 0  # Don't fail, just continue
}

# Check database configuration first
check_db_config

# Wait for database to be ready
wait_for_db

# Run migrations
echo "Running database migrations..."
if python manage.py migrate --noinput; then
    echo "Migrations completed successfully"
else
    echo "WARNING: Migrations failed, but continuing..."
fi

# Collect static files (in case it wasn't done during build)
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear || echo "Static files collection failed, continuing..."

# Create superuser if needed
echo "Creating superuser..."
if python manage.py create_superuser_from_env --skip-if-exists; then
    echo "Superuser creation completed"
else
    echo "WARNING: Superuser creation failed, but continuing..."
fi

echo "Railway deployment script completed!"
echo ""
echo "IMPORTANT NEXT STEPS:"
echo "1. If you see database connection errors above, add a PostgreSQL service in Railway"
echo "2. Make sure the PostgreSQL service is connected to your Django service"
echo "3. Check that DATABASE_URL environment variable is automatically set"
echo "4. If using SQLite fallback, your data won't persist between deployments"
