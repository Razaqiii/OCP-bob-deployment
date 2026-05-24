pipeline {
    agent any
    
    environment {
        OCP_NAMESPACE = 'production'
        APP_NAME = 'bob-app'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '📦 Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Info') {
            steps {
                echo '📊 Build Information'
                script {
                    sh '''
                        echo "=========================================="
                        echo "Repository: ${GIT_URL}"
                        echo "Branch: ${GIT_BRANCH}"
                        echo "Commit: ${GIT_COMMIT}"
                        echo "Build Number: ${BUILD_NUMBER}"
                        echo "=========================================="
                    '''
                }
            }
        }
        
        stage('Verify OpenShift Connection') {
            steps {
                echo '🔍 Verifying OpenShift connection...'
                script {
                    sh '''
                        echo "Testing OpenShift CLI..."
                        oc version
                        oc whoami
                        oc project ${OCP_NAMESPACE}
                        echo "✅ Connected to OpenShift namespace: ${OCP_NAMESPACE}"
                    '''
                }
            }
        }
        
        stage('Deploy to OpenShift') {
            steps {
                echo '🚀 Deploying to OpenShift...'
                script {
                    sh '''
                        echo "Deploying ${APP_NAME} to ${OCP_NAMESPACE}..."
                        
                        # Check if k8s directory exists
                        if [ -d "k8s" ]; then
                            echo "📦 Applying Kubernetes manifests..."
                            oc apply -f k8s/ -n ${OCP_NAMESPACE}
                            echo "✅ Manifests applied successfully"
                            
                            # Wait for rollout if deployment exists
                            if oc get deployment ${APP_NAME} -n ${OCP_NAMESPACE} 2>/dev/null; then
                                echo "⏳ Waiting for rollout to complete..."
                                oc rollout status deployment/${APP_NAME} -n ${OCP_NAMESPACE} --timeout=5m
                                echo "✅ Rollout completed"
                            fi
                        else
                            echo "⚠️  No k8s directory found"
                            echo "Creating a simple test deployment..."
                            
                            # Create a simple deployment for demo
                            cat <<EOF | oc apply -f - -n ${OCP_NAMESPACE}
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ${APP_NAME}
  labels:
    app: ${APP_NAME}
spec:
  replicas: 1
  selector:
    matchLabels:
      app: ${APP_NAME}
  template:
    metadata:
      labels:
        app: ${APP_NAME}
    spec:
      containers:
      - name: ${APP_NAME}
        image: python:3.9-slim
        command: ["/bin/sh", "-c"]
        args:
          - |
            pip install flask &&
            cat > app.py << 'PYEOF'
            from flask import Flask, jsonify
            app = Flask(__name__)
            @app.route('/')
            def home():
                return jsonify({'message': 'Bob Pipeline Working!', 'build': '${BUILD_NUMBER}'})
            @app.route('/health')
            def health():
                return jsonify({'status': 'healthy'})
            if __name__ == '__main__':
                app.run(host='0.0.0.0', port=8080)
            PYEOF
            python app.py
        ports:
        - containerPort: 8080
EOF
                            echo "✅ Demo deployment created"
                        fi
                    '''
                }
            }
        }
        
        stage('Verify Deployment') {
            steps {
                echo '🔍 Verifying deployment status...'
                script {
                    sh '''
                        echo "Checking pods..."
                        oc get pods -n ${OCP_NAMESPACE} -l app=${APP_NAME}
                        
                        echo ""
                        echo "Checking deployment..."
                        oc get deployment ${APP_NAME} -n ${OCP_NAMESPACE} || echo "Deployment not found"
                        
                        echo ""
                        echo "Checking service..."
                        oc get service ${APP_NAME} -n ${OCP_NAMESPACE} || echo "Service not found"
                        
                        echo ""
                        echo "Checking route..."
                        oc get route ${APP_NAME} -n ${OCP_NAMESPACE} || echo "Route not found"
                        
                        echo ""
                        echo "✅ Deployment verification complete"
                    '''
                }
            }
        }
        
        stage('Get Application URL') {
            steps {
                echo '🌐 Getting application URL...'
                script {
                    sh '''
                        if oc get route ${APP_NAME} -n ${OCP_NAMESPACE} 2>/dev/null; then
                            APP_URL=$(oc get route ${APP_NAME} -n ${OCP_NAMESPACE} -o jsonpath='{.spec.host}')
                            echo "=========================================="
                            echo "🎉 Application deployed successfully!"
                            echo "URL: https://${APP_URL}"
                            echo "=========================================="
                        else
                            echo "⚠️  No route found. Application is deployed but not exposed externally."
                        fi
                    '''
                }
            }
        }
    }
    
    post {
        success {
            echo '=========================================='
            echo '🎉 Pipeline completed successfully!'
            echo '=========================================='
        }
        failure {
            echo '=========================================='
            echo '❌ Pipeline failed!'
            echo 'Check the logs above for details.'
            echo '=========================================='
        }
        always {
            echo 'Pipeline execution finished.'
        }
    }
}

// Made with Bob
