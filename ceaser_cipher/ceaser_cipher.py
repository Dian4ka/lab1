import string

def caesar_cipher(text, shift, decrypt=False):
    """Encrypt or decrypt text using the Caesar cipher."""
    alphabet = string.ascii_letters + string.digits + string.punctuation + " "
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]

    if decrypt:
        translation_table = str.maketrans(shifted_alphabet, alphabet)
    else:
        translation_table = str.maketrans(alphabet, shifted_alphabet)

    return text.translate(translation_table)

# Read the input text from a file
with open("input.txt", "r", encoding="utf-8") as file:
    original_text = file.read()

# User input: shift value
shift = int(input("Enter shift value: "))

# Encrypt the text
encrypted_text = caesar_cipher(original_text, shift)

# Save encrypted text to a file
with open("encrypted.txt", "w", encoding="utf-8") as file:
    file.write(encrypted_text)

print("\nEncryption successful! Check 'encrypted.txt'.")

# --- Decryption (for testing) ---
if input("\nDo you want to decrypt? (yes/no): ").strip().lower() == "yes":
    decrypted_text = caesar_cipher(encrypted_text, shift, decrypt=True)
    print("\nDecrypted text:\n", decrypted_text)

