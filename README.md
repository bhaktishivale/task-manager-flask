📝 Task Manager Web Application

A simple and user-friendly Task Manager web app built using Flask. This application allows users to manage their daily tasks efficiently with features like adding, updating, deleting, and marking tasks as completed.

## 🚀 Features
- ➕ Add new tasks with priority (High, Medium, Low)
- 📋 View all tasks in a clean UI
- ✏️ Update existing tasks
- ❌ Delete tasks
- ✅ Mark tasks as completed / undo completion
- 🎨 Responsive and modern UI using Bootstrap

## 🛠️ Tech Stack
- Frontend: HTML, CSS, Bootstrap  
- Backend: Python (Flask)  
- Database: SQLite  
- ORM: SQLAlchemy  

## 📂 Project Structure
task_manager/
│── app.py  
│── models.py  
│── tasks.db  
│── templates/  
│     ├── index.html  
│     ├── add.html  
│     └── update.html  
│── static/ (optional)

## ⚙️ Installation & Setup
1. Clone the repository:  
   git clone https://github.com/bhaktishivale/task-manager-flask.git  
2. Navigate to the project folder:  
   cd task-manager-flask  
3. Install dependencies:  
   pip install flask flask_sqlalchemy flask_migrate  
4. Run the application:  
   python app.py  
5. Open in browser:  
   http://127.0.0.1:5000

## 🧠 How It Works
Tasks are stored in a SQLite database. Flask handles routing and backend logic. SQLAlchemy manages database operations. Jinja templates render dynamic data in HTML.

## 📸 Screenshots
Add screenshots of your project here.

## 📌 Future Improvements
- 🔐 User authentication (Login/Signup)  
- 📅 Add due dates and reminders  
- 🔍 Search and filter tasks  
- 🌐 Deploy the app online  

## 🙌 Acknowledgement
This project was built as part of learning full-stack web development using Flask.

## 📎 Author
Bhakti shivale  
GitHub: https://github.com/bhaktishivale
