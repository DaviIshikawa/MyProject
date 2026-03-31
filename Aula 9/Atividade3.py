# Lista de afazeres

tarefas = []

for x in range(5):
    tarefa = input(f"Digite a tarefa {x+1}: ")
    tarefas.append(tarefa)

print("\nLista de tarefas:")
for y in tarefas:
    print("-", y)

resposta = input("\nA primeira tarefa já foi executada? (s/n): ")

if resposta.lower() == "s":
    del(tarefas[0])
    print("Primeira tarefa removida.")

    nova = input("Digite uma nova tarefa: ")
    tarefas.append(nova)

print("\nLista atualizada:")
for y in tarefas:
    print("-", y)