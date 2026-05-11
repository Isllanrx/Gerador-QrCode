import re

def is_valid_email(email: str) -> bool:
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def is_valid_phone(phone: str) -> bool:
    return bool(re.match(r'^\+?[\d\s-]+$', phone))

def sanitize_filename(name: str) -> str:
    return "".join(c for c in name if c.isalnum() or c in "._- ").strip()
