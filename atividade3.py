# Atividade 3 - IA EDN 

# 1- Classificador de Idade:

print("1- Classificador de Idade:")
idade = int(input("Digite em numeros a sua idade: "))

if 0 <= idade <= 12:
    print("Com a sua idade, você está classificado como *criança*.")
elif 13 <= idade <= 17:
    print("Com a sua idade, você está classificado como *adolescente*.")
elif 18 <= idade <= 59:
    print("Com a sua idade, você está classificado como *adulto*.")
elif idade >= 60:
    print("Com a sua idade, você está classificado como *idoso*.")
else:
    print("A idade que você digitou não corresponde ao nosso banco de dados, por favor, digite um valor aceitável!")

print("\n")

# 2 - Calculadora de IMC:

print("2- Calculadora de IMC:")
peso = float(input("Digite o peso em kg para o cálculo: "))
altura = float(input("Digite sua altura em metros para o cálculo: "))

if peso <= 0 or altura <= 0:
    print("Erro! Peso e altura devem ser maiores que zero.")
else:
    imc = peso / (altura ** 2)

    if imc <= 18.5:
        classificacao = "abaixo do peso"
    elif imc <= 25:
        classificacao = "peso normal"
    elif imc <= 30:
        classificacao = "sobrepeso"
    else:
        classificacao = "obeso"

    print(f"De acordo com o cálculo, seu IMC é de {imc:.2f}, você está classificado como *{classificacao}*!")

print("\n")

# 3 - Conversor de Temperatura:

print("3- Conversor de Temperatura:")
temperatura = float(input("Digite a temperatura com casas decimais: "))
tipo = input("Digite em qual tipo de temperatura você está colocando para convertemos para outra (C = Celsius, F = Fahrenheit e K = Kelvin): ")

tipo = tipo.strip().upper()

if tipo not in ["C", "F", "K"]:
    print("Erro! Digite C, F ou K para o tipo de temperatura.")
else:
    if tipo == "C":
        fahrenheit = temperatura * 9/5 + 32
        kelvin = temperatura + 273.15

        print(f"A temperatura {temperatura:.2f}ºC equivalem a {fahrenheit:.2f}ºF")
        print(f"A temperatura {temperatura:.2f}ºC equivalem a {kelvin:.2f}°K")
    elif tipo == "F":
        celsius = (temperatura - 32) * 5/9
        kelvin = celsius + 273.15

        print(f"A temperatura {temperatura:.2f}ºF equivalem a {celsius:.2f}ºC")
        print(f"A temperatura {temperatura:.2f}ºF equivalem a {kelvin:.2f}°K")

    elif tipo == "K":
        celsius = temperatura - 273.15
        fahrenheit = (celsius * 9/5) + 32

        print(f"A temperatura {temperatura:.2f}ºK equivalem a {celsius:.2f}ºC")
        print(f"A temperatura {temperatura:.2f}ºK equivalem a {fahrenheit:.2f}°F")

print("\n")

# 4 - Verificador de Ano Bissexto:

print("4- Verificador de Ano Bissexto:")
ano = int(input("Digite um ano para o cálculo: "))

if (ano % 400 == 0):
    print(f"O ano {ano} é bissexto!")
elif (ano % 100 == 0):
    print(f"O ano {ano} não é bissexto!")
elif (ano % 4 == 0):
    print(f"O ano {ano} é bissexto!")
else:
    print(f"O ano {ano} não é bissexto!")






