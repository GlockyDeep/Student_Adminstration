from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector

app = Flask(__name__)
app.secret_key = 'no'  # Replace with a secure key in production

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
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template('students.html', students=students)

# Students - Add
@app.route('/students/add', methods=['POST'])
def add_student():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    cursor.execute(
        "INSERT INTO students (first_name, last_name, email) VALUES (%s, %s, %s)",
        (first_name, last_name, email)
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