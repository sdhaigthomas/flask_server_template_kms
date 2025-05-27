#validates weather a response can be used to make a new account
def signup_val(get:object, User:object, password_val:object, username_val:object)->tuple:
    #set the responses to varibles
    username      = get("username")
    password      = get("password")
    conf_password = get("password confirm")

    #is the form even filled out?
    if username:
        #validate the username
        to_flash = username_val(username)
        print(to_flash)
        if to_flash: 
            return False, to_flash
        to_flash = password_val(password)
          
        if to_flash: 
            return False, to_flash
        elif password != conf_password:
            return False, to_flash
        else:
            #is the username taken?
            if User.query.filter_by(username=username).first() == None:
                return True, None
    return False, "Please enter a username"