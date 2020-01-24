welcome = "Welcome.  Do you want to login or create a new account?"

print(welcome)

def login():
    global username
    global password
    global password2
    for retry in range(5):
        welcome_input = input("login or create?")
        if welcome_input == "login":
            username = input("Please enter username")
            password = input("Please enter your password")
            break
        if welcome_input == "create":
            username = input("Please choose a username")
            password = input("Please choose a password")
            password2 = input("Please confirm you chose password")
            break
        print("Sorry, please type login or create")
    else:
        print("Sorry, you don't get this")
        username = ""

login()

if username != "":
    print(username)
elif username == "":
    print("No username available")

if password != "":
    print(password)
