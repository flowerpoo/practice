# program to check password strength

import re
def check_password_strength(password):
    #check length
    if(len(password)<8):
        print("Passord must be minimum 8 characters")
        return False
    #check uppercase
    if not re.search(r'[A-Z]', password):
        print("Passord must contain utleaset one upper character")
        return False
    #check lowercase
    if not re.search(r'[a-z]', password):
        print("Passord must contain utleaset one lower character")
        return False
    #check numbers
    if not re.search(r'\d', password):
        print("Passord must contain utleaset one number")
        return False
    #check special characters
    if not re.search(r'[!@#$%^&*()":{}|<>,.`~]', password):
        print("Passord must contain utleaset one special character")
        return False
    # All became false then enter into the true condition
    return True

password=input("Enter th password: ")
valid=check_password_strength(password)

if valid:
    print("Congrats valid password")
else:
    print("Enter a valid one")

    
