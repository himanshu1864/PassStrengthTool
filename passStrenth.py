import re

def assess_password_strength(password):
    # Initialize the score
    score = 0
    
    # Criteria 1: Length of the password
    length = len(password)
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1

    # Criteria 2: Presence of both uppercase and lowercase letters
    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1

    # Criteria 3: Presence of numbers
    if re.search(r'\d', password):
        score += 1

    # Criteria 4: Presence of special characters
    if re.search(r'[@$!%*?&#]', password):
        score += 1

    # Criteria 5: Absence of common passwords (for simplicity, we'll use a short list)
    common_passwords = ["password", "123456", "123456789", "qwerty", "abc123"]
    if password.lower() not in common_passwords:
        score += 1

    # Determine strength based on the score
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return strength

# Example usage:
password = input("Enter a password to assess its strength: ")
strength = assess_password_strength(password)
print(f"Password Strength: {strength}")
