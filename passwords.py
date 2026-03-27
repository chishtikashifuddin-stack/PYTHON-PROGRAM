a = input("set your name:")
f = input("Entre your user id:")
if f==a:
    a = input("Set password:")
    d = input("Check the password:")
    if d==a:print("login successfully")
    else:print("password is incorrect")        
else:print("user id is incorect")