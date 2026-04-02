# Atividade 04

print("Digite um filme/série")
FILMESÉRIE = input()

print("Digite um número de 1 a 5:")

NUMERO = int(input())

match NUMERO:
    case 1:
        print("Péssimo")
        motivo = input("Por que você achou o filme Péssimo?")
        print("Entendido, avaliação registrada")
    case 2:
        print("Ruim")
        motivo = input("Por que você achou o filme ruim?")
        print("Entendido, avaliação registrada")
    case 3:
        print("Razoável")
    case 4:
        print("Bom")
    case 5:
        print("Ótimo")
    case _:
        print("ALERTA! Número não identificado")