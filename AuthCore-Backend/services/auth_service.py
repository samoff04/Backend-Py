import bcrypt
from models.user_model import *

def register_user(username, password):
    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    )
    create_user(
        username,
        hashed.decode()
    )

def login_user(username, password):
    user = get_user(username)
    if not user:
        return False
    return bcrypt.checkpw(
        password.encode(),
        user["password"].encode()
    )