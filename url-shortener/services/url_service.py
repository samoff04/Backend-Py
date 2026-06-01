import string
import random
from models.url_model import save_url

def generate_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))

def create_short_url(original_url, user_id):
    code = generate_code()
    save_url(original_url, code, user_id)
    return code