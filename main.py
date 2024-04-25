def caesar_cipher(text):    
    alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
    encrypted_text = ""

    for char in text:
        if char.lower() in alphabet:
            index = alphabet.index(char.lower())
            new_index = (index - 2) % len(alphabet)
            encrypted_char = alphabet[new_index]
            if char.isupper():
                encrypted_char = encrypted_char.upper()
            encrypted_text += encrypted_char
        else:
            encrypted_text += char

    return encrypted_text

text = input().lower()
encrypted_text = caesar_cipher(text)
print(f"Розшиврований текст: {encrypted_text}")
