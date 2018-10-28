# ----- Caeser Cipher v04 ----- #


LIBRARY = '?aZbY1cXdW2eVfU3gTh4SiRj5QkPl6OmNn7MoLp8KqJ9rIs0HtG uFvE,wDxC.yBzA!'

def encrypt(plaintext: str, keyphrase: int, encrypt: bool) -> str:
    '''
    Using the Ceaser Cipher method to shift the alpha characters of the string 
    plaintext in lowercase by the key amount, then return the encrypted string.
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
        
        index = LIBRARY.find(plaintext[j])
        
        if index != -1:
            ciphertext += LIBRARY[(index + key) % len(LIBRARY)]
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

    print ('\n' + encrypt(plaintext, keyphrase, encrypt_toggle) + '\n')