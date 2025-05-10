# Student Enrollment and Management System

This project is a simple Flask-based web application for managing student enrollments. It allows an admin to log in, view, add, edit, and delete student records, including their enrolled programs, in a MySQL database. The application features a clean, responsive frontend built with Bootstrap and a lightweight Flask backend.

## Features
- **Admin Login**: Secure login for administrators using a username and password.

- **Student Management** : View, add, edit, and delete student records with details like first name, last name, email, parent name, mobile number, address, birthplace, branch, date of birth, gender, enrollment date, and program enrollment.

- **Program Enrollment** : Assign students to academic programs (e.g., CS101 (Computer Science)) via a dropdown menu.

- **Responsive UI** : Built with Bootstrap for a modern, mobile-friendly interface.

- **MySQL Integration** : Stores student, user, program, and enrollment data in a MySQL database.




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

-- Table for Programs
CREATE TABLE programs (
    program_id INT AUTO_INCREMENT PRIMARY KEY,
    program_name VARCHAR(100) NOT NULL,
    program_code VARCHAR(10) UNIQUE NOT NULL
);

-- Table for Students
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    parent_name VARCHAR(100),
    mobile_number VARCHAR(15),
    address VARCHAR(255),
    birthplace VARCHAR(100),
    branch VARCHAR(50),
    date_of_birth DATE,
    gender ENUM('Male', 'Female', 'Other'),
    enrollment_date DATE
);

-- Table for Enrollments
CREATE TABLE enrollments (
    enrollment_id INT AUTO_INCREMENT PRIMARY KEY,
    student_id INT,
    program_id INT,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON DELETE CASCADE,
    FOREIGN KEY (program_id) REFERENCES programs(program_id)
);

-- Table for Admin Users
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password VARCHAR(50) NOT NULL
);

-- Insert test data
INSERT INTO users (username, password) VALUES ('admin', 'admin123');
INSERT INTO programs (program_name, program_code) VALUES 
    ('Computer Science', 'CS101'),
    ('Electrical Engineering', 'EE201'),
    ('Information Science', 'IS301'),
    ('Electronics', 'EL401');

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
