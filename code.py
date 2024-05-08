import random
import string

def generate_password( length, complexity,uppercase=True, lowercase=True, digits=True, punctuation=True):
    characters = ''
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if punctuation:
        characters += string.punctuation

    if not characters:
        raise ValueError("At least one character type must be selected")

    if complexity == "easy":
        characters = string.ascii_letters + string.digits
        include_uppercase = ask_yes_no_question("Include uppercase letters?")
        include_lowercase = ask_yes_no_question("Include lowercase letters?")
        include_digits = ask_yes_no_question("Include digits?")
    elif complexity == "hard":
        characters= string.ascii_letters + string.digits + string.punctuation
        include_uppercase = ask_yes_no_question("Include uppercase letters?")
        include_lowercase = ask_yes_no_question("Include lowercase letters?")
        include_digits = ask_yes_no_question("Include digits?")
        include_punctuation = ask_yes_no_question("Include punctuation?")

    else:
        print("Invalid complexity level. Please choose 'easy' or 'hard'.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

def ask_yes_no_question(question):
    while True:
        response = input(question + " (y/n): ").strip().lower()
        if response in ['y', 'yes']:
            return True
        elif response in ['n', 'no']:
            return False
        else:
            print("Please enter 'y' for yes or 'n' for no.")

    password = ''.join(random.choice(characters) for i in range(length))
    return password

length = int(input("Enter the length of the password: "))
complexity = input("Enter the complexity level (easy/hard): ").lower()

try:
    password = generate_password(length, complexity)
    print("Generated Password:", password)
except ValueError as e:
    print("Error:", e)

