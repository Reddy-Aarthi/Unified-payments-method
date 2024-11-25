from flask import Flask, render_template, request, jsonify, redirect, url_for
import mysql.connector

app = Flask(__name__)

# Database Connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Chinnu@123",
    database="upi-payments-method"
)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM USER WHERE EmailId=%s AND UserPassword=%s", (email, password))
        user = cursor.fetchone()

        if user:
            return redirect(url_for('user_home', user_id=user['UserId']))
        else:
            return render_template('login.html', error="Invalid credentials")

    return render_template('login.html')

@app.route('/user/home/<int:user_id>')
def user_home(user_id):
    return render_template('user_home.html', user_id=user_id)

@app.route('/user/profile/<int:user_id>')
def profile(user_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM USER WHERE UserId=%s", (user_id,))
    user = cursor.fetchone()
    return render_template('profile.html', user=user)

@app.route('/user/kyc/<int:user_id>')
def kyc(user_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT k.* FROM KYC k
        JOIN bankaccount b ON k.GovtId = b.GovtId
        JOIN USER u ON b.AccountNumber = u.UserId
        WHERE u.UserId = %s
    """, (user_id,))
    kyc_data = cursor.fetchone()
    return render_template('kyc.html', kyc=kyc_data)

@app.route('/user/transactions/<int:user_id>')
def transactions(user_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT t.* FROM Transactions t
        JOIN BANKATMCARD c ON t.CardNumber = c.CardNumber
        JOIN bankaccount b ON c.AccountNumber = b.AccountNumber
        WHERE b.GovtId = %s
    """, (user_id,))
    transactions = cursor.fetchall()
    return render_template('transactions.html', transactions=transactions)

@app.route('/user/cards/<int:user_id>')
def cards(user_id):
    cursor = db.cursor(dictionary=True)
    cursor.execute("""
        SELECT c.* FROM BANKATMCARD c
        JOIN bankaccount b ON c.AccountNumber = b.AccountNumber
        WHERE b.GovtId = %s
    """, (user_id,))
    cards = cursor.fetchall()
    return render_template('cards.html', cards=cards)

if __name__ == '__main__':
    app.run(debug=True)
