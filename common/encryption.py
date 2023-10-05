'''
Todo Encrypt Response 
'''

import json
from datetime import datetime
from cryptography.fernet import Fernet


SECRET_KEY = b'kNSzrr2qU64mtDiRWNgG3sQ77S5iKvT2FjstsIflw7g='
cipher_suite = Fernet(SECRET_KEY)


def custom_json_serializer(obj):
    """
    This method is used for convert if obj is datatime into iso format
    """
    if isinstance(obj, datetime):
        return obj.isoformat()

def encrypt_response_func(data, todo_model=None):
    """
    This method is used for encrypt response 
    """
    
    if isinstance(data, list):
        serialized_data = [item.as_dict() for item in data]
    elif todo_model and isinstance(data, todo_model):
        serialized_data = data.as_dict()
    else:
        serialized_data = data

    json_data = json.dumps(serialized_data, default=custom_json_serializer)

    encrypted_data = cipher_suite.encrypt(json_data.encode())
    return encrypted_data.decode('utf-8')