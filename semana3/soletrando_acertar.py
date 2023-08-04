palavra = input()
letra = input()
verificacao = False 
palavra2 = ''

while verificacao != True:
    palavra2 = palavra2 + letra
    letra = input()
    if letra =='.':
        if palavra2 == palavra:
            print('8-)')
            verificacao = True
        else:
          print('8-|')
          palavra2 = ''
          letra = ''