import re

def validate_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return bool(re.fullmatch(pattern, email))

def validate_phone(phone):
    pattern = r'^[6-9]\d{9}$'
    return bool(re.fullmatch(pattern, phone))