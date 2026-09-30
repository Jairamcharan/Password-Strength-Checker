import re


def check_password(password):
    score = 0
    suggestions = []

    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Use at least 8 characters.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add an uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add a lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add a number.")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        suggestions.append("Add a special character.")

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return strength, score, suggestions


password = input("Enter your password: ")

strength, score, suggestions = check_password(password)

print("\nPassword Analysis")
print("-----------------")
print(f"Strength: {strength}")
print(f"Score: {score}/5")

if suggestions:
    print("\nSuggestions:")
    for suggestion in suggestions:
        print(f"- {suggestion}")
else:
    print("\nGood! Your password meets all basic checks.")
