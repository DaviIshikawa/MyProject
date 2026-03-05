# Atividade 4

funcao = input("Digite sua funcao em campo: ")

if funcao == "goleiro" or funcao == "zagueiro" or funcao == "lateral":
    print("defesa")
elif funcao == "ala" or funcao == "volante" or funcao == "meia":
    print("meio campo")
elif funcao == "ponta" or funcao == "atacante" or funcao == "centroavante":
    print("ataque")
else:
    print("teimoso")