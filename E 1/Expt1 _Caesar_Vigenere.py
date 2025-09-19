def caesar_cipher(text, shift, decrypt=False):
    if decrypt:
        shift *= -1
    
    result = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - base + shift) % 26 + base)
        else:
            result += char
    return result

def vigenere_cipher(text, key, decrypt=False):
    result = ""
    key_shifts = [ord(k.lower()) - ord('a') for k in key]
    direction = -1 if decrypt else 1
    
    for i, char in enumerate(text):
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            offset = key_shifts[i % len(key_shifts)] * direction
            result += chr((ord(char) - base + offset) % 26 + base)
        else:
            result += char
    return result

# --- Example Usage ---
print("--- Caesar Cipher ---")
encrypted_c = caesar_cipher("Hello World", 3)
print(f"Encrypted: {encrypted_c}")
print(f"Decrypted: {caesar_cipher(encrypted_c, 3, decrypt=True)}\n")

print("--- Vigenère Cipher ---")
encrypted_v = vigenere_cipher("Network Security", "KEY")
print(f"Encrypted: {encrypted_v}")
print(f"Decrypted: {vigenere_cipher(encrypted_v, 'KEY', decrypt=True)}")
