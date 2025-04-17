import string
import random

def generate_short_code(length: int = 6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
