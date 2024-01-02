def caesar_cipher(message, key, mode):
    """Encrypt or decrypt the given message using Caesar cipher."""
    result = ""
    for char in message:
        if char.isalpha():
            shift = key % 26
            if char.islower():
                result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                result += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        else:
            result += char
    return result


def get_valid_key():
    """Prompt user to enter a valid key (0 to 25)."""
    while True:
        key_input = input("Please enter the key (0 to 25) to use:\n> ")
        if key_input.isdigit() and 0 <= int(key_input) <= 25:
            return int(key_input)
        else:
            print("Invalid key value. Please try again.")


def get_input_message(operation):
    """Prompt user to enter the message for encryption or decryption."""
    return input(f"Enter the message to {operation}:\n> ")


def main():
    """Main function to execute the Caesar cipher program."""
    print("Do you want to (e)ncrypt or (d)ecrypt?")
    choice = input("> ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice. Exiting.")
        exit()

    key = get_valid_key() if choice == 'e' else -get_valid_key()
    message = get_input_message("encrypt" if choice == 'e' else "decrypt")

    result = caesar_cipher(message, key, choice)
    print(f"Result: {result}")


if __name__ == "__main__":
    main()
