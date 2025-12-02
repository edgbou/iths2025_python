user_credentials = {"user1": "Welcome123", "user2": "qwerty!", "user3": "Password2025"}

password_list = ["123456", "password", "Welcome123", "letmein", "Password2025"]
for user in user_credentials.items():
    current_user = user[0]
    user_pass = user[1]
    for password in password_list:
        # if user_pass == password:
        #     print(f"{current_user}: {password} -> successful")
        #     file = open("password_spray_results.txt", "a")
        #     file.write(f"{current_user}: {password} -> successful\n")
        #     file.close()
        # else:
        #     print(f"{current_user}: {password} -> failed")
        #     file = open("password_spray_results.txt", "a")
        #     file.write(f"{current_user}: {password} -> failed\n")
        #     file.close()

        # KOMPRIMERAD KOD NEDAN:
        succesORfailedtext = "Failed"
        if user_pass == password:
            succesORfailedtext = "Successful"

        print(f"{current_user}: {password} -> {succesORfailedtext}")
        file = open("password_spray_results.txt", "a")
        file.write(f"{current_user}: {password} -> {succesORfailedtext}\n")
        file.close()
            