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
http://54.9:8000/docs
```



You’re doing very well — AWS console + SSH is confusing for everyone at first 💪
