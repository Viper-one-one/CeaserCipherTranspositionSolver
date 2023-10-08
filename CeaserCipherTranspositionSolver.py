import itertools
import math
from pprint import pprint
import threading

key_len = 10
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
key = "aaaaaaaaaa"

def decrypt_ceasar_dev(cipher_text, shift_amount):
    cipher_text = cipher_text.lower()
    plain_text = ""
    for character in cipher_text:
        position = alphabet.index(character)
        new_position = position - shift_amount
        plain_text += alphabet[new_position]
#    print(f"caeser decode result: {plain_text}")
    return plain_text
    
def decrypt_transposition_geeks(cipher_text):
    cols = math.ceil(len(cipher)/key_len)
    rows = key_len-1
    trans_matrix = [[0 for x in range(cols)] for x in range(rows)]
    for i in range(rows):
        for j in range(cols):
            trans_matrix[i][j] = cipher[i * cols + j]
    trans_matrix[:] = itertools.permutations(trans_matrix[:])
    return trans_matrix

cipher = "KUHPVIBQKVOSHWHXBPOFUXHRPVLLDDWVOSKWPREDDVVIDWQRBHBGLLBBPKQUNRVOHQEIRLWOKKRDD"
i = 0
trans_ceasar = ""
trans_trans = ""
while i <= 26:
    trans_ceasar = decrypt_ceasar_dev(cipher, i)
    print(trans_ceasar)
    i = i + 1
    trans_trans = decrypt_transposition_geeks(trans_ceasar)
    t = threading.Thread(target=pprint, args=trans_trans)
    t.daemon = True
    t.start()

