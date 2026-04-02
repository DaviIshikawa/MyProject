# Demonstração do uso de if/elif/else...
print("Digite a sua idade:")
IDADE = int(input())
 
if IDADE < 18:
    print("Você não é maior de idade!")
    print("Não poderá realizar as operações bancárias!")
elif IDADE >= 65:
    print("Você já é aposentado(a)!")
    print("Poderemos oferecer suporte técnico...")
else:
    print("Você é maior de idade.")
    print("Portanto, poderá realizar a operação.")

print("Obrigado por escolher os nossos serviços!")