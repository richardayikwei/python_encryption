import re

def scrabbeler(cypher:int,path:str) -> str:
    '''
    Encrypt text using using cypher
    
    cypher (int): Possitive non zero integer
    path (str): Path to file 
    return (str) : write a text document
    '''
    if cypher == 0:
        print('No encryption applied. Exiting program...............')
        return
    elif cypher < 0:
        print('Cypher must be a positive integer')
        return
    
    cypher_digit = re.match(r'\d{1,5}$',str(cypher))
    try:
        cypher_digit.group()
        corr_num = True
    except:
        corr_num = False
        print(f'Cypher requires at least 1 Digit and not more than 5 digits\n{"=" * 58}',
              f'\nCurrent number of digits = {len(str(cypher))}')

    if corr_num == True:
        with open(path,'r',encoding='utf-8',) as begin:
            file = begin.read()

        scrabble = [chr(ord(i) + cypher) for i in file]
        hidden = ''.join(scrabble)
        with open('hidden.txt','w',encoding='utf-8') as f:
            f.write(hidden)


def unscrabbeler(cypher:int,path:str) -> str:
    '''
    Encrypt text using using cypher
    
    cypher (int): Possitive non zero integer
    path (str): Path to file 
    return (str) : write a text document
    '''

    if cypher == 0:
        print('No decryption applied. Exiting program...............')
        return
    elif cypher < 0:
        print('Cypher must be a positive integer')
        return
    
    cypher_digit = re.match(r'\d{1,5}$',str(cypher))

    try:
        cypher_digit.group()
        corr_num = True
    except:
        corr_num = False
        print(f'Cypher requires at least 1 Digit and not more than 5 digit\n{"=" * 58}',
              f'\nCurrent number of digits = {len(str(cypher))}')
        
    if corr_num == True:
        try:
            with open(path,'r',encoding='utf-8',) as begin:
                file = begin.read()
            scrabble = [chr(ord(i) - cypher) for i in file]
            revealed = ''.join(scrabble)
            with open('revealed.txt','w',encoding='utf-8') as f:
                f.write(revealed)
        except:
            print('Decryption cycpher exceeded text character range')


scrabbeler(999,'Power.txt')
unscrabbeler(999,'hidden.txt')