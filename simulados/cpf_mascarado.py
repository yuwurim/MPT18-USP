cpf = input()
novocpf = ''

for x in cpf:
  if int(x) %2 == 0: 
    novocpf = novocpf + '*'
  else:
    novocpf = novocpf + x 
    
print(novocpf)