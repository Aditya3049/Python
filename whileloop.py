secret_code=1234
code=int(input("enter your sceret code : \n"))
while code != secret_code:
    code=int(input("Sorry ,incorrect password Re-enter again : \n"))
print("You have entered the correct password!!!")    