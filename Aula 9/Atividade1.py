# Atividde 1

GABARITO = ["B", "C", "A", "E", "D"]
RESPOSTAS = []
acertos = 0

for i in range(5):
    resposta = input(f"Digite a resposta da questão {i+1}: ").upper()
    RESPOSTAS.append(resposta)

for i in range(5):
    if RESPOSTAS[i] == GABARITO[i]:
        acertos += 1

print("Quantidade de acertos:", acertos)

