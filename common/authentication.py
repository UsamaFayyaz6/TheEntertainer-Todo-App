'''
Todo App Basic Authentication 
'''

from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()

USER_DATA = {
    "entertainer": "entertainer@123"
}


@auth.verify_password
def verify(username, password):
    """
    This method used for check user's basic authentication
    """
    if not (username and password):
        return False
    return USER_DATA.get(username) == password