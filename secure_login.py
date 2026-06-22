import hashlib

users = {}

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        username = input("Username: ")
        password = input("Password: ")

        users[username] = hash_password(password)
        print("Registration Successful!")

    elif choice == "2":
        username = input("Username: ")
        password = input("Password: ")

        if username in users and users[username] == hash_password(password):
            print("Login Successful!")
        else:
            print("Invalid Username or Password!")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid Choice")