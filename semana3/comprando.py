valor = int(input())
itens = int(input()) # uma vez 
contagem_itens = 0 # contagem de itens

while valor >= itens:
    contagem_itens = contagem_itens + 1 
    valor = valor - itens
    itens = int(input()) # condição de parada tem que ser sempre a ultima coisa a ser lida no codigo
    
print('Número de itens', contagem_itens)
print('Saldo:', ('%.2f' % valor))