problemas = int(input())
situacao = ''
aceitos = 0  
submissoes = 0 

while situacao != 'timeout' and problemas>aceitos:
    situacao = input()
    if situacao!= 'timeout':
        submissoes = submissoes + 1 
    if situacao == 'accepted':
        aceitos = aceitos + 1
        
print('submissoes:', submissoes)
print('aceitos:', aceitos)