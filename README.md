# O-1A Visa Assessment API

##  How to Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/o1a-assessment.git
cd o1a-assessment

uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

### Once the server is running, visit:
http://127.0.0.1:8000/docs#/default/evaluate_cv_evaluate_cv_post
