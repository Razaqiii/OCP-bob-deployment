# 🤖 Bob Deployment Pipeline

This repository demonstrates automated deployment to OpenShift using Jenkins webhooks.

## 🚀 Features

- **Automatic Deployment**: Push to `main` branch triggers Jenkins pipeline
- **OpenShift Integration**: Deploys directly to OpenShift production namespace
- **GitHub Webhooks**: No manual Jenkins triggering needed
- **Build Verification**: Automatic health checks and deployment verification

## 📋 How It Works

```
Developer pushes code → GitHub webhook → Jenkins → OpenShift → App deployed!
```

### Workflow

1. **Push Code**: Developer commits and pushes to GitHub
2. **Webhook Trigger**: GitHub sends webhook to Jenkins
3. **Pipeline Execution**: Jenkins runs the Jenkinsfile
4. **Deployment**: Application deploys to OpenShift
5. **Verification**: Pipeline verifies deployment success

## 🔧 Jenkins Configuration

- **Job Name**: `bob-pipeline`
- **Jenkins URL**: https://jenkins-production.apps.itz-gkg33y.infra01-lb.tok04.techzone.ibm.com/job/bob-pipeline
- **Webhook URL**: https://jenkins-production.apps.itz-gkg33y.infra01-lb.tok04.techzone.ibm.com/github-webhook/
- **Branch**: `main`
- **Trigger**: GitHub push events

## 📦 Repository Structure

```
bob-app/
├── Jenkinsfile          # Jenkins pipeline definition
├── README.md            # This file
├── app.py               # Sample Flask application
├── requirements.txt     # Python dependencies
└── k8s/                 # Kubernetes manifests (optional)
    ├── deployment.yaml
    ├── service.yaml
    └── route.yaml
```

## 🎯 Quick Start

### For Developers

```bash
# Clone the repository
git clone https://github.com/Razaqiii/OCP-bob-deployment.git
cd OCP-bob-deployment

# Make changes
echo "# My changes" >> README.md

# Commit and push
git add .
git commit -m "Update README"
git push origin main

# Jenkins will automatically build and deploy! 🎉
```

### For DevOps/Admins

**Setup Jenkins Job:**
```bash
python jenkins.py create bob-pipeline https://github.com/Razaqiii/OCP-bob-deployment.git main
```

**Configure GitHub Webhook:**
1. Go to: https://github.com/Razaqiii/OCP-bob-deployment/settings/hooks
2. Add webhook with URL: `https://jenkins-production.../github-webhook/`
3. Content type: `application/json`
4. Events: "Just the push event"

## 🔍 Monitoring

### Check Build Status
- Jenkins: https://jenkins-production.apps.itz-gkg33y.infra01-lb.tok04.techzone.ibm.com/job/bob-pipeline
- GitHub: Check commit status (green checkmark or red X)

### Check Deployment
```bash
# Check pods
oc get pods -n production -l app=bob-app

# Check deployment
oc get deployment bob-app -n production

# Get application URL
oc get route bob-app -n production
```

## 📊 Pipeline Stages

1. **Checkout** - Clone repository from GitHub
2. **Build Info** - Display build information
3. **Verify OpenShift Connection** - Test OCP connectivity
4. **Deploy to OpenShift** - Apply Kubernetes manifests
5. **Verify Deployment** - Check deployment status
6. **Get Application URL** - Display application URL

## 🛠️ Customization

### Modify Deployment

Edit `k8s/deployment.yaml` to customize:
- Number of replicas
- Resource limits
- Environment variables
- Container image

### Modify Pipeline

Edit `Jenkinsfile` to add:
- Testing stages
- Security scanning
- Notifications
- Approval gates

## 🔐 Security

- Repository: Public (for demo)
- Webhook: No secret (for demo)
- OpenShift: Uses service account authentication
- Jenkins: Bearer token authentication

**For Production**: Add webhook secrets and use private repositories.

## 📝 Example Deployment

```yaml
# k8s/deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: bob-app
spec:
  replicas: 2
  selector:
    matchLabels:
      app: bob-app
  template:
    metadata:
      labels:
        app: bob-app
    spec:
      containers:
      - name: bob-app
        image: python:3.9-slim
        ports:
        - containerPort: 8080
```

## 🎓 Learning Resources

- [Jenkins Pipeline Documentation](https://www.jenkins.io/doc/book/pipeline/)
- [OpenShift Documentation](https://docs.openshift.com/)
- [GitHub Webhooks](https://docs.github.com/en/webhooks)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Push and create a pull request
5. Jenkins will automatically test your changes!

## 📞 Support

- Jenkins Issues: Check Jenkins console output
- OpenShift Issues: Check pod logs with `oc logs`
- GitHub Issues: Check webhook delivery status

## 🎉 Success Indicators

✅ Green checkmark on GitHub commit  
✅ Jenkins build shows "SUCCESS"  
✅ Pods running in OpenShift  
✅ Application accessible via route  

---

**Created with ❤️ by Bob - Your AI DevOps Assistant**

*Last Updated: 2026-05-24*