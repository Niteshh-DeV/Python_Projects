import random
import string

def generate_password(length, include_letters, include_numbers, include_symbols):
    characters = ""
    if include_letters:
        characters += string.ascii_letters  # Uppercase + lowercase letters
    if include_numbers:
        characters += string.digits  # Numbers
    if include_symbols:
        characters += string.punctuation  # Special symbols

    if not characters:
        print("You must select at least one type of character!")
        return None

    password = "".join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("\n--- Password Generator ---")

    try:
        length = int(input("Enter the desired password length: "))
        include_letters = input("Include letters? (yes/no): ").strip().lower() == "yes"
        include_numbers = input("Include numbers? (yes/no): ").strip().lower() == "yes"
        include_symbols = input("Include symbols? (yes/no): ").strip().lower() == "yes"

        password = generate_password(length, include_letters, include_numbers, include_symbols)
        if password:
            print(f"\nYour generated password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number for the length.")

if __name__ == "__main__":
    main()