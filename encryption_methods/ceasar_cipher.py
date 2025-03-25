def caesar_cipher(text, key, encrypt=True):
    result = " "
    for char in text:
        if char.isalpha():         # Only encrypt letters
            shift = key if encrypt else -key
            base = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - base + shift) % 26 + base)
            result += new_char.lower()         # Convert all letters to lowercase
    return result              # Spaces are removed
# Define the key
key = 17
# Original message
message = "I Promise to attend all lectures so that I can pass all my exams."
print(key);
# Encrypt the message
encrypted_text = caesar_cipher(message, key, encrypt=True)
print("Encrypted message:", encrypted_text)

# Decrypt the message
decrypted_text = caesar_cipher(encrypted_text, key, encrypt=False)
print("Decrypted message:", decrypted_text)
