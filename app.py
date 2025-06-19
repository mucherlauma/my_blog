from flask import Flask, render_template, request, redirect
import mysql.connector

app = Flask(__name__)

# Database connection function
def get_connection():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='',  # Use your MySQL password if set
        database='portfolio_db'
    )

@app.route('/')
def index():
    return render_template('protofolio.html')

@app.route('/contact', methods=['POST'])
def contact():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO contact_messages (first_name, last_name, email, phone, message)
        VALUES (%s, %s, %s, %s, %s)
    ''', (first_name, last_name, email, phone, message))
    conn.commit()
    conn.close()

    return redirect('/thank-you')

@app.route('/thank-you')
def thank_you():
    return "<h2>Thank you for contacting me!</h2><a href='/'>Go Back to Home</a>"

if __name__ == '__main__':
    app.run(debug=True)
