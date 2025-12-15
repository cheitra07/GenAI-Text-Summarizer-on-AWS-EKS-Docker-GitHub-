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
....................................
method 2:


# PHASE 1: Bring GitHub Repo to VS Code (Local)

### 1️⃣ Copy your GitHub repo URL

Example:

```
https://github.com/your-username/genai-eks-app.git
```

### 2️⃣ Open VS Code

* Open VS Code
* Press **Ctrl + `** (open terminal)

### 3️⃣ Clone repo locally

```bash
git clone https://github.com/your-username/genai-eks-app.git
cd genai-eks-app
```

✅ Now your GitHub project is **on your local system**

---

### 4️⃣ Open folder in VS Code

```bash
code .
```

Your project folder opens in VS Code 🎉

---

# PHASE 2: Create Project Files in VS Code

Inside VS Code, create these files:

```
genai-eks-app/
│
├── app/
│   ├── main.py
│   └── summarizer.py
│
├── Dockerfile
├── requirements.txt
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── README.md
```

(Use **Right click → New File / New Folder**)

---

# PHASE 3: Run the App Locally (Before Docker)

### 1️⃣ Create Python virtual environment

```bash
python -m venv venv
```

Activate:

* **Windows**

```bash
venv\Scripts\activate
```

* **Linux/Mac**

```bash
source venv/bin/activate
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run FastAPI locally

```bash
uvicorn app.main:app --reload
```

Open browser:

```
http://127.0.0.1:8000/docs
```

✔ Test `/summarize` endpoint
✔ This confirms your code works

---

# PHASE 4: Create Docker Image (Locally)

### 1️⃣ Make sure Docker is running

Check:

```bash
docker --version
```

---

### 2️⃣ Build Docker image

```bash
docker build -t genai-app .
```

---

### 3️⃣ Run Docker container

```bash
docker run -p 8000:8000 genai-app
```

Test again:

```
http://localhost:8000/docs
```

✔ If this works → Docker part is DONE

---

# PHASE 5: Push Code Changes Back to GitHub

```bash
git status
git add .
git commit -m "Initial GenAI FastAPI app with Docker"
git push origin main
```

Now GitHub has **working code + Dockerfile** 💪

---

# PHASE 6: Create AWS Services (Very Important Order)

## 1️⃣ Install & Configure AWS CLI

```bash
aws configure
```

Enter:

* Access Key
* Secret Key
* Region (example: `us-east-1`)
* Output format: `json`

---

## 2️⃣ Create Amazon ECR (Docker Registry)

```bash
aws ecr create-repository \
--repository-name genai-eks-app \
--region us-east-1
```

Copy **repositoryUri** (you’ll need it).

---

## 3️⃣ Login Docker to ECR

```bash
aws ecr get-login-password --region us-east-1 \
| docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

---

## 4️⃣ Tag & Push Docker Image

```bash
docker tag genai-app:latest <ECR_URI>:latest
docker push <ECR_URI>:latest
```

✔ Your image is now in AWS

---

# PHASE 7: Create EKS Cluster (Simplest Way)

### Install eksctl (once)

* Windows: download from GitHub releases
* Linux/Mac:

```bash
brew install eksctl
```

---

### Create EKS cluster

```bash
eksctl create cluster \
--name genai-cluster \
--region us-east-1 \
--nodegroup-name genai-nodes \
--node-type t3.small \
--nodes 2
```

⏳ Takes ~15 minutes

---

### Configure kubectl

```bash
aws eks update-kubeconfig \
--name genai-cluster \
--region us-east-1
```

Verify:

```bash
kubectl get nodes
```

---

# PHASE 8: Deploy App to EKS

### 1️⃣ Update image in `deployment.yaml`

Replace:

```yaml
image: <ECR_URI>:latest
```

---

### 2️⃣ Deploy to Kubernetes

```bash
kubectl apply -f k8s/
```

---

### 3️⃣ Get Public URL

```bash
kubectl get svc genai-service
```

Copy **EXTERNAL-IP**

---

### 4️⃣ Test from browser or curl

```bash
http://<EXTERNAL-IP>/docs
```

🎉 **GenAI app running on AWS EKS**

---

# PHASE 9: Clean Up (IMPORTANT – Avoid Cost)

When done:

```bash
eksctl delete cluster --name genai-cluster --region us-east-1
aws ecr delete-repository --repository-name genai-eks-app --force
```

---



