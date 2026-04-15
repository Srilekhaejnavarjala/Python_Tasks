'''
8. Decorator-based Access Control
Scenario:
Restrict access to certain functions.
Task:
● Create a decorator to check user role
● Use condition inside decorator
● Apply decorator to multiple functions
● Store roles in a dictionary
'''

# Stores users data
users = {
    "sri": "admin",
    "ram": "user",
    "sita": "guest"
}

# Creating decorator
def check_role(required_role):
    def decorator(func):
        def wrapper(username):
            role = users.get(username)

            if role == required_role:
                return func(username)
            else:
                print(f"Access Denied for {username}!")
        return wrapper
    return decorator


# Apply decorator to functions

@check_role("admin")
def delete_data(username):
    print(f"{username} deleted data successfully")


@check_role("user")
def view_data(username):
    print(f"{username} is viewing data")


@check_role("guest")
def limited_view(username):
    print(f"{username} has limited access")


#Test
delete_data("sri")   
delete_data("ram")   
view_data("ram")     
view_data("sita")    
limited_view("sita")
