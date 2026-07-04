# 🎓 Python MySQL Student Management System

A command-line Student Management System built using Python and MySQL.

This project demonstrates Object-Oriented Programming (OOP), MySQL database connectivity, CRUD operations, environment variable management, and exception handling following beginner-to-intermediate development practices.

---

## 🚀 Features

- Add new students
- View all student records
- Update existing student information
- Delete student records
- MySQL database integration
- Environment variable support using `.env`
- Input validation and error handling
- Duplicate student prevention
- Menu-driven command-line interface

---

## 🛠️ Technologies Used

- Python 3
- MySQL
- mysql-connector-python
- python-dotenv
- Git & GitHub

---

## 📚 Concepts Covered

This project helped me practice:

### Python Fundamentals
- Classes and Objects
- Constructors (`__init__`)
- Methods
- Exception Handling
- Loops and Conditional Statements
- Functions

### Database Concepts
- Database Connection
- Table Creation
- SQL Queries
- CRUD Operations
- Transactions (`commit` & `rollback`)
- Primary Keys
- Unique Constraints

### Environment Management
- Virtual Environment (`venv`)
- Environment Variables (`.env`)
- Dependency Management (`requirements.txt`)

### Version Control
- Git Basics
- GitHub Repository Management
- `.gitignore` Configuration

---

## 📂 Project Structure

```text
mysql-student-management/
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
└── venv/
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/Shivanshusaini/python-mysql-student-management.git
```

Move into the project directory:

```bash
cd python-mysql-student-management
```

---

### Create Virtual Environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Linux/Mac:

```bash
python3 -m venv venv
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file:

```env
Db_password=YOUR_MYSQL_PASSWORD
```

Example:

```env
Db_password=mypassword123
```

---

## 🗄️ MySQL Database Setup

Create a database:

```sql
CREATE DATABASE python_test_db;
```

The application will automatically create the `STUDENT` table if it does not exist.

---

## ▶️ Running the Application

```bash
python app.py
```

---

## 📸 Sample Menu

```text
===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. Show Students
3. Update Student
4. Delete Student
5. Exit
```

---

## 📝 Example Output

```text
Database Connected Successfully!

===== STUDENT MANAGEMENT SYSTEM =====

1. Add Student
2. Show Students
3. Update Student
4. Delete Student
5. Exit

Enter Choice: 1

Enter Name: Shivanshu
Enter Age: 23

Student Inserted Successfully!
```

---

## 🔮 Future Improvements

- Search Student by ID
- Pagination Support
- Logging System
- Unit Testing
- Modular Project Structure
- REST API using Flask/Django
- Docker Support
- Admin Authentication

---

## 👨‍💻 Author

**Shivanshu Saini**

MCA Student | Python Developer

GitHub:
https://github.com/Shivanshusaini

---

## ⭐ Learning Outcome

This project helped me understand:

- Python OOP in real-world applications
- MySQL integration with Python
- Environment variable management
- Exception handling techniques
- Git and GitHub workflows
- Professional project organization
