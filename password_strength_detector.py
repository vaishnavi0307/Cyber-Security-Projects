import re

def check_password_strength(password):
    """
    Evaluates the strength of a password.
    Returns a score and suggestions for improvement.
    """
    score = 0
    suggestions = []

    # Check length
    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        suggestions.append("Make your password at least 12 characters long.")

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter.")

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter.")

    # Check for numbers
    if re.search(r'\d', password):
        score += 1
    else:
        suggestions.append("Include at least one number.")

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1
    else:
        suggestions.append("Include at least one special character.")

    # Avoid common patterns
    if re.search(r'(1234|password|qwerty|abcd)', password, re.IGNORECASE):
        score -= 1
        suggestions.append("Avoid common patterns like '1234' or 'password'.")

    return score, suggestions


# User input and strength evaluation
if __name__ == "__main__":
    user_password = input("Enter a password to evaluate its strength: ")
    strength_score, tips = check_password_strength(user_password)

    print(f"\nPassword Strength Score: {strength_score}/7")
    if strength_score >= 6:
        print("Your password is strong!")
    elif 4 <= strength_score < 6:
        print("Your password is decent but could be stronger.")
    else:
        print("Your password is weak. Consider the following suggestions:")

    for tip in tips:
        print(f"- {tip}")
