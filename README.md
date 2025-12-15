# GenAI-Text-Summarizer-on-AWS-EKS-Docker-GitHub-
GenAI Text Summarizer on AWS EKS (Docker + GitHub)

genai-eks-app/
│
├── app/
│   ├── main.py          # FastAPI app
│   └── summarizer.py    # GenAI logic
│
├── Dockerfile
├── requirements.txt
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── README.md
uvicorn app.main:app --reload
docker build -t genai-app .
docker run -p 8000:8000 genai-app
Step 3: Push Image to Amazon ECR
Create ECR repo
aws ecr create-repository --repository-name genai-eks-app

Login & push
aws ecr get-login-password --region us-east-1 \
| docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com

docker tag genai-app:latest <ECR_URI>:latest
docker push <ECR_URI>:latest

☸️ Step 4: Create EKS Cluster

Simplest way (recommended):

eksctl create cluster \
--name genai-cluster \
--region us-east-1 \
--nodegroup-name genai-nodes \
--node-type t3.small \
--nodes 2


Configure kubectl:

aws eks update-kubeconfig --name genai-cluster --region us-east-1

..........
Apply:

kubectl apply -f k8s/


Get public URL:

kubectl get svc genai-service
..............
Step 6: Test GenAI API
curl -X POST http://<EXTERNAL-IP>/summarize \
-H "Content-Type: application/json" \
-d '{"text":"Generative AI is transforming software development..."}'

📤 Step 7: Push Project to GitHub
git init
git add .
git commit -m "GenAI app deployed on AWS EKS"
git branch -M main
git remote add origin https://github.com/<your-username>/genai-eks-app.git
git push -u origin main

