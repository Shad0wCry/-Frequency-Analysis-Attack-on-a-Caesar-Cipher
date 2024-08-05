import string

def caesar_cipher(plaintext, shift):
    """
    Encrypts a plaintext message using a Caesar Cipher with the given shift value.
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            ascii_offset = 65 if char.isupper() else 97
            ciphertext += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        elif char.isdigit():
            ciphertext += chr((ord(char) - 48 + shift) % 10 + 48)
        else:
            ciphertext += char
    return ciphertext

def frequency_analysis(ciphertext):
    """
    Performs frequency analysis on the ciphertext to infer the shift value.
    """
    # Create a dictionary to store the frequency of each letter
    frequency = {}
    for char in ciphertext:
        if char.isalpha():
            char = char.lower()
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1

    # Sort the letters by frequency
    sorted_frequency = sorted(frequency.items(), key=lambda x: x[1], reverse=True)

    # Infer the shift value based on the most frequent letter
    shift = ord(sorted_frequency[0][0]) - ord('e')

    return shift

def main():
    # Get the plaintext from the user
    plaintext = input("Enter the plaintext message: ")

    # Encrypt the plaintext message using a Caesar Cipher with a random shift value
    shift = 3
    ciphertext = caesar_cipher(plaintext, shift)

    # Perform frequency analysis on the ciphertext to infer the shift value
    inferred_shift = frequency_analysis(ciphertext)

    # Decrypt the ciphertext using the inferred shift value
    decrypted_text = caesar_cipher(ciphertext, -inferred_shift)

    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)
    print("Inferred Shift:", inferred_shift)
    print("Decrypted Text:", decrypted_text)

if __name__ == "__main__":
    main()