#from palavras import *
#import random

palavra = 'casa'  #random.choice(palavras).lower()
letrasU = []
chances = 6
acertos = 0
corpo = [
'''
+------+
|      |
|
|
|
|
|
==========''',
'''
+------+
|      |
|      O
|
|
|
|
==========''',
'''
+------+
|      |
|      O
|      | 
|
|
|
==========''',
'''
+------+
|      |
|      O
|      |\ 
|
|
|
==========''',
'''
+------+
|      |
|      O
|     /|\ 
|
|
|
==========''',
'''
+------+
|      |
|      O
|     /|\ 
|       \_
|
|
==========''',
'''
+------+
|      |
|      O
|     /|\ 
|    _/ \_
|
|
=========='''
]

print ('')
print(f'A palavra tem {len(palavra)} Letras\ne você tem  {chances} tentativas de acerto. ')
print('')
print('-=' * 20)

while chances > -1:

    for letra in palavra:
        if letra.lower() in letrasU:
            print(letra, end=' ')
        else:
            print(' _ ', end='')
    print('')

    print('-=' * 20)
       
    
    if chances == 6 and acertos < (len(palavra)):
        print(corpo[0])
    elif chances == 5 and acertos < (len(palavra)):
        print(corpo[1])
    elif chances == 4 and acertos < (len(palavra)):
        print(corpo[2])
    elif chances == 3 and acertos < (len(palavra)):
        print(corpo[3])
    elif chances == 2 and acertos < (len(palavra)):
        print(corpo[4])
    elif chances == 1 and acertos < (len(palavra)):
        print(corpo[5])
    elif chances == 0:
        print (corpo[6])
        print('')
        print (f'FIM DE JOGO, você perdeu, a palavra era: {palavra}')
        break
    else:
        print("ganhou", palavra)
        break
        
    print('')
    if chances >=2:
        print(f'Você tem {chances} tentativas.')
    else:
        print('-='*20)
        print(f'Você tem {chances} tentativa.')
    print('')
    tentativa = (input("Escolha uma letra: "))
    
    letrasU.append(tentativa.lower())
    if tentativa.lower() not in palavra.lower():
        chances -= 1
    else:
        acertos += 1   