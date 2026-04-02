# Atividade 01

print("Digite o seu saldo atual:")
Saldo = float(input())

print("Digite o valor do produto que deseja comprar:")
Produto = float(input())

if Saldo >= Produto:
    print("Parabéns pela compra!")
else:
    print("Você não possui saldo suficiente para realizar esta compra.")
    print("Você nao poderá relizar está compra, sinto muito...")
