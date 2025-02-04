import random
import string

def generate_random_id(length=10):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))
