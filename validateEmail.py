import re
from validate_email import validate_emial

"""
this function validates the format of the email.
@param: email. a string that represents the email.
"""

def validateEmailFormat(email):
    email_regex = r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
    if re.match(email_regex, email):
        return True
    else:
        return False
    
"""
this function validates if the mx record exist.
@param: email. a string that represents the email.
"""
def validateMxRecord(email):
    return validate_email(email, verify=True)