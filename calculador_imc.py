ls# Função para calcular o IMC
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

# Solicitar entrada do usuário para peso "ex: 73.200" e altura "ex: 1.58"
peso = float(input("Digite o seu peso em quilogramas: "))
altura = float(input("Digite a sua altura em metros: "))

# Calcular o IMC
imc = calcular_imc(peso, altura)

# Exibir o resultado
print("Seu IMC é:", imc)

# Interpretar o IMC
if imc < 18.5:
    print("Você está abaixo do peso.")
elif imc < 24.9:
    print("Seu peso está saudável.")
elif imc < 29.9:
    print("Você está com sobrepeso.")
else:
    print("Você está com obesidade.")
