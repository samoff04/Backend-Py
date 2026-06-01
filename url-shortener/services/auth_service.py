import bcrypt
from models.user_model import create_user, get_user
from utils.jwt_handler import generate_token

def register_user(username, password):
    hashed = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    create_user(username, hashed.decode())

def login_user(username, password):
    user = get_user(username)
    if not user:
        return None
    if bcrypt.checkpw(password.encode(), user["password"].encode()):
        return generate_token(user["id"])
    return None