# TheEntertainer-Todo-App

Todo App using flask-restful include multiple features like Basic Authentication, response encryption etc..

## Table of Contents

- [Installation](#installation)
- [Project Setup](#project-setup)
- [How to Run](#how-to-run)
- [Decrypting the Response](#decrypting-the-response)

## Installation

Clone the repository:

   ```shell
   git clone https://github.com/UsamaFayyaz6/TheEntertainer-Todo-App.git
   cd TheEntertainer-Todo-App/
   ```

## Project Setup
```
cd /path/to/the/project/
pip install -r requirements.txt
activate your enviroment: source /path-to-the-env/activate
```

## How to Run
```
python app.py
```

### Decrypting the Response

I make a file in project/common/decryption.py this file you will use for decrypt response and I'm also writing here:

```
import json
from cryptography.fernet import Fernet

SECRET_KEY = 'your_secret_key_is_available_in_encryption file' <!--`b'kNSzrr2qU64mtDiRWNgG3sQ77S5iKvT2FjstsIflw7g='-->
cipher_suite = Fernet(SECRET_KEY)

def decrypt_response(data):
    decrypted_data = cipher_suite.decrypt(data.encode())
    decrypted_response = json.loads(decrypted_data)
    return decrypted_response
 ```
