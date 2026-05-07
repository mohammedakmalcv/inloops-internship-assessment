import re

def validate_user_input(username, email, password):
    
    errors = []

    
    if not re.match(r"^[a-zA-Z0-9]{3,16}$", username):
        errors.append("Username must be 3-16 characters long and contain only letters and numbers.")

    
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    if not re.match(email_regex, email):
        errors.append("Invalid email format.")

    
    if len(password) < 8:
        errors.append("Password must be at least 8 characters long.")
    if not re.search(r"[A-Z]", password):
        errors.append("Password must contain at least one uppercase letter.")
    if not re.search(r"[a-z]", password):
        errors.append("Password must contain at least one lowercase letter.")
    if not re.search(r"\d", password):
        errors.append("Password must contain at least one number.")
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        errors.append("Password must contain at least one special character.")

    
    if errors:
        return {"is_valid": False, "errors": errors}
    else:
        return {"is_valid": True, "message": "Success! All inputs are valid."}


if __name__ == "__main__":
    
    print("--- Test 1: Invalid Inputs ---")
    
    bad_test = validate_user_input("ak", "akmal@com", "weakpass")
    print(bad_test)

    print("\n--- Test 2: Valid Inputs ---")
   
    good_test = validate_user_input("Akmal2026", "akmal@example.com", "Str0ng!P@ssw0rd")
    print(good_test)