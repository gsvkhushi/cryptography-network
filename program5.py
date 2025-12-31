import re

def check_password_string(password):
    if len(password)<8:
        return "Weak Password should be at least 8 characters."
    if not re.search ("[a-z]", password):
        return "Weak : Password should have at least one Lowercase letter."
    if not re.search ("[A-Z]",password):
        return "Weak : Password should have at least one uppercase letter."
    if not re.search ("[0-9]",password):
        return "Weak : Password should have at least one digit."
    if not re.search ("[!@#$%^&*(),..?\":{}|<>]",password):
        return "Weak : Password should have at least one special character."
    
    return "Strong Password!"
password = input("Enter your password:")
print(check_password_string(password))