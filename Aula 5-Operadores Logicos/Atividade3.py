# Atividade 3
x = float(input("Digite o valor x: "))
y = float(input("Digite o valor y: "))
z = float(input("Digite o valor z: "))

if x == y == z:
    print("equilatero")
elif x == y or z == x or z == y:
    print("isosceles")
else:
    print("escaleno")