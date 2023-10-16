import math

ceasar_result = ""
transposition_result = ""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher_text = "KUHPVIBQKVOSHWHXBPOFUXHRPVLLDDWVOSKWPREDDVVIDWQRBHBGLLBBPKQUNRVOHQEIRLWOKKRDD"

#https://brilliant.org/wiki/caesar-cipher/
#source for caesar cipher
def decrypt_caesar(cipher_text: str, shift_amount: int):
    translation = ""
    for symbol in cipher_text:
        if symbol in alphabet:
            num = alphabet.find(symbol)
            num = num - shift_amount
            if num < 0:
                num = num + len(alphabet)
            translation = translation + alphabet[num]
        else:
            translation = translation + symbol
    return translation

#https://www.geeksforgeeks.org/columnar-transposition-cipher/
#source for this code that doesnt even work
def decrypt_transposition(cipher: str, key: int): 
    key = str(key)
    decrypted_message = ""
    rows = math.ceil(len(cipher) / len(key))
    diff = rows * len(key) - len(cipher)
    empty_matrix = [""] * len(key)
    key = key.upper()
    dictKey = {}
    for x in range(len(key)):
        dictKey[x] = key[x]
    sorted_key = sorted(dictKey.items(), key=lambda pair: pair[1], reverse=False)
    row_pointer = 0
    char_pointer = 0
    for i in range(len(sorted_key)):
        col = sorted_key[i][0]
        if col >= len(key) - diff:
            rowsMax = rows - 1
        else:
            rowsMax = rows
        for z in range(rowsMax):
            if char_pointer == len(cipher):
                break
            empty_matrix[col] += cipher[char_pointer]
            char_pointer += 1
    decrypted_message = ''
    for row in range(rows):
        for i in range(len(key)):
            if row < len(empty_matrix[i]):
                decrypted_message += empty_matrix[i][row]
    return decrypted_message


#for j in range(1, 9999999, 1):
#        transposition_result = decrypt_transposition("HREMSFYNHSLPETEUYMLCRUEOMSIIAATSLPHTMOBAASSFATNOYEYDIIYYMHNRKOSLENBFOITLHHOAA", j)#solution from ceasar cipher
#        print(transposition_result)
        
#transposition_result = decrypt_transposition("HREMSFYNHSLPETEUYMLCRUEOMSIIAATSLPHTMOBAASSFATNOYEYDIIYYMHNRKOSLENBFOITLHHOAA", 7315426)#solution from transposition
#print(transposition_result)

#brute force method I used to find everything below
index = 0
while index <= 26:
    ceasar_result = decrypt_caesar(cipher_text, index) #"HREMSFYNHSLPETEUYMLCRUEOMSIIAATSLPHTMOBAASSFATNOYEYDIIYYMHNRKOSLENBFOITLHHOAA"
    print(ceasar_result)
    for j in range(1, 9999999, 1):
        transposition_result = decrypt_transposition(ceasar_result, j) #7315426
        print(transposition_result)
    index += 1