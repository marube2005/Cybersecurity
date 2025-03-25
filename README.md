# Cybersecurity

# Encryption and Decryption Methods

This repository contains implementations of various encryption and decryption methods in Python. The following encryption techniques are included:

1. **Playfair Cipher**
2. **Vigenère Cipher**
3. **Rail Fence Cipher**
4. **Columnar Transposition Cipher**
5. **Row Transposition Cipher**
6. **Caesar Cipher** (as an additional assignment)

## Description of Encryption Methods

### 1. Playfair Cipher
The Playfair Cipher is a digraph substitution cipher that encrypts plaintext in pairs of letters using a 5x5 key matrix.
- **Encryption:** Replaces letter pairs based on their positions in the matrix.
- **Decryption:** Reverses the process using the same key matrix.

### 2. Vigenère Cipher
A polyalphabetic substitution cipher that uses a keyword to shift letters based on a repeating pattern.
- **Encryption:** Each letter of plaintext is shifted by the corresponding letter in the key.
- **Decryption:** The key is used to reverse the shifts applied to the ciphertext.

### 3. Rail Fence Cipher
A transposition cipher that writes text in a zigzag pattern across multiple rails.
- **Encryption:** Reads the text row by row after writing it in a rail pattern.
- **Decryption:** Reconstructs the original message using the rail positions.

### 4. Columnar Transposition Cipher
A transposition cipher that rearranges text based on column order derived from a key.
- **Encryption:** The plaintext is written in columns and read in a permuted order.
- **Decryption:** Reconstructs the original text by placing characters back into columns.

### 5. Row Transposition Cipher
A variation of the Columnar Transposition Cipher where rows are rearranged based on a numeric key.
- **Encryption:** Text is arranged into rows and then shuffled according to the key.
- **Decryption:** The original row order is restored to obtain the plaintext.

### 6. Caesar Cipher (Additional Assignment)
A simple substitution cipher that shifts letters by a fixed number.
- **Encryption:** Each letter is replaced by another letter shifted by a specific number.
- **Decryption:** The reverse shift restores the original message.

## Usage Instructions

Each encryption method is implemented in its own Python file. To run an encryption or decryption process:

1. Clone this repository:
   ```sh
   git clone https://github.com/marube2005/Cybersecurity.git
   cd encryption-methods
   ```
2. Run the desired cipher script:
   ```sh
   python3 playfair_cipher.py
   ```
   Replace `playfair_cipher.py` with the appropriate file name for other methods.

## Requirements
- Python 3.11

## Contributing
Feel free to contribute by improving the implementations, fixing bugs, or adding new encryption methods.

## License
This project is licensed under the MIT License.

