import random
import string

def generate_id(prefix: str, length: int = 6) -> str:
    suffix = "".join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length))
    return f"{prefix}{suffix}"
