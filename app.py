from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL connection details (update these with your own details)
db_config = {
    'host': 'localhost',       # MySQL server address
    'user': 'root',            # MySQL username
    'password': 'Chinnu@123',  # MySQL password
    'database': 'upi-payments-method'  # Database name
}

# Function to check user credentials from MySQL database
def check_user_credentials(email, password):
    # Connect to MySQL database
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()

    # Query to find user by email and password
    cursor.execute("SELECT * FROM user WHERE EMAILID = %s AND USERPASSWORD = %s", (email, password))
    user = cursor.fetchone()  # Fetch the first matching user

    conn.close()
    
    # Return the user if credentials are correct, otherwise None
    return user

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form['email']
        password = request.form['password']
        
        # Check credentials in the database
        user = check_user_credentials(email, password)
        
        if user:
            # If user is found, redirect to user home page
            return redirect(url_for('user_home'))  
        else:
            # If credentials are incorrect, show the error message
            return render_template("login.html", error="You entered an incorrect email or password.")
    
    # Default GET request to render the login form
    return render_template("login.html")
@app.route("/createAccount", methods=["GET", "POST"])
def createAccount():
    if request.method == "POST":
        # Correct the field names to match the HTML input names
        first_name = request.form['first-name']  # Get first name
        last_name = request.form['last-name']    # Get last name
        email = request.form['email']
        phone_number = request.form['phone_number']
        address = request.form['address']
        zip_code = request.form['zipcode']
        password = request.form['password']
        confirm_password = request.form['confirm-password']

        # Check if passwords match
        if password != confirm_password:
            return render_template("createAccount.html", error="Passwords do not match!")

        # Hash the password (for security purposes)
        # You can implement your own hashing logic or use a package like bcrypt or werkzeug
        hashed_password = password

        # Insert the user into the database
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Query to insert user data
        cursor.execute("""
            INSERT INTO user (FIRSTNAME, LASTNAME, EMAILID, PHONENUMBER, USERADDRESS, ZIPCODE, USERPASSWORD)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (first_name, last_name, email, phone_number, address, zip_code, hashed_password))

        conn.commit()
        conn.close()

        # Redirect to login page after successful registration
        return redirect(url_for('login'))

    return render_template("createAccount.html")


@app.route("/user_home")
def user_home():
    return render_template("user_home.html")

@app.route("/transactions")
def transactions():
    print("transactions route is being accessed")  # Debugging message
    return render_template("transactions.html")

@app.route("/cards")
def cards():
    print("cards route is being accessed")  # Debugging message
    return render_template("cards.html")

@app.route("/kyc")
def kyc():
    print("KYC route is being accessed")  # Debugging message
    return render_template("kyc.html")

@app.route("/profile")
def profile():
    print("profile route is being accessed")  # Debugging message
    return render_template("profile.html")

if __name__ == "__main__":
    app.run(debug=True)
