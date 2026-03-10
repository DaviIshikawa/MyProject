# demonstraçao de estrutura repetitiva...
contador = 0; senha = ""
while senha !="S3nh4":
    print("digite a senha:")
    senha = input()

    if senha == "S3nh4":
        print("senha correta")
        break
    else:
        print("senha incorreta")

    contador += 1
    if contador == 3:
        print("3 tentativas excedidas")
        break