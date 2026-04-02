# Atividade
matriz = []
soma = 0

for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"Digite um valor para [{i}][{j}]: "))
        linha.append(valor)
        soma += valor
    matriz.append(linha)

media = soma / 4

print("Matriz:")
for linha in matriz:
    print(linha)

print("Soma =", soma)
print("Média =", media)