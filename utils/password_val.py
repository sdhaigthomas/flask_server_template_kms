#checks if a usersubmitted password is valid.
def password_val(password:str, maxlen:int=64, minlen:int=8)->tuple:
    to_return = None
    length = len(password)
    if password in [None, ""]:
        to_return = "Please enter a Password!"
    elif length > maxlen:
        to_return = f"Password is too long! Maximum length is {maxlen}"
    elif length < minlen:
        to_return = f"Password is too short! The minimum length is {minlen}"
    #print(f"Password {to_return}")
    if to_return: return False, to_return
    else: return True, to_return
    

        
