# ----- Caeser Cipher v01 ----- #

def encrypt(msg: str, key: int) -> str:
    '''
    Using the Ceaser Cipher method to shift the alpha characters of the string 
    msg in lowercase by the key amount, then return the encrypted string.
    '''

    new_string = ''    
    
    for ch in msg: 
        if ch.isalpha():
            num = ord(ch.lower())
            new_string += chr((num - 97 + key) % 26 + 97)
        else:
            new_string += ch
    
    return new_string

while True: 
    msg = str(input('Enter your message: '))
    
    key = input('Enter an integer key: ')
    
    while not ((key[0] == '-' and key[1: ].isdigit()) or key.isdigit()):
        key = input('Enter an integer key: ')
    
    key = int(key)

    print ('\n' + encrypt(msg, key) + '\n')