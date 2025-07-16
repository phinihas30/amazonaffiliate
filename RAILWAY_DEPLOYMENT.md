# Railway Deployment Guide

## Environment Variables Setup

To properly deploy your Django application on Railway, you need to set the following environment variables in your Railway project dashboard:

### Required Environment Variables

1. **Database Configuration** (automatically provided by Railway PostgreSQL service):
   - `DATABASE_URL` - Automatically set when you add PostgreSQL service

2. **Django Configuration**:
   - `SECRET_KEY` - Your Django secret key (generate a new one for production)
   - `DEBUG` - Set to `False` for production
   - `ALLOWED_HOSTS` - Your Railway domain (e.g., `your-app.railway.app`)
   - `CSRF_TRUSTED_ORIGINS` - Your Railway domain with protocol (e.g., `https://your-app.railway.app`)

3. **Superuser Configuration** (recommended for production):
   - `DJANGO_SUPERUSER_USERNAME` - Your admin username
   - `DJANGO_SUPERUSER_EMAIL` - Your admin email
   - `DJANGO_SUPERUSER_PASSWORD` - Your admin password

### Setting Environment Variables in Railway

1. Go to your Railway project dashboard
2. Click on your service
3. Go to the "Variables" tab
4. Add each environment variable with its value

### Example Environment Variables

```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-app.railway.app
CSRF_TRUSTED_ORIGINS=https://your-app.railway.app
DJANGO_SUPERUSER_USERNAME=youradmin
DJANGO_SUPERUSER_EMAIL=admin@yourdomain.com
DJANGO_SUPERUSER_PASSWORD=your-secure-password
```

## Deployment Process

1. **Connect Repository**: Connect your GitHub repository to Railway
2. **Add PostgreSQL**: Add a PostgreSQL database service to your project
3. **Set Environment Variables**: Configure all the variables listed above
4. **Deploy**: Railway will automatically deploy using the Procfile

## Troubleshooting

### Superuser Creation Issues

If you encounter superuser creation errors:

1. **Check Environment Variables**: Ensure all superuser environment variables are set
2. **Fallback Mode**: If environment variables are missing, the system will create a default admin user:
   - Username: `admin`
   - Email: `admin@example.com`
   - Password: `admin123`
   - **IMPORTANT**: Change these credentials immediately after first login!

3. **Manual Creation**: You can also create a superuser manually using Railway's console:
   ```bash
   python manage.py createsuperuser
   ```

### Database Issues

- Ensure PostgreSQL service is properly connected
- Check that `DATABASE_URL` environment variable is set
- Verify database migrations are running during deployment

### Static Files Issues

- Static files are collected automatically during deployment
- Ensure `STATIC_ROOT` is properly configured in settings.py
- WhiteNoise middleware is configured for serving static files

## Security Notes

1. **Never commit sensitive data** like secret keys or passwords to your repository
2. **Use strong passwords** for your superuser account
3. **Set DEBUG=False** in production
4. **Configure proper ALLOWED_HOSTS** and CSRF_TRUSTED_ORIGINS
5. **Regularly update dependencies** for security patches

## Post-Deployment Steps

1. **Test the application**: Visit your Railway URL to ensure it's working
2. **Access admin panel**: Go to `/admin/` and login with your superuser credentials
3. **Change default credentials**: If using fallback credentials, change them immediately
4. **Monitor logs**: Check Railway logs for any errors or issues
