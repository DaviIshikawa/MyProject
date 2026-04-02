# demonstraçao de matrizes em python
print("eis, o telado numerico do terminal")
teclado = [["1", "2", "3"],
           ["4", "5", "6"],
           ["7", "8", "9"],
           ["0", "*", "#"]]
senha = []

print("digite sua senha de 4 digitos")
for x in range(0, 4):
    senha.append(input(f'digite o digito {x+1}: '))

for x in range(0, 4):
    for y in range(0, 3):
        for z in range(0, 3):
            if teclado[x][y] == senha[z]:
                teclado[x][y] = "x"

print("eis, a senha digitada: ", senha)
print("confira,as tecla acionadas:")
for listas in teclado:
    print(listas)