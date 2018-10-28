# ----- Caeser Cipher v05 ----- #

LETTERS = 'abcdefghijklmnopqrstuvwxyz'
NUMBERS = '0123456789'
SYMBOLS = ' .,!?'

def library_generator(keyphrase:int) -> str:
    
    key_list = []
    
    for ch in keyphrase:
        key_list += [ord(ch)]        

    library = []
    letters_upper = list(LETTERS.upper())
    letters_lower = list(LETTERS)
    numbers = list(NUMBERS)
    symbols = list(SYMBOLS)
    
    library_start = letters_upper + letters_lower + numbers + symbols
    
    for i in range(len(library_start)):
        key = key_list[i % len(key_list)]
        library += library_start.pop((key) % len(library_start))
    
    library = ''.join(library)
    
    print(library)
    
    return library


def encrypt(library: str, plaintext: str, keyphrase: int, encrypt: bool) -> str:
    '''
    Using the Ceaser Cipher method to shift the alpha characters of the string 
    plaintext in lowercase by the key amount, then return the encrypted or 
    decrypted string.
    '''

    ciphertext = ''
    
    key_list = []
    
    for ch in keyphrase:
        key_list += [ord(ch)]
    
    j = 0
    
    while j in range(len(plaintext)):
        
        key = key_list[j % len(key_list)]
        
        if encrypt:
            key = -key
        
        index = library.find(plaintext[j])
        
        if index != -1:
            ciphertext += library[(index + key) % len(library)]
        else:
            ciphertext += plaintext[j]  
        j += 1
    
    return ciphertext

while True: 
    
    plaintext = input('Enter your message: ')
    
    # Encrypt or Decrypt
    
    encrypt_prompt = ''
    
    while encrypt_prompt != 'E' and encrypt_prompt != 'D':
        encrypt_prompt = input('Encrypt or Decrypt? (type E or D): ')
    
    encrypt_toggle = (encrypt_prompt == 'E')
    
    # Keyphrase prompt
    
    keyphrase = ''
    
    while not (keyphrase.isalnum() and len(keyphrase) >= 8):
        keyphrase = input('Enter a keyphrase: ')
        
        if not keyphrase.isalnum():
            print('Please use only letters a-Z and numbers 0-9.')
        
        if len(keyphrase) < 8:
            print('Key must be at least 8 characters long.')

    print ('\n' + encrypt(library_generator(keyphrase), plaintext, keyphrase, encrypt_toggle) + '\n')