# atividade 1

Valor = int(input("Digite um número entre 0 e 25: "))

if Valor < 0 or Valor > 25:
    print("Valor inválido! Digite um número entre 0 e 25.")
else:
    fatorial = 1
    
    for i in range(1, Valor + 1):
        fatorial *= i
    
    print(f"O fatorial de {Valor} é {fatorial}")