from flask import Flask, render_template, request
import sqlite3

conn = sqlite3.connect('logined_people.db')
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")
conn.commit()
conn.close()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('submit_form.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Get data from the form
    user_email = request.form['email']
    user_password = request.form['password']
    
    conn = sqlite3.connect('logined_people.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password) VALUES (?, ?)", (user_email, user_password))
    conn.commit()
    conn.close()
    

    conn = sqlite3.connect('logined_people.db')
    cursor = conn.cursor()
    
    cursor.execute('SELECT * FROM users')

    # Fetch all rows from the last executed statement
    rows = cursor.fetchall()

    # Iterate through the rows
    for row in rows:
        print(row)

    # Close the connection
    conn.close()


    # Do something with the data (e.g., store in a database, process it, etc.)
    return f"Email: {user_email}, Password: {user_password}"

if __name__ == '__main__':
    app.run(debug=True)
