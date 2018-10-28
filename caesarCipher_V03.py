# ----- Caeser Cipher v03 ----- #


LIBRARY = '?aZbY1cXdW2eVfU3gTh4SiRj5QkPl6OmNn7MoLp8KqJ9rIs0HtG uFvE,wDxC.yBzA!'

def encrypt(plaintext: str, keyphrase: int) -> str:
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
        
        index = LIBRARY.find(plaintext[j])
        
        if index != -1:
            ciphertext += LIBRARY[(index + key) % len(LIBRARY)]
        else:
            ciphertext += plaintext[j]
            
        j += 1
    
    return ciphertext

while True: 
    plaintext = str(input('Enter your message: '))
    
    while True:
        key = input('Enter a keyphrase: ')
        
        if not key.isalnum():
            print('Please use only letters a-Z and numbers 0-9.')
        
        if len(key) < 8:
            print('Key must be at least 8 characters long.')
        
        if key.isalnum() and len(key) >= 8:
            break

    print ('\n' + encrypt(plaintext, key) + '\n')