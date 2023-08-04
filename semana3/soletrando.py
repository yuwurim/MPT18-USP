palavra = input()
letra = input()
palavra2 = '' # aqui precisa ser vazio 

while letra != '.':
  palavra2 = palavra2 + letra # aqui ele monta a palavra
  letra = input()
  
if palavra == palavra2:
  print('True')
else:
  print('False')