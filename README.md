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
Great 👍
Since your **local app is now running with a small model**, the **next steps are exactly these 5 phases**.
Follow them **in order**, don’t skip anything.

---

# 🚀 NEXT STEPS: From Local → Docker → AWS ECR → EKS

---

## ✅ PHASE 1: Final Local Verification (2 minutes)

Run:

```bat
uvicorn app.main:app
```

Open:

```
http://127.0.0.1:8000/docs
```

✔ Test `/summarize`
✔ Confirm it works

👉 **Only continue if this works**

---

## 🐳 PHASE 2: Build Docker Image (Local)

### 1️⃣ Check Docker

```bat
docker --version
```

---

### 2️⃣ Build image

From project root:

```bat
docker build -t genai-eks-app .
```

---

### 3️⃣ Run container locally

```bat
docker run -p 8000:8000 genai-eks-app
```

Test again:

```
http://localhost:8000/docs
```

✔ If this works → Docker is DONE

---

## 📤 PHASE 3: Push Image to AWS ECR

### 1️⃣ Configure AWS CLI (once)

```bat
aws configure
```

---

### 2️⃣ Create ECR repository

```bat
aws ecr create-repository \
--repository-name genai-eks-app \
--region us-east-1
```

Copy:

```
repositoryUri
```

---

### 3️⃣ Login Docker to ECR

```bat
aws ecr get-login-password --region us-east-1 ^
| docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

---

### 4️⃣ Tag & push image

```bat
docker tag genai-eks-app:latest <ECR_URI>:latest
docker push <ECR_URI>:latest
```

✔ Image is now in AWS

---

## ☸️ PHASE 4: Create AWS EKS Cluster

### 1️⃣ Install eksctl (once)

* Download from GitHub (Windows)
* Verify:

```bat
eksctl version
```

---

### 2️⃣ Create cluster (15 mins)

```bat
eksctl create cluster ^
--name genai-cluster ^
--region us-east-1 ^
--nodegroup-name genai-nodes ^
--node-type t3.small ^
--nodes 2
```

---

### 3️⃣ Verify

```bat
aws eks update-kubeconfig --name genai-cluster --region us-east-1
kubectl get nodes
```

---

## ☸️ PHASE 5: Deploy App on EKS

### 1️⃣ Update image in `k8s/deployment.yaml`

```yaml
image: <ECR_URI>:latest
```

---

### 2️⃣ Deploy

```bat
kubectl apply -f k8s/
```

---

### 3️⃣ Get public URL

```bat
kubectl get svc genai-service
```

Copy:

```
EXTERNAL-IP
```

---

### 4️⃣ Test

```
http://<EXTERNAL-IP>/docs
```

🎉 **GenAI app LIVE on AWS EKS**

---

## 🧹 PHASE 6: CLEAN UP (CRITICAL – Avoid Bills)

After demo:

```bat
eksctl delete cluster --name genai-cluster --region us-east-1
aws ecr delete-repository --repository-name genai-eks-app --force
```

---

Great 👍
Since your **local app is now running with a small model**, the **next steps are exactly these 5 phases**.
Follow them **in order**, don’t skip anything.

---

# 🚀 NEXT STEPS: From Local → Docker → AWS ECR → EKS

---

## ✅ PHASE 1: Final Local Verification (2 minutes)

Run:

```bat
uvicorn app.main:app
```

Open:

```
http://127.0.0.1:8000/docs
```

✔ Test `/summarize`
✔ Confirm it works

👉 **Only continue if this works**

---

## 🐳 PHASE 2: Build Docker Image (Local)

### 1️⃣ Check Docker

```bat
docker --version
```

---

### 2️⃣ Build image

From project root:

```bat
docker build -t genai-eks-app .
```

---

### 3️⃣ Run container locally

```bat
docker run -p 8000:8000 genai-eks-app
```

Test again:

```
http://localhost:8000/docs
```

✔ If this works → Docker is DONE

---

## 📤 PHASE 3: Push Image to AWS ECR

### 1️⃣ Configure AWS CLI (once)

```bat
aws configure
```

---

### 2️⃣ Create ECR repository

```bat
aws ecr create-repository \
--repository-name genai-eks-app \
--region us-east-1
```

Copy:

```
repositoryUri
```

---

### 3️⃣ Login Docker to ECR

```bat
aws ecr get-login-password --region us-east-1 ^
| docker login --username AWS --password-stdin <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com
```

---

### 4️⃣ Tag & push image

```bat
docker tag genai-eks-app:latest <ECR_URI>:latest
docker push <ECR_URI>:latest
```

✔ Image is now in AWS

---

## ☸️ PHASE 4: Create AWS EKS Cluster

### 1️⃣ Install eksctl (once)

* Download from GitHub (Windows)
* Verify:

```bat
eksctl version
```

---

### 2️⃣ Create cluster (15 mins)

```bat
eksctl create cluster ^
--name genai-cluster ^
--region us-east-1 ^
--nodegroup-name genai-nodes ^
--node-type t3.small ^
--nodes 2
```

---

### 3️⃣ Verify

```bat
aws eks update-kubeconfig --name genai-cluster --region us-east-1
kubectl get nodes
```

---

## ☸️ PHASE 5: Deploy App on EKS

### 1️⃣ Update image in `k8s/deployment.yaml`

```yaml
image: <ECR_URI>:latest
```

---

### 2️⃣ Deploy

```bat
kubectl apply -f k8s/
```

---

### 3️⃣ Get public URL

```bat
kubectl get svc genai-service
```

Copy:

```
EXTERNAL-IP
```

---

### 4️⃣ Test

```
http://<EXTERNAL-IP>/docs
```

🎉 **GenAI app LIVE on AWS EKS**

---

## 🧹 PHASE 6: CLEAN UP (CRITICAL – Avoid Bills)

After demo:

```bat
eksctl delete cluster --name genai-cluster --region us-east-1
aws ecr delete-repository --repository-name genai-eks-app --force
```
AWS deployment in EC2 without docker


### ✔ Step 2: Continue EC2 setup (this is the right step now)

From:

```
[ec2-user@ip-172 ~]$
```

Run:

```bash
sudo dnf update -y
sudo dnf install python3 git -y
```

---

### ✔ Step 3: Clone your GitHub project

```bash
git clone https://github.com/YOUR_USERNAME/GenAI-Text-Summarizer.git
cd GenAI-Text-Summarizer
```

---

### ✔ Step 4: Setup & run app

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

### ✔ Step 5: Test from browser

Open on your laptop:

```
http://54.:8000/docs
```

(Only works if **security group port 8000** is open)

*************with out docker aws deloy to ec2

## ✅ WHAT YOU SHOULD DO NOW (Correct Path)

### ✔ Step 1: STOP trying SSH inside EC2

You already succeeded earlier.

Do **NOT** run:

```bash
ssh -i ...
```

from this prompt.

---

### ✔ Step 2: Continue EC2 setup (this is the right step now)

From:

```
[ec2-user@ip-126 ~]$
```

Run:

```bash
sudo dnf update -y
sudo dnf install python3 git -y
```

---

### ✔ Step 3: Clone your GitHub project

```bash
git clone https://github.com/YOUR_USERNAME/GenAI-Text-Summarizer.git
cd GenAI-Text-Summarizer
```

---

### ✔ Step 4: Setup & run app

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

---

### ✔ Step 5: Test from browser

Open on your laptop:

```
http://39:8000/docs
```











