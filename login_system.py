attempt = ["test", "hello", "admin123"]
for i in range(3):
    passsword = input("Enter your password: ")
    if passsword in attempt:
        print("Login successful")
        break
    else:
        print("Invalid")