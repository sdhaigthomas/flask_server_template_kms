def username_val(username:str, maxlen:int=15, minlen:int=3)->str:
    to_return = None
    length = len(username)
    if length in [None, ""]:
        to_return = "Please enter a Username!"
    elif length > maxlen:
        to_return = f"Username is too long! Maximum length is {maxlen}"
    elif length < minlen:
        to_return = f"Username is too short! The minimum length is {minlen}"
    #print(f"Username {to_return}")
    if to_return: return False, to_return
    else: return True, to_return
        
