# Atividade 2   

jogadores = []

for i in range(11):
    nome = input(f"Digite o nome do jogador {i+1}: ")
    camisa = input(f"Digite o número da camisa de {nome}: ")
    jogadores.append([nome, camisa])

print("\nEscalação inicial:")
for j in jogadores:
    print("Nome:", j[0], "- Camisa:", j[1])

print("\nIntervalo do jogo - Substituições")

for i in range(3):
    posicao = int(input("Qual posição do jogador que sairá (1 a 11)? ")) - 1
    nome = input("Nome do novo jogador: ")
    camisa = input("Número da camisa: ")
    jogadores[posicao] = [nome, camisa]

print("\nEscalação atualizada:")
for j in jogadores:
    print("Nome:", j[0], "- Camisa:", j[1])