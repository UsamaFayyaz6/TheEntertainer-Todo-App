'''
Todo Decryption Response 
'''

import json
from cryptography.fernet import Fernet


SECRET_KEY = b'kNSzrr2qU64mtDiRWNgG3sQ77S5iKvT2FjstsIflw7g='
cipher_suite = Fernet(SECRET_KEY)


def decrypt_response(data):
    """
    This method is used for decrypt response
    """

    decrypted_data = cipher_suite.decrypt(data.encode())
    decrypted_response = json.loads(decrypted_data)

    return decrypted_response


print(decrypt_response("gAAAAABlHykb-vX1R5acFQF7s3O73GhG4SlG_QOFRQbx_w0tQICwXc92YuRp4WjW5dibDiaHVj6QdA_bxVcYCRYbFiAoDzfyBR6Z0xtRb7yKSWZfvizTmHs="))
