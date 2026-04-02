# atividade 1
time = input("Digite o seu time:")
classificacao = int(input("Digite sua posiçao na tabela:"))

if classificacao == 1:
    print("campeão!")
elif classificacao >=2 and classificacao <=6:
    print("libertadores!")
elif classificacao >= 7 and classificacao <=12:
    print("Sul americana!")
else:
    print("rebaixado")