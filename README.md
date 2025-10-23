# 🎓 University Management System

A full-stack web application for managing university data — including students, faculty, departments, courses, classrooms, and more.

---

## 🧩 Tech Stack

**Frontend:** React  
**Backend:** Flask (Python)  
**Database:** MySQL  
**API Communication:** Axios (RESTful API)  

---

## 📁 Project Structure

```
university-management-system/
│
├── backend/                  # Flask + MySQL backend
│   ├── app.py                # Flask entry point
│   ├── config/               # Database config files
│   ├── models/               # ORM / database models
│   ├── routes/               # API endpoints
│   ├── controllers/          # Business logic for CRUD
│   ├── utils/                # Helper functions
│   ├── requirements.txt      # Python dependencies
│   └── .env                  # Environment variables
│
├── frontend/                 # React frontend
│   ├── public/
│   │   └── index.html
│   └── src/
│       ├── api/              # Axios API configuration
│       ├── components/       # Reusable UI components
│       ├── pages/            # Page-level React components
│       ├── styles/           # CSS files
│       ├── App.jsx
│       ├── App.css
│       └── index.js
│
├── database/
│   ├── university_schema.sql # SQL file to create all tables
│   └── seed_data.sql         # Optional initial data
│
└── README.md
```

---

## ⚙️ Backend Setup (Flask + MySQL)

### 1️⃣ Create a virtual environment

```bash
cd backend
python -m venv venv
source venv/bin/activate       # On Linux/Mac
venv\Scripts\activate        # On Windows
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure environment variables

Create a file named `.env` inside the `backend` folder:

```bash
FLASK_ENV=development
FLASK_RUN_PORT=5000
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=yourpassword
DB_NAME=university_db
CORS_ORIGINS=http://localhost:3000
```

### 4️⃣ Run the backend

```bash
flask run
```

Your backend should now be live at  
👉 **http://127.0.0.1:5000**

---

## 💻 Frontend Setup (React)

### 1️⃣ Navigate to frontend

```bash
cd frontend
```

### 2️⃣ Install dependencies

```bash
npm install
```

### 3️⃣ Create a `.env` file

In the `frontend` folder:

```bash
REACT_APP_API_URL=http://127.0.0.1:5000/api
```

### 4️⃣ Run the frontend

```bash
npm start
```

Now your app should be available at  
👉 **http://localhost:3000**

---

## 🔗 API Integration

All API calls are defined in **`src/api/api.js`**

Example:
```js
import API from './api';

export const getStudents = () => API.get('/students');
```

---

## 🧠 Features

✅ Manage Universities, Departments, Students, Faculty, and Courses  
✅ CRUD operations with MySQL integration  
✅ Responsive and modern dashboard UI  
✅ Data tables with search, filter, and sort  
✅ Reusable components (Navbar, Sidebar, Table, Form)  
✅ RESTful API with Flask backend  
✅ Environment-based configuration

---

## 🗃️ Database Schema

**Main Entities:**
- University
- Department
- Faculty
- Student
- Course
- Subject
- Classroom
- Enrolled_In
- Scheduled_In

**Relationships:**
- A University has many Departments  
- A Department has many Faculty and Students  
- A Course belongs to a Department  
- Subjects are linked to Courses and Faculty  
- Enrolled_In connects Students and Courses  
- Scheduled_In connects Subjects and Classrooms  

---

## 🧪 Testing the Setup

Once both frontend and backend are running:
- Open http://localhost:3000 in your browser  
- The dashboard should load and interact with your Flask APIs  

To test API directly, visit:
```
http://127.0.0.1:5000/api/students
```

---

## 📦 Example Requirements (Python)

Example `requirements.txt`:
```
Flask
Flask-Cors
mysql-connector-python
python-dotenv
```

---

## 🚀 Future Improvements

- User authentication (Admin / Faculty / Student)
- File upload (student documents, images)
- Pagination and advanced filtering
- Role-based access control
- Charts and analytics dashboard

---

## 👨‍💻 Author

**Developed by:** Mohith T, Murthy Narasimhulu  
**Project:** University Management System  
**Tech Stack:** React + Flask + MySQL  

---

> 🧾 *This project serves as a complete full-stack implementation for managing university entities efficiently and securely.*
