from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Database to store user credentials
user_database = {}


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']

    # Check if the username exists in the database
    if username in user_database:
        stored_password = user_database[username]
        # Compare the entered password with the stored password
        if password == stored_password:
            return redirect('/success')
        else:
            return redirect('/failure')
    else:
        return redirect('/failure')


@app.route('/success')
def success():
    return 'Login successful!'


@app.route('/failure')
def failure():
    return 'Login failed!'


if __name__ == '__main__':
    app.run()

