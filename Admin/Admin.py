def login():
    user = input("Enter username: ")
    passwd = input("Enter password: ")
    if (valid(user, passwd)):
        n = 2
        while (n != -1):
            n = Menu()

def valid(usr, pwd):
    if ((usr.lower() == 'machawk') and (pwd == 'M4cH4wk')):
        return bool('true')
    else :
        return bool('false')
    
def Menu():
    print('Hello world')
    return -1