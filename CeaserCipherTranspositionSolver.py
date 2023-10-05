alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def decrypt_dev(cipher_text, shift_amount):
    plain_text = ""
    for character in cipher_text:
        position = alphabet.index(character)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"decode result: {plain_text}")
    
cipher = "KUHPVIBQKVOSHWHXBPOFUXHRPVLLDDWVOSKWPREDDVVIDWQRBHBGLLBBPKQUNRVOHQEIRLWOKKRDD"

