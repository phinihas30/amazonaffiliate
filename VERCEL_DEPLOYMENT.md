# Vercel Frontend Deployment Guide

## ✅ **Your Frontend is Ready for Vercel Deployment!**

### **What's Been Fixed:**

1. **Environment Variables**: Added proper API URL configuration
2. **Build Configuration**: Updated for Vercel deployment
3. **Routing**: Added SPA routing support
4. **Production Build**: Successfully tested and working

## 🚀 **Deploy to Vercel - Step by Step**

### **Step 1: Prepare Your Repository**

1. **Commit the changes** (we'll do this after this guide)
2. **Push to GitHub** - Make sure your frontend changes are in your repository

### **Step 2: Deploy to Vercel**

1. **Go to [vercel.com](https://vercel.com)** and sign in with GitHub
2. **Click "New Project"**
3. **Import your `amazonaffiliate` repository**
4. **Configure the project:**
   - **Framework Preset**: Create React App
   - **Root Directory**: `frontend` (IMPORTANT!)
   - **Build Command**: `npm run build`
   - **Output Directory**: `build`

### **Step 3: Set Environment Variables in Vercel**

In your Vercel project dashboard:

1. **Go to Settings → Environment Variables**
2. **Add this variable:**
   - **Name**: `REACT_APP_API_URL`
   - **Value**: `https://your-railway-domain.railway.app` (replace with your actual Railway URL)
   - **Environment**: Production

### **Step 4: Deploy**

1. **Click "Deploy"**
2. **Wait for build to complete**
3. **Your frontend will be live at a Vercel URL**

## 🔧 **Important Configuration Details**

### **Environment Variables:**
- **Development**: Uses `http://127.0.0.1:8000` (local Django server)
- **Production**: Uses your Railway API URL

### **API Endpoints Used:**
- `GET /api/products/` - Fetch products
- `GET /api/products/?ordering=...` - Sorted products
- `GET /api/track-product-click/{id}/` - Track clicks

### **Features Ready:**
- ✅ Product listing with pagination
- ✅ Sorting (newest, price ascending/descending)
- ✅ Bootstrap styling
- ✅ Flappy Bird game integration
- ✅ Responsive design
- ✅ Click tracking

## 🎯 **After Deployment**

### **Update Your Railway Backend**

Add your Vercel domain to Railway environment variables:

```
ALLOWED_HOSTS=your-railway-domain.railway.app,your-vercel-domain.vercel.app
CSRF_TRUSTED_ORIGINS=https://your-railway-domain.railway.app,https://your-vercel-domain.vercel.app
CORS_ALLOWED_ORIGINS=https://your-vercel-domain.vercel.app
```

### **Test Your Deployment**

1. **Visit your Vercel URL**
2. **Check if products load** (they should fetch from your Railway API)
3. **Test sorting functionality**
4. **Test product click tracking**
5. **Try the Flappy Bird game**

## 🔍 **Troubleshooting**

### **If Products Don't Load:**
- Check browser console for CORS errors
- Verify `REACT_APP_API_URL` is set correctly in Vercel
- Ensure Railway backend allows your Vercel domain

### **If Build Fails:**
- Check Vercel build logs
- Ensure root directory is set to `frontend`
- Verify all dependencies are in package.json

### **If Routing Doesn't Work:**
- The `vercel.json` handles SPA routing
- All routes should redirect to `index.html`

## 📋 **Final Checklist**

Before deploying:
- ✅ Frontend builds successfully
- ✅ Environment variables configured
- ✅ API URLs use environment variables
- ✅ Vercel configuration files created
- ✅ Repository updated with changes

Your frontend is production-ready for Vercel deployment!
