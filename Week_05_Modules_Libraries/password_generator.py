# password_generator.py
# Week 5 Task – Password Generator using random and string modules

import random
import string

def generate_password(length=12, use_uppercase=True, use_digits=True, use_symbols=True):
    """
    Generate a random password based on given options.
    
    Args:
        length (int): Length of the password
        use_uppercase (bool): Include uppercase letters
        use_digits (bool): Include digits
        use_symbols (bool): Include special characters

    Returns:
        str: Generated password
    """

    # Always include lowercase letters
    characters = string.ascii_lowercase

    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if length < 4:
        print("⚠️ Password length too short! Setting to minimum length of 4.")
        length = 4

    # Randomly pick characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length (min 4): "))
    except ValueError:
        print("⚠️ Invalid input, defaulting to length 12.")
        length = 12

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    password = generate_password(length, use_uppercase, use_digits, use_symbols)
    print(f"✅ Your generated password is: {password}")


if __name__ == "__main__":
    main()
