from itertools import permutations
import math


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = "aaaaaaaaaa"

def decrypt_ceasar_dev(cipher_text, shift_amount):
    cipher_text = cipher_text.lower()
    plain_text = ""
    for character in cipher_text:
        position = alphabet.index(character)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
    print(f"caeser decode result: {plain_text}")
    return plain_text
    
def decrypt_transposition_geeks(cipher_text, key):
    msg = ""
    k_index = 0
    msg_index = 0
    msg_len = float(len(cipher_text))
    msg_list = list(cipher_text)
    key_list = sorted(list(key))
    col = len(key)
    row = int(math.ceil(cipher_text / col))
    plain_text = ""

    for _ in range(row):
        plain_text += [[None] * col]
            
    for _ in range(col):
        curr_index = key.index(key_list[k_index])
        for j in range(row):
            plain_text[j][curr_index] = msg_list[msg_index]
            msg_index += 1
        k_index += 1
    try:
        msg = ''.join(sum(plain_text, []))
    except TypeError:
        raise TypeError("Repeated word")
    null_count = msg.count('_')
    if null_count > 0:
        return msg[: -null_count]
    return msg
    

cipher = "KUHPVIBQKVOSHWHXBPOFUXHRPVLLDDWVOSKWPREDDVVIDWQRBHBGLLBBPKQUNRVOHQEIRLWOKKRDD"

print(cipher)
i = 0
while i <= 26:
    decrypt_ceasar_dev(cipher, i)
    i = i + 1
    
maxlen = 3
x[maxlen+1]
for thislen in range(maxlen):
    x[thislen] = 0
    all_combinations( x, thislen-1 )

