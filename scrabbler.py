import re

def scrabbeler(cypher:int,path:str) -> str:

    cypher_digit = re.match(r'\d{1,5}$',str(cypher))
    try:
        cypher_digit.group()
        corr_num = True
    except:
        corr_num = False
        print(f'Cypher requires at least 1 Digit and not more than 5 digit\n{"=" * 58}',
              f'\nCurrent number of digits = {len(str(cypher))}')

    if corr_num == True:
        with open(path,'r',encoding='utf-8',) as begin:
            file = begin.read()

        scrabble = [chr(ord(i) + cypher) for i in file]
        hidden = ''.join(scrabble)
        with open('hidden.txt','w',encoding='utf-8') as f:
            f.write(hidden)


def unscrabbeler(cypher:int,path:str) -> str:

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
            print('Cypher out of range')


scrabbeler(20000000,'Power.txt')
unscrabbeler(20,'hidden.txt')