```
How to run

Enable Kubernetes in Docker Desktop - go to settings - Kubernetes - enable

Change dir to the project dir

1. Run Docker Desktop with Kubernetes enabled 
2. docker build -t simple-api .
3. kubectl apply -k k8s
4. kubectl port-forward service/api-deployment-service 8000:80 -n api
5. Visit http://127.0.0.1:8000
```