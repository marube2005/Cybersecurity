import re
def prepare_key_matrix(key):
    key = key.upper().replace("J", "I")  # Standard Playfair rule: J -> I
    matrix = []
    seen = set()
    for char in key:
        if char not in seen and char.isalpha():
            seen.add(char)
            matrix.append(char)
    for char in "ABCDEFGHIKLMNOPQRSTUVWXYZ":  # J is already replaced by I
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]
def find_position(matrix, char):
    for i, row in enumerate(matrix):
        for j, cell in enumerate(row):
            if char == cell:
                return i, j
    return None

def process_text(text):
    text = re.sub(r'[^A-Z]', '', text.upper().replace("J", "I"))  # Standard Playfair handling of J
    processed = ""
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'X'   
        if a == b:
            processed += a + 'X'
            i += 1
        else:
            processed += a + b
            i += 2
    if len(processed) % 2 != 0:
        processed += 'X'
    return processed
def playfair_encrypt(plaintext, key):
    matrix = prepare_key_matrix(key)
    plaintext = process_text(plaintext)
    ciphertext = "" 
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext
def playfair_decrypt(ciphertext, key):
    matrix = prepare_key_matrix(key)
    plaintext = "" 
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(matrix, a)
        row2, col2 = find_position(matrix, b)
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    
    # Remove unnecessary 'X' if it was added between identical letters
    corrected_plaintext = ""
    i = 0
    while i < len(plaintext):
        if i < len(plaintext) - 2 and plaintext[i] == plaintext[i+2] and plaintext[i+1] == 'X':
            corrected_plaintext += plaintext[i]
            i += 2  # Skip the artificial 'X'
        else:
            corrected_plaintext += plaintext[i]
            i += 1

    # Remove any trailing X if it was added as padding
    if corrected_plaintext.endswith("X"):
        corrected_plaintext = corrected_plaintext[:-1]

    return corrected_plaintext

# Example Usage
key = "KEYWORD"
plaintext = "COMPUTERSECURITY"
ciphertext = playfair_encrypt(plaintext, key)
decrypted_text = playfair_decrypt(ciphertext, key)

print("Key Matrix:")
for row in prepare_key_matrix(key):
    print(row)
print("\nPlaintext:", plaintext)
print("Encrypted Text:", ciphertext)
print("Decrypted Text:", decrypted_text)
