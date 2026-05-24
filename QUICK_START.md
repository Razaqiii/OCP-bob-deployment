# ⚡ Quick Start Guide

Get your automated deployment running in 5 minutes!

---

## 📦 What's in This Folder

```
bob-app/
├── Jenkinsfile              # Jenkins pipeline definition
├── README.md                # Full documentation
├── SETUP_INSTRUCTIONS.md    # Detailed setup guide
├── QUICK_START.md          # This file
├── app.py                   # Sample Flask application
├── requirements.txt         # Python dependencies
├── .gitignore              # Git ignore patterns
└── k8s/                    # Kubernetes manifests
    ├── deployment.yaml      # Application deployment
    ├── service.yaml         # Service definition
    └── route.yaml          # OpenShift route (external access)
```

---

## 🚀 3-Step Setup

### Step 1: Push to GitHub (2 minutes)

```bash
# Navigate to bob-app directory
cd bob-app

# Initialize git (if needed)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit: Bob deployment pipeline"

# Add your GitHub repo
git remote add origin https://github.com/Razaqiii/OCP-bob-deployment.git

# Push
git push -u origin main
```

### Step 2: Create Jenkins Job (1 minute)

```bash
# Go back to parent directory
cd ..

# Create Jenkins job with webhook
python jenkins.py create bob-pipeline https://github.com/Razaqiii/OCP-bob-deployment.git main
```

**Copy the webhook URL from output!**

### Step 3: Configure GitHub Webhook (2 minutes)

1. Go to: https://github.com/Razaqiii/OCP-bob-deployment/settings/hooks
2. Click "Add webhook"
3. Paste webhook URL: `https://jenkins-production.apps.itz-gkg33y.infra01-lb.tok04.techzone.ibm.com/github-webhook/`
4. Content type: `application/json`
5. Click "Add webhook"

---

## ✅ Test It!

```bash
cd bob-app

# Make a change
echo "# Test" >> README.md

# Push
git add README.md
git commit -m "Test webhook"
git push origin main

# Jenkins will automatically build and deploy! 🎉
```

**Check:**
- Jenkins: https://jenkins-production.apps.itz-gkg33y.infra01-lb.tok04.techzone.ibm.com/job/bob-pipeline
- GitHub: Look for green checkmark on commit

---

## 🎯 What Happens

```
You push code
    ↓
GitHub webhook triggers Jenkins
    ↓
Jenkins runs pipeline
    ↓
Deploys to OpenShift
    ↓
App is live! ✅
```

---

## 📊 Verify Deployment

```bash
# Check pods
oc get pods -n production -l app=bob-app

# Get app URL
oc get route bob-app -n production

# Test app
curl https://$(oc get route bob-app -n production -o jsonpath='{.spec.host}')
```

---

## 🆘 Troubleshooting

**Webhook not working?**
- Check GitHub webhook deliveries (green checkmark = working)
- Verify Jenkins URL is accessible

**Build failing?**
- Check Jenkins console output
- Verify OpenShift access: `oc whoami`

**Need detailed help?**
- See `SETUP_INSTRUCTIONS.md` for full guide
- See `README.md` for complete documentation

---

## 🎉 Success!

You now have:
- ✅ Automated deployment on every push
- ✅ No manual Jenkins triggering needed
- ✅ Application running in OpenShift
- ✅ Continuous deployment pipeline

**Next:** Make changes, push, and watch it auto-deploy! 🚀