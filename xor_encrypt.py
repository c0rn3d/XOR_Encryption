def xor_encrypt(message, key):
    # Get the length of the key. This is used to cycle through the key characters.
    key_length = len(key)

    # Encrypt the message using XOR. This creates a new string where each character
    # is XORed with a character from the key. The key characters are reused cyclically.
    encrypted_message = ''.join(
        # For each character in the message:
        # `ord(char)` gets the ASCII value of the character.
        # `ord(key[i % key_length])` gets the ASCII value of the key character at position `i % key_length`.
        # `^` performs the XOR operation between these two ASCII values.
        # `chr(...)` converts the resulting ASCII value back to a character.
        # `''.join(...)` concatenates these characters to form the encrypted message.
        chr(ord(char) ^ ord(key[i % key_length])) for i, char in enumerate(message)
    )
    return encrypted_message

def to_hex_string(s):
    # Convert each character in the string to its hexadecimal representation.
    # `ord(c)` gets the ASCII value of the character `c`.
    # `f'{ord(c):02x}'` formats this value as a two-digit hexadecimal string.
    # `''.join(...)` concatenates these hexadecimal strings to form the final hex representation.
    return ''.join(f'{ord(c):02x}' for c in s)

# Get input from the user for the message to be encrypted and the key to use for encryption.
message = input("Enter the message to encrypt: ")
key = input("Enter the key: ")
# To add salt
salt1v = "%42hsad"
salt2v = "asd67d"
key = salt2v + key + salt1v
# Encrypt the message using the provided key. This returns the encrypted message as a string.
encrypted_message = xor_encrypt(message, key)

# Convert the encrypted message to its hexadecimal representation.
hex_encrypted_message = to_hex_string(encrypted_message)

# Print the encrypted message in hexadecimal format.
print("Encrypted message (hex):", hex_encrypted_message)
