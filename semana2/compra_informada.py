saldo = int(input())
compra = int(input())

if saldo >= compra:
  valor = saldo - compra
  print('se você comprar tudo o saldo será:', valor)

if saldo < compra:
  print('seu saldo é insuficiente para essa compra')