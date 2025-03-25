def columnar_encrypt(plaintext, key):
    # Remove whitespace from the plaintext.
    plaintext = "".join(plaintext.split())
    num_cols = len(key)
    num_rows = len(plaintext) // num_cols
    if len(plaintext) % num_cols != 0:
        num_rows += 1
    # Pad the plaintext with 'X' to fill the rectangle.
    padded_length = num_rows * num_cols
    plaintext += 'X' * (padded_length - len(plaintext))
    # Create the matrix.
    matrix = [list(plaintext[i*num_cols:(i+1)*num_cols]) for i in range(num_rows)]
    # Determine the order of columns based on the key. 
    order = sorted(list(enumerate(key)), key=lambda x: x[1])
    # Read columns in the sorted order.
    cipher = ""
    for col_index, _ in order:
        for row in matrix:
            cipher += row[col_index]
    return cipher
def columnar_decrypt(cipher, key):
    num_cols = len(key)
    num_rows = len(cipher) // num_cols
    # Determine the order of columns based on the key.
    order = sorted(list(enumerate(key)), key=lambda x: x[1])

    # Create an empty matrix.
    matrix = [[''] * num_cols for _ in range(num_rows)]
    idx = 0
    # Fill the matrix column by column in the order of the sorted key.
    for col_index, _ in order:
        for row in range(num_rows):
            matrix[row][col_index] = cipher[idx]
            idx += 1
    # Read the matrix row-wise to get the plaintext.
    plain = ""
    for row in matrix:
        plain += "".join(row)
    # Remove any trailing padding characters.
    return plain.rstrip("X")
def main():
    key = input("Enter the key for Columnar Transposition cipher: ")
    text = input("Enter the text: ")
    encrypted = columnar_encrypt(text, key)
    print("Encrypted:", encrypted)
    decrypted = columnar_decrypt(encrypted, key)
    print("Decrypted:", decrypted)

main()

