#Secure Login system (Decorators)
'''
A web application wants to ensure that users are authenticated before
accessing sensitive functions. Create a decorator that checks whether the
user is logged in before allowing access to a function.

'''
def web_login(func):
    def wrapper():
        if logged_in == True:
            func()
        else:
            print("Access Denied! Please login first.")
    return wrapper

logged_in = False

@web_login
def view_user():
    print("Welcome! You got access to function")

view_user()

logged_in = True
print("\n User logged in successfully")
view_user()
