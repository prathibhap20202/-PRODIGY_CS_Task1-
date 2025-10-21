# Caesar Cipher Program - Show Both Encryption and Decryption

def encrypt(text, s):
    """Encrypt text using Caesar Cipher"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + s) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 + s) % 26 + 97)
        else:
            result += char
    return result

def decrypt(text, s):
    """Decrypt text using Caesar Cipher"""
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 - s) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) - 97 - s) % 26 + 97)
        else:
            result += char
    return result

# ---- User Interaction ----
print("=== Welcome to Caesar Cipher ===")

text = input("Enter your message: ")

# Input shift value and validate
while True:
    try:
        s = int(input("Enter shift value (number): "))
        break
    except ValueError:
        print("Shift must be a number. Try again.")

# Show both encryption and decryption
cipher_text = encrypt(text, s)
decrypted_text = decrypt(cipher_text, s)

print("\nOriginal Message: ", text)
print("Encrypted Message:", cipher_text)
print("Decrypted Message:", decrypted_text)
