def rail_fence_encrypt(text, num_rails):
    num_rails = int(num_rails)
    if num_rails <= 1 or num_rails >= len(text):
        return text
    rails = [''] * num_rails
    row = 0
    direction = 1
    for char in text:
        rails[row] += char
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1
    return ''.join(rails)
def rail_fence_decrypt(cipher, num_rails):
    num_rails = int(num_rails)
    if num_rails <= 1 or num_rails >= len(cipher):
        return cipher
    # Create the rail pattern used during encryption.
    rail_pattern = [0] * len(cipher)
    row = 0
    direction = 1
    for i in range(len(cipher)):
        rail_pattern[i] = row
        row += direction
        if row == 0 or row == num_rails - 1:
            direction *= -1
    # Count the number of characters for each rail.
    rail_counts = [rail_pattern.count(r) for r in range(num_rails)]
    # Slice the cipher text into parts for each rail.
    rails = []
    index = 0
    for count in rail_counts:
        rails.append(list(cipher[index:index+count]))
        index += count
    # Reconstruct the plaintext by taking letters in the order of the rail pattern.
    plaintext = []
    for r in rail_pattern:
        plaintext.append(rails[r].pop(0))
    return ''.join(plaintext)
def main():
    num_rails = input("Enter the number of rails for Rail Fence cipher: ")
    text = input("Enter the text: ")
    encrypted = rail_fence_encrypt(text, num_rails)
    print("Encrypted:", encrypted)
    decrypted = rail_fence_decrypt(encrypted, num_rails)
    print("Decrypted:", decrypted)

main()

