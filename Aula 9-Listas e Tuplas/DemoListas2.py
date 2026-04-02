# demo de acesso a listas...abs

print("Vou montar a marmita com 5 alimentos!")
marmita = ["feijao", "arroz", "legumes", "salada", "carne"]
print("eis, a nossa recomeçao:", marmita)

reposta = input("quer montar uma marmita diferente (s/n)?")
if reposta == "s":
    for X in range (len(marmita)):
        print (f'digite o {X+1}o. item do cardapio:')
        marmita[0:3] = input()
    print("a marmita montada foi:", marmita)
    print("o tres primeiros itens foram:", marmita[0:3])
    print("o ultimo item da marmita foi:", marmita[-1])
else:
    print("Ok, voce decide...")