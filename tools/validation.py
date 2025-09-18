import re

def username_validator(username):
    if re.match(r"^[a-zA-Z0-9]{10,20}$", username):
        return username
    else:
        raise ValueError("Invalid username!!!")

def password_validator(password):
    if re.match(r"^[a-zA-Z0-9$@#]{8,14}$", password):
        return password
    else:
        raise ValueError("Invalid password!!!")

def nickname_validator(nickname):
    if re.match(r"^[a-zA-Z0-9\s]{3,30}$", nickname):
        return nickname
    else:
        raise ValueError("Invalid nickname!!!")
