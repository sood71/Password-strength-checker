#Introduce
print("Lets make a strong password!")
print("This program checks the strength of a given password and helps make a stronger one!")
print("A strong password contains: ")
print("Has at least 8 characters")
print("An uppercase letter")
print("A lowercase letter")
print("Special characters")


#DEFINE A FUNCTION
#Assess password strength
def password_strength_check(password):
    score = 0
    length = len(password)

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_characters = "!@$%^&()_-+={}[]|:;,.<>?"

    for char in password:
        if char.isupper():
            has_upper = True

        elif char.islower():
            has_lower = True

        elif char.isdigit():
            has_digit = True

        elif char in special_characters:
            has_special = True

#Scoring to assign points to a password

    if length >= 6:
        score += 1
    if length >= 8:
        score += 1
    if has_upper:
        score += 1
    if has_lower:
        score += 1
    if has_digit:
        score += 1
    if has_special:
        score += 1

#Decsion for the strength of the password

    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

#FeedbacK for improving the strength of the password
    suggestions = []
    if length < 8:
        suggestions.append("Use at least 8 characters")
    if not has_upper:
        suggestions.append("Add an uppercase letter")
    if not has_lower:
        suggestions.append("Add a lowercase letter")
    if not has_digit:
        suggestions.append("Add a number")
    if not has_special:
        suggestions.append("Add a special character (!@$%^&()_-+={}[]|:;,.<>?)")

    return strength, suggestions


#Loops until the password is strong
while True:
    password = input("Please enter a password: ")
    strength, suggestions = password_strength_check(password)

    print("Password Strength:", strength)

    if strength == "Strong":
        print("Great job! Your password is strong!")
        break
    else:
        print("Suggestions to make your password stronger:")
        for s in suggestions:
            print("-", s)
        print()