# Kontroll av inloggningsförsök

password = "lösenord123"
login_attemts = 0

username = input("Username: ")

while True:

    if len(username) < 1:
        print("Incorrect username!")
        username = input("New attempt. Username: ")
        continue
    
    if login_attemts >= 5:
        print("Too many attempts. Locked out from account.")        
        break
    password_input = input("Password: ")
    
    if len(password_input) < 8 or password_input != password:
        print("Incorrect password! Try again.")
        login_attemts = login_attemts + 1
        continue
    print("Correct password! You are now logged in.")
    break
    