from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'simple_secret_key'  # Replace with a secure key in production

# MySQL Configuration
db = mysql.connector.connect(
    host="localhost",
    user="root",  # Replace with your MySQL username
    password="2a84y90yrasifba2Asd",  # Replace with your MySQL password
    database="student_management"
)
cursor = db.cursor(dictionary=True)

# Login Route
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        user = cursor.fetchone()
        if user:
            session['user_id'] = user['user_id']
            return redirect(url_for('students'))
        flash('Invalid username or password')
    return render_template('login.html')

# Students - View
@app.route('/students')
def students():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    # Fetch students with their enrolled programs formatted as "code (name)"
    cursor.execute("""
        SELECT s.*, 
               GROUP_CONCAT(CONCAT(p.program_code, ' (', p.program_name, ')')) as programs
        FROM students s
        LEFT JOIN enrollments e ON s.student_id = e.student_id
        LEFT JOIN programs p ON e.program_id = p.program_id
        GROUP BY s.student_id
    """)
    students = cursor.fetchall()
    # Fetch all programs for the add student form
    cursor.execute("SELECT * FROM programs")
    programs = cursor.fetchall()
    return render_template('students.html', students=students, programs=programs)

# Students - Add
@app.route('/students/add', methods=['POST'])
def add_student():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']

    mobile_number = request.form.get('mobile_number')
    address = request.form.get('address')
    birthplace = request.form.get('birthplace')

    date_of_birth = request.form.get('date_of_birth')
    gender = request.form.get('gender')
    enrollment_date = request.form.get('enrollment_date')
    program_id = request.form.get('program_id')  # Selected program

    # Insert student
    cursor.execute(
        """
        INSERT INTO students (first_name, last_name, email, mobile_number, address, birthplace, date_of_birth, gender, enrollment_date)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
        (first_name, last_name, email, mobile_number, address, birthplace, date_of_birth or None, gender or None, enrollment_date or None)
    )
    db.commit()

    # Get the newly inserted student_id
    cursor.execute("SELECT LAST_INSERT_ID() as student_id")
    student_id = cursor.fetchone()['student_id']

    # Insert enrollment if a program is selected
    if program_id:
        cursor.execute(
            "INSERT INTO enrollments (student_id, program_id) VALUES (%s, %s)",
            (student_id, program_id)
        )
        db.commit()

    flash('Student added successfully')
    return redirect(url_for('students'))

# Logout
@app.route('/logout')
def logout():
    session.pop('user_id', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)