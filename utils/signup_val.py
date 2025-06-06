#validates weather a response can be used to make a new account
def signup_val(get:object, User:object, password_val:object, username_val:object, email_val:object)->tuple:
    #set the responses to varibles
    username      = get("username")
    password      = get("password")
    email         = get("email")
    conf_password = get("password confirm")

    #is the form even filled out?
    if username:
        #validate the username
        to_flash = username_val(username)

        if not to_flash[0]: 
            return False, to_flash[1]

        #now check for password
        to_flash = password_val(password)
        
        if not to_flash[0]: 
            return False, to_flash[1]

        #email check
        to_flash = email_val(email)

        if not to_flash[0]:
            return False, to_flash[1]

        # does the password equal the check?
        if password != conf_password:
            return False, "Passwords must match"

        #is the username taken?
        if User.query.filter_by(username=username).first() == None:
            return True, None

    return False, "Username occupied"