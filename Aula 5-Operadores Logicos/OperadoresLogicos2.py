# Demo 2
TEMPO = input ("Qual a melhor meterológica?")
RESERVA = input("Tem algum dinheirinho na conta?")

if TEMPO == "sol" and RESERVA == "sim":
    print("Dá para ir à praia!")

if not TEMPO == "sol" and RESERVA == "sim":
    print("Comprar pizza e assstir Netflix!")

if TEMPO == "sol" or RESERVA == "não":
    print("Vamos passear de bicicleta")

