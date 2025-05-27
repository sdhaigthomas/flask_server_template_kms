#checks if keys are added
def key_checker(tempkey:str="tempkey")->str:
    #keys
    try: 
        #checks if keys.py can be found
        from keys import get_key
        return get_key()
    except: 
        #warns user if keys.py isn't found
        input(f"\033[1m\033[91m{"-"*50} \nkeys.py file missing! \nPlease add a key.py file with a get_key() function \n{'-'*50} \033[00m\033[00m")
        return tempkey
    