from math import ceil

def row_transposition_encrypt(plaintext, key):
    # Remove whitespace from the plaintext.
    plaintext = "".join(plaintext.split())
    num_rows = len(key)
    num_cols = ceil(len(plaintext) / num_rows)
    
    # Pad the plaintext with 'X' to fill the rectangle.
    padded_length = num_rows * num_cols
    plaintext += 'X' * (padded_length - len(plaintext))
    
    # Create the matrix row by row.
    rows = [list(plaintext[i * num_cols:(i + 1) * num_cols]) for i in range(num_rows)]
    
    # Determine the order of rows based on the key.
    # Each element is a tuple: (original_index, character)
    order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    # Concatenate rows in the sorted order.
    cipher = ""
    for row_index, _ in order:
        cipher += "".join(rows[row_index])
    
    return cipher

def row_transposition_decrypt(cipher, key):
    num_rows = len(key)
    num_cols = len(cipher) // num_rows
    
    # Determine the order of rows based on the key.
    order = sorted(list(enumerate(key)), key=lambda x: x[1])
    
    # Allocate the cipher text blocks to rows according to the sorted order.
    rows = [None] * num_rows
    idx = 0
    for original_index, _ in order:
        rows[original_index] = list(cipher[idx:idx + num_cols])
        idx += num_cols
    
    # Read the matrix row-wise to reconstruct the plaintext.
    plain = ""
    for row in rows:
        plain += "".join(row)
    
    # Remove any trailing padding characters.
    return plain.rstrip("X")

def main():
    key = input("Enter the key for Row Transposition cipher: ")
    text = input("Enter the text: ")
    
    encrypted = row_transposition_encrypt(text, key)
    print("Encrypted:", encrypted)
    
    decrypted = row_transposition_decrypt(encrypted, key)
    print("Decrypted:", decrypted)


main()
