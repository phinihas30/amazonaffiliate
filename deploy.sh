#!/bin/bash

# Railway deployment script
# This script runs database operations that require a live database connection

set -e  # Exit on any error

echo "Starting Railway deployment script..."

# Function to wait for database with retries
wait_for_db() {
    echo "Waiting for database to be ready..."
    local max_attempts=30
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

        echo "Database not ready, waiting 2 seconds..."
        sleep 2
        attempt=$((attempt + 1))
    done

    echo "ERROR: Database connection failed after $max_attempts attempts"
    return 1
}

# Wait for database to be ready
wait_for_db

# Run migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files (in case it wasn't done during build)
echo "Collecting static files..."
python manage.py collectstatic --noinput --clear || echo "Static files collection failed, continuing..."

# Create superuser if needed
echo "Creating superuser..."
python manage.py create_superuser_from_env --skip-if-exists

echo "Railway deployment script completed successfully!"
