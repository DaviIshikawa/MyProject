# Atividade 05

print("Digite um dia da semana")
DiasDaSemana = input

match DiasDaSemana:
    case "segunda":
        print("Estudar")
    case "terça":
        print("Jogar futebol")
    case "quarta":
        print("cozinhar")
    case "quinta":
        print("Ler")
    case "sexta":
        print("cantar")
    case "sabado":
        print("Descansar")
    case "Domingo":
        print("Ir à igreja")
    case _:
        print("ERROR")