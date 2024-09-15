def xor_decrypt(encrypted_message, key):
    # Get the length of the key. This is used to cycle through the key characters.
    key_length = len(key)

    # Decrypt the message using XOR. This creates a new string where each character
    # is XORed with a character from the key. The key characters are reused cyclically.
    decrypted_message = ''.join(
        # For each character in the encrypted_message:
        # `ord(char)` gets the ASCII value of the character.
        # `ord(key[i % key_length])` gets the ASCII value of the key character at position `i % key_length`.
        # `^` performs the XOR operation between these two ASCII values.
        # `chr(...)` converts the resulting ASCII value back to a character.
        # `''.join(...)` concatenates these characters to form the decrypted message.
        chr(ord(char) ^ ord(key[i % key_length])) for i, char in enumerate(encrypted_message)
    )
    return decrypted_message

def from_hex_string(hex_string):
    # Convert a hexadecimal string back to a regular string.
    # This function processes the hex string in chunks of two characters,
    # converts each chunk from hexadecimal to decimal, and then to its ASCII character.
    return ''.join(
        # Process each pair of hex characters:
        # `int(hex_string[i:i+2], 16)` converts the hex pair to an integer.
        # `chr(...)` converts this integer to its corresponding ASCII character.
        # `''.join(...)` concatenates these characters to form the final string.
        chr(int(hex_string[i:i+2], 16)) for i in range(0, len(hex_string), 2)
    )

# Get input from the user for the encrypted message (in hexadecimal format) and the key.
hex_encrypted_message = input("Enter the encrypted message (hex): ")
key = input("Enter the key: ")
# To add salt
salt1v = "%42hsad"
salt2v = "asd67d"
key = salt2v + key + salt1v
# Convert the hexadecimal string back to the original encrypted message.
# This involves converting the hex representation into a regular string of characters.
encrypted_message = from_hex_string(hex_encrypted_message)

# Decrypt the message using the provided key. This returns the original plaintext message.
decrypted_message = xor_decrypt(encrypted_message, key)

# Print the decrypted message to the user.
print("Decrypted message:", decrypted_message)
