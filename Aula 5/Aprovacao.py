# Atividade feita com prof
nota = float(input("digite sua nota:"))
presenca = float(input("digite sua presença:"))

if nota >= 6 and presenca >= 75:
    print("aprovado!")
elif nota < 6 and presenca < 75:
    print("reprovado!")
else:
    print("recuperacao")
