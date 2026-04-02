# Desafio
idade = int(input("qual é a idade: "))
inss = int (input("qt. anos de contribuição: "))
insalubre = input("Em condições insalubres(s/n)? ")

if insalubre == "s":
    if inss >= 25:
        print("aposentadoria especial!")
    else:
        print(f"faltam {25 - inss} anos para se aposentar...")
    
else:
    if idade >= 65 and inss >= 35:
        print("Aposentadoria normal.")
    else:
        print("Falta atender aos requisitos...")