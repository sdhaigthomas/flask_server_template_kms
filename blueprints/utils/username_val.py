def username_val(username:str, maxlen:int=15, minlen:int=3)->str:
    to_return = None
    length = len(username)
    if length in [None, ""]:
        to_return = "Please enter a Username!"
    elif length > maxlen:
        to_return = f"Username is too long! Maximum length is {maxlen}"
    elif length < minlen:
        to_return = f"Username is too short! The minimum length is {minlen}"
    return to_return
        
