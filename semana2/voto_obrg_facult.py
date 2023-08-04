idade = int(input())

if idade <= 15:
    print('Jovem demais para votar, espere até 16')
elif idade == 16 and idade == 17:
     print('Seu voto é facultativo: você pode votar ou não')
elif idade >= 18 and idade < 70:
    print('Seu voto é obrigatório')
else:
    print('Seu voto é facultativo: você pode votar ou não')