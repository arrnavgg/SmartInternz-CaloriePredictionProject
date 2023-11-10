from flask import Flask, render_template, request, redirect, url_for, flash, session
import sqlite3
import os

app = Flask(__name__)
app.config['DATABASE'] = 'Calorie.db'
app.secret_key = 'TH15_1S_@_S3CR3T_K3Y'

@app.route('/login',methods=("GET","POST"))
def login():
    pass

from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = 'Calorie.db'
app.secret_key = 'TH15_1S_@_S3CR3T_K3Y'

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':

        # Get user input from the registration form
        userid = request.form['username']
        password = request.form['password']
        name = request.form['name']

        # Connect to the SQLite database
        with sqlite3.connect(app.config['DATABASE']) as conn:
            cursor = conn.cursor()

            # Check if the user already exists
            cursor.execute("SELECT userid FROM users WHERE userid=?", (userid,))
            existing_user = cursor.fetchone()

            if existing_user:
                # User already exists, render the registration form with an error message
                flash("User already exists. Please choose a different username.")
                return render_template('register.html')

            # Insert the new user
            cursor.execute("INSERT INTO users (userid, password, name) VALUES (?, ?, ?)",
                           (userid, password, name))

        flash("Registration successful. You can now log in.")
        return redirect(url_for('login'))  # Redirect to the login page after registration

    return render_template('register.html')  # Render the registration form template

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')

@app.route('/dashboard',methods=("GET","POST"))
def dashboard():
    pass

@app.route('/home',methods=("GET","POST"))
def home():
    pass


# Below we can just redirect it to the login page directly, or can display a
# Homepage with dev info/project info and login button.

@app.route('/')
def index():
    return render_template('base.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)