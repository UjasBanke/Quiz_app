# 🧠 Django Quiz Platform — **Quiz404**

#🔗 https://quiz-app-8se2.onrender.com

**Quiz404** is a modern and interactive application that makes testing knowledge engaging and fun deployed on **Render**
It’s built with **Django** and designed for **students, educators, and quiz enthusiasts** who want instant results, progress tracking, and a smooth quiz-taking experience.  

---

## ✨ Key Features  

### 💁🏻‍♀️ For Users  
- 🎯 **Clean, user-friendly interface** – minimal and distraction-free.  
- 📝 **Multiple-choice questions (MCQs)** with one correct answer.  
- ⏳ **Built-in timer** – auto-submits answers if time runs out.  
- 📊 **Instant scoring** – see results right after completing a quiz.  
- 📜 **Attempt history** – review all past quiz attempts with scores and timestamps.  

### 🛠 For Admins  
- 🔑 **Secure login** for administrators.  
- 👥 **User management** – add, edit, delete, or bulk upload users via CSV.  
- 📚 **Quiz management** – create, edit, delete, and bulk upload quizzes.  
- ❓ **Question & option management** – define correct/wrong answers.  
- 📈 **Custom dashboard with analytics** – total users, quizzes, and attempts.  

---

## 🏗 Tech Stack  
- **Backend**: Django (Python)  
- **Frontend**: HTML, CSS, Bootstrap 5  
- **Database**: SQLite (default) – supports PostgreSQL/MySQL  
- **Authentication**: Django’s built-in authentication  


---

## 🚀 Getting Started  

### 1. Clone the repo  
```bash
git clone https://github.com/UjasBanke/Quiz_app.git
cd Quiz_app
```
### 2. Set up virtual environment & install dependencies  
```bash
# Create virtual environment
python -m venv venv

# Activate the virtual environment
# On Linux / macOS
source venv/bin/activate

# On Windows (Command Prompt)
venv\Scripts\activate

# On Windows (PowerShell)
venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```
### 3. Run database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```
### 4. Create an admin account
```bash
python manage.py createsuperuser
```
### 5. Start the server
```bash
python manage.py runserver
```

### 6. Visit the site
```bash
http://127.0.0.1:8000/
```

# Admin dashboard
http://127.0.0.1:8000/admin/dashboard/


or just....

**click on the link!** https://quiz-app-8se2.onrender.com

### Happy Learning!!
