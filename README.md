# Student Enrollment and Management System

This project is a simple Flask-based application for managing student enrollments. It allows users to log in, view a list of students, and add new students to the database.

## Prerequisites

Before running the application, ensure you have the following installed on your system:

- **Python 3.x**  
  Download and install Python from [here](https://www.python.org/downloads/).

- **MySQL**  
  Download and install MySQL from [here](https://dev.mysql.com/downloads/installer/).



## Setup and Installation

### 1. **Clone or Download this repository**

### 2. **Install Dependencies**

In your terminal or command prompt, navigate to the project folder and install the necessary Python packages:

```bash
pip install flask
```
```bash
pip install flask mysql-connector-python
```
### 3. **Fire up MySQL, create the databases and tables.**
```bash
-- Create the database
CREATE DATABASE student_management;

-- Switch to the newly created database
USE student_management;

-- Table for Students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL
);

-- Table for Admin Users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Insert a test admin user
INSERT INTO users (username, password) VALUES ('admin', 'admin123');

```

### 4. **Update MySQL Credentials in `app.py`**
After setting up the database, make sure to update your MySQL credentials in app.py. 
Find this block of code in app.py and modify the values for user and password to match your MySQL setup:
```bash
db = mysql.connector.connect(
    host="localhost",
    user="your_mysql_user",  # Replace with your MySQL username
    password="your_mysql_password",  # Replace with your MySQL password
    database="student_management"
)
```

### 5. **Run the Application**
Navigate to your project folder and start the Flask server byexecute the command below in a terminal:
```bash
python app.py
```
This application will run at [http://127.0.0.1:5000/](http://127.0.0.1:5000/)
