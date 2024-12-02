from flask import Flask, render_template, request, redirect, url_for, session, flash
import mysql.connector
from flask_session import Session

app = Flask(__name__)

# Set up session configuration
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your-secret-key'  # Secure the session
Session(app)

# MySQL connection details
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Chinnu@123',
    'database': 'upi-payments-method'
}

def check_user_credentials(email, password):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE EMAILID = %s AND USERPASSWORD = %s", (email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def get_user_details(user_id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM user WHERE USERID = %s", (user_id,))
    user = cursor.fetchone()
    conn.close()
    return user

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        user = check_user_credentials(email, password)
        if user:
            session['user_id'] = user[0]
            return redirect(url_for('user_home'))
        else:
            flash("You entered an incorrect email or password.", "danger")
            return render_template("login.html")
    return render_template("login.html")

@app.route("/createAccount", methods=["GET", "POST"])
def createAccount():
    if request.method == "POST":
        first_name = request.form['first-name']
        last_name = request.form['last-name']
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']
        zip_code = request.form['zipcode']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return render_template("createAccount.html")

        hashed_password = password
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO user (FIRSTNAME, LASTNAME, EMAILID, PHONENUMBER, USERADDRESS, ZIPCODE, USERPASSWORD)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email, phone_number, address, zip_code, hashed_password))
        conn.commit()
        conn.close()
        flash("Account created successfully! Please log in.", "success")
        return redirect(url_for('login'))
    return render_template("createAccount.html")

@app.route("/user_home")
def user_home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    user = get_user_details(user_id)
    if user:
        return render_template("user_home.html", user=user)
    else:
        return redirect(url_for('login'))
@app.route("/transactions")
def transactions():
    if 'user_id' not in session:
        return redirect(url_for('login'))  # Ensure the user is logged in

    user_id = session.get('user_id')

    # Check if KYC is done
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT IS_KYC_DONE FROM user WHERE USERID = %s", (user_id,))
    result = cursor.fetchone()
    connection.close()

    if result and result[0]:  # IS_KYC_DONE is True
        return render_template("transactions.html")
    else:
        flash("Please complete your KYC to access UPI payments.", "warning")
        return redirect(url_for('kyc_form'))


@app.route("/cards")
def cards():
    return render_template("cards.html")

@app.route('/kyc', methods=['GET', 'POST'])
def kyc():
    if request.method == 'POST':
        govt_id = request.form.get('govt-id')
        first_name = request.form.get('first-name')
        last_name = request.form.get('last-name')
        dob = request.form.get('dob')
        nationality = request.form.get('nationality')
        gender = request.form.get('gender')

        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()

            # Insert data into KYC table
            query = """
                INSERT INTO KYC (GOVTID, FIRSTNAME, LASTNAME, DOB, NATIONALITY, GENDER)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(query, (govt_id, first_name, last_name, dob, nationality, gender))

            # Update user's KYC status in the user table
            user_id = session.get('user_id')  # Retrieve logged-in user ID from session
            if user_id:
                update_query = "UPDATE user SET IS_KYC_DONE = TRUE WHERE USERID = %s"
                cursor.execute(update_query, (user_id,))
            
            connection.commit()

            flash("KYC submission successful!", "success")
        except mysql.connector.Error as err:
            flash(f"Error: {err}", "danger")
        finally:
            cursor.close()
            connection.close()

        return redirect(url_for('kyc_form'))

    return render_template('kyc.html')


@app.route("/profile")
def profile():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    user_id = session['user_id']
    user = get_user_details(user_id)
    if user:
        return render_template("profile.html", user=user)
    else:
        return redirect(url_for('login'))

if __name__ == "__main__":
    app.run(debug=True)
