#imports
from email_validator import validate_email, EmailNotValidError
#email validator
def email_val(email:str)->str:
    try:
        #will valdate syntax of the email, and check deliverablility
        email = validate_email(email, check_deliverability=True)
        return True, None

    except EmailNotValidError as e:
        return False, str(e)
