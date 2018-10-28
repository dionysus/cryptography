# ----- Caeser Cipher v02 ----- #


LIBRARY = '?aZbY1cXdW2eVfU3gTh4SiRj5QkPl6OmNn7MoLp8KqJ9rIs0HtG uFvE,wDxC.yBzA!'

def encrypt(plaintext: str, key: int) -> str:
    '''
    Using the Ceaser Cipher method to shift the alpha characters of the string 
    plaintext in lowercase by the key amount, then return the encrypted string.
    '''

    ciphertext = ''    
    
    for ch in plaintext: 
        index = LIBRARY.find(ch)
        if index != -1:
            ciphertext += LIBRARY[(index + key) % len(LIBRARY)]
        else:
            ciphertext += ch
    
    return ciphertext

while True: 
    plaintext = str(input('Enter your message: '))
    
    key = input('Enter an integer key: ')
    
    while not ((key[0] == '-' and key[1: ].isdigit()) or key.isdigit()):
        key = input('Enter an integer key: ')
    
    key = int(key)

    print ('\n' + encrypt(plaintext, key) + '\n')