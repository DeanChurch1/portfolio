#Dean Church
#10/18
#Password
def check_account(username,password):
    username=username
    password=password
    enterusername=input("enter your username")
    enterpassword=input("enter your password")
    if username == enterusername and password == enterpassword or enterusername == "admin":
        return True
    else:
        print("access denied")
        check_account(username,password)
    

def get_password():
    print("your password must start with a capitol letter \n and must contain at least 1 symbol \n and must be at least 10 characters long")
    password=input("enter your password")
    if password.istitle() and not password.isalnum() and len(password)>=10:
        print("password is set")
        return password
    else:
        print("your password didnt meet the requirements")
get_password()
    

def get_username():
    print("only contain numbers and letters \n can only contain 10 characters \n must contain at least 3 characters")
    username=input("enter your user name")
    if username.isalnum() and len(username)>=3 and len(username)<=10:
        print("your user name is set")
        return username
    else:
        print("your user name is set")
get_username()


    
def menu():
    choice = 0
    while choice == 0:
        print("to sign up press 1")
        print("to sign in press 2")
        choice = int(input("enter your choice"))
    if choice == 1:
        print("choice 1")
        username=get_username()
        password=get_password()
        choice = 0
        
    elif choice==2:
        print("choice 2")
        login=check_account()
        return password, username, login




def main():
    password,user_name,got_in=menu()
    if got_in == True:
        print("you got in")
    else:
        print("try again")
main()
