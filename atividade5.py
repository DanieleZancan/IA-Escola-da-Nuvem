# Atividade 5 - IA EDN 

# 1- Calculadora Gorjeta:

print("1- Calculadora Gorjeta")

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

conta = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite o valor da porcentagem da gorjeta: "))
gorjeta = calcular_gorjeta(conta, porcentagem)

print(f"A gorjeta será de R${gorjeta:.2f}")
print("\n")

# 2- Verificador de Palavra ou Frase Palíndromo:

print("2- Verificador de Palavra ou Frase Palíndromo")

def eh_palindromo(texto):
    texto_limpo = ''.join(c.lower() for c in texto if c.isalnum())
    return texto_limpo == texto_limpo[::-1]

frase = input("Digite uma palavra ou frase: ")
if eh_palindromo(frase):
    print("SIM")
else:
    print("NÃO")
print("\n")

# 3- Calculadora de Desconto:

print("3- Calculadora de Desconto")

def calcular_desconto(preco, percentual_desconto):
    desconto = preco * (percentual_desconto / 100)
    return desconto

def calcular_preco_final(preco, desconto):
    return preco - desconto

preco_produto = float(input("Digite o preço original do produto: "))
desconto_percentual = float(input("Digite o percentual de desconto: "))

valor_desconto = calcular_desconto(preco_produto, desconto_percentual)
preco_final = calcular_preco_final(preco_produto, valor_desconto)

print(f"O valor do desconto é de: R$ {valor_desconto:.2f}")
print(f"O preço final com desconto é de: R$ {preco_final:.2f}")
print("\n")

# 4- Calculadora Dias de Vida:

print("4- Calculadora Dias de Vida")

from datetime import datetime

data_nascimento = input("Digite a data de nascimento (dd/mmm/aaaa): ")
dia, mes, ano = map(int, data_nascimento.split("/"))

data_nasc = datetime(ano, mes, dia)
data_atual = datetime.today()

dias_vida = (data_atual - data_nasc).days

print(f"Você está vivo há {dias_vida} dias!")