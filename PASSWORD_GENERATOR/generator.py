import random
import string

def generate_password(length):
    # Define the characters for the password
    all_characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a password using random characters
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def check_strength(password):
    # Define criteria for password strength
    criteria = [
        lambda p: p[0].isupper(),  # First character is uppercase
        lambda p: any(char.islower() for char in p),
        lambda p: any(char.isupper() for char in p),
        lambda p: any(char.isdigit() for char in p),
        lambda p: any(char in string.punctuation for char in p),
        lambda p: len(p) >= 12  # Minimum length criterion
    ]

    # Calculate the strength score based on the criteria
    strength_score = sum(1 for criterion in criteria if criterion(password))

    # Determine the strength level based on the length
    if len(password) >= 15:
        return "Very Strong"
    elif len(password) >= 10:
        return "Strong"
    elif len(password) >= 8:
        return "Moderate"
    else:
        return "Weak"

def main():
    print("Password Generator")

    # Get the desired length of the password from the user
    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

    # Generate the password
    password = generate_password(length)

    # Display the generated password
    print(f"\nGenerated Password: {password}")

    # Check and display the level of strength
    strength_level = check_strength(password)
    print(f"Password Strength: {strength_level}")

if __name__ == "__main__":
    main()
