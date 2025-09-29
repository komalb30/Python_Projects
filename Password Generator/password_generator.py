import random
import string

def generate_password(length=12):
    # Define the character set: lowercase, uppercase, digits, special characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate password by randomly choosing characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Simple Password Generator")
    
    try:
        length = int(input("Enter desired password length (e.g., 12): "))
        if length <= 0:
            print("Please enter a positive integer.")
            return
        
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
