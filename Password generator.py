import random
import string


def generate_password(length=12, use_digits=True, use_special_chars=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ''
    special_chars = string.punctuation if use_special_chars else ''

    all_chars = letters + digits + special_chars

    if not all_chars:
        return "Error: No characters selected for password generation"

    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password


# Example Usage
if __name__ == "__main__":
    length = int(input("Enter password length: "))
    include_digits = input("Include digits? (y/n): ").strip().lower() == 'y'
    include_special_chars = input("Include special characters? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, include_digits, include_special_chars)
    print(f"Generated Password: {password}")
