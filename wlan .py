
import time

# Create a dictionary to store user credentials
users = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3"
}

# Define the login function
def login():
    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if the username exists in the dictionary and the password is correct
        if username in users and users[username] == password:
            print("Login successful!")
            # Add code here to grant access to the Wi-Fi network
            break
        else:
            print("Invalid username or password. Please try again.")
            time.sleep(1)

# Call the login function
login()
