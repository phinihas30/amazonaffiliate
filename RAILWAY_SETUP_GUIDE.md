# Railway PostgreSQL Setup Guide

## The Problem
You're seeing this error: `could not translate host name "postgres.railway.internal" to address: Name or service not known`

This means your Django service can't connect to the PostgreSQL database because:
1. PostgreSQL service is not added to your Railway project, OR
2. PostgreSQL service is not properly connected to your Django service

## Step-by-Step Fix

### 1. Add PostgreSQL Service to Railway

1. Go to your Railway project dashboard
2. Click the **"+ New"** button
3. Select **"Database"** → **"Add PostgreSQL"**
4. Railway will create a new PostgreSQL service

### 2. Connect Services (CRITICAL STEP)

This is the most important step that's often missed:

1. In your Railway project dashboard, you should now see TWO services:
   - Your Django app service (from GitHub)
   - PostgreSQL database service

2. **Connect the services**:
   - Click on your **Django service** (not the database)
   - Go to the **"Variables"** tab
   - You should see `DATABASE_URL` automatically appear
   - If you don't see it, the services aren't connected properly

3. **If DATABASE_URL is missing**:
   - Go to your Django service settings
   - Look for "Service Connections" or "Connected Services"
   - Make sure PostgreSQL is connected
   - Railway should automatically inject the `DATABASE_URL` variable

### 3. Verify Environment Variables

In your Django service's Variables tab, you should see:
- `DATABASE_URL` (automatically set by Railway when PostgreSQL is connected)
- Any custom variables you set (SECRET_KEY, DEBUG, etc.)

### 4. Redeploy

After connecting the services:
1. Go to your Django service
2. Click **"Deploy"** or trigger a new deployment
3. Watch the logs - you should see successful database connection

## Alternative: Manual DATABASE_URL Setup

If automatic connection doesn't work:

1. Go to your **PostgreSQL service**
2. Go to **"Connect"** tab
3. Copy the **"Postgres Connection URL"**
4. Go to your **Django service** → **"Variables"** tab
5. Add a new variable:
   - Name: `DATABASE_URL`
   - Value: (paste the connection URL)

## Troubleshooting

### Check if PostgreSQL is Running
1. Go to PostgreSQL service in Railway
2. Check the "Deployments" tab
3. Make sure it shows "Active" status

### Check Service Connection
1. In your Django service, go to Variables tab
2. Look for `DATABASE_URL` - it should start with `postgresql://`
3. If missing, the services aren't connected

### Check Logs
1. Go to Django service → "Deployments" tab
2. Click on latest deployment
3. Check logs for database connection messages

## Expected Success Messages

After fixing, you should see in your deployment logs:
```
Database configuration:
  Engine: django.db.backends.postgresql
  Host: postgres.railway.internal
  Port: 5432
Database connection successful
Migrations completed successfully
Superuser creation completed
```

## Still Having Issues?

If you're still seeing connection errors:

1. **Delete and recreate** the PostgreSQL service
2. **Ensure both services are in the same Railway project**
3. **Check Railway's status page** for any service outages
4. **Contact Railway support** if the issue persists

The key is making sure Railway automatically injects the `DATABASE_URL` environment variable when you connect the PostgreSQL service to your Django service.
