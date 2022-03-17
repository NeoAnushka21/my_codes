import re

def validate_emai(email):

    regex_email =re.compile(r"""
            ^([a-z0-9_\.-]+)              # local Part
            @                             # single @ sign
            ([0-9a-z\.-]+)                # Domain name
            \.                            # single Dot .
            ([a-z]{2,6})$                 # Top level Domain  
             """, re.VERBOSE | re.IGNORECASE)
    res=regex_email.fullmatch(email)

    if res:
        print("{} is Valid . Details are as follows:".format(email))
        print("Local:{}")

    else:
        print("{} is Invaild".format(email))
