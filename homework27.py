import random
import string

def generate_password(length=8):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits)
    ]
    all_chars = lowercase + uppercase + digits
    password_chars += [random.choice(all_chars) for _ in range(length - 3)]
    random.shuffle(password_chars)
    return ''.join(password_chars)
if __name__ == "__main__":
    password_length = int(input("Enter desired password length (minimum 3): "))
    if password_length < 3:
        print("Password length must be at least 3 to include all required character types.")
    else:
        generated_password = generate_password(password_length)
        print("Generated Password:", generated_password)