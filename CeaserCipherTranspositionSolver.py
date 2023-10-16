import math

ceasar_result = ""
transposition_result = ""
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
cipher_text = "KUHPVIBQKVOSHWHXBPOFUXHRPVLLDDWVOSKWPREDDVVIDWQRBHBGLLBBPKQUNRVOHQEIRLWOKKRDD"

def decrypt_ceasar(cipher_text: str, shift_amount: int):
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
#    print(f"caeser decode result: {plain_text}")
    return translation

#https://www.tutorialspoint.com/cryptography_with_python/cryptography_with_python_decryption_of_transposition_cipher.htm
#source for this code that doesnt even work
def decrypt_transposition(cipher: str, key: int): 
    numOfColumns = math.ceil(len(cipher) / key)
    numOfRows = key
    numOfShadedBoxes = (numOfColumns * numOfRows) - len(cipher)
    plaintext = [''] * numOfColumns
    col = 0
    row = 0
   
    for symbol in cipher:
        plaintext[col] += symbol
        col += 1
        if (col == numOfColumns) or (col == numOfColumns - 1 and row >= numOfRows - numOfShadedBoxes):
            col = 0
            row += 1
    return ''.join(plaintext)

#for j in range(1, 999999999):
#    transposition_result = decrypt_transposition("HREMSFYNHSLPETEUYMLCRUEOMSIIAATSLPHTMOBAASSFATNOYEYDIIYYMHNRKOSLENBFOITLHHOAA", j)
#print(list(permutations(list("HREMSFYNHSLPETEUYMLCRUEOMSIIAATSLPHTMOBAASSFATNOYEYDIIYYMHNRKOSLENBFOITLHHOAA"))))

for j in range(1, 9999999, 1):
        transposition_result = decrypt_transposition("HREMSFYNHSLPETEUYMLCRUEOMSIIAATSLPHTMOBAASSFATNOYEYDIIYYMHNRKOSLENBFOITLHHOAA", j)#solution from ceasar cipher
        print(transposition_result)

index = 0
while index <= 26:
    ceasar_result = decrypt_ceasar(cipher_text, index)
    print(ceasar_result)
    for j in range(1, 9999999, 1):
        transposition_result = decrypt_transposition(ceasar_result, j)
        print(transposition_result)
    #transposition_result = decrypt_transposition(10, cipher_text)
    #ceasar_result = decrypt_ceasar(transposition_result, i)
    #print(ceasar_result)
    index += 1