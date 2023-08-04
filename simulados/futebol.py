time1 = input()
time2 = input()
pontos1 = int(input())
pontos2 = int(input())

if pontos1 > pontos2: 
    print('vitoria:', time1)
elif pontos2 > pontos1:
    print('vitoria:', time2)
elif pontos1 == pontos2:
    print('prorrogação!')
    pontosp1 = int(input())
    pontosp2 = int(input())
    if pontosp1 > pontosp2:
        print('vitoria:', time1)
    elif pontosp2 > pontosp1:
        print('vitoria:', time2)
    elif pontosp1 == pontosp2:
        print('disputa de penaltis!')