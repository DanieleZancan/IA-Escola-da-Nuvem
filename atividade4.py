# Atividade 4 - IA EDN 

# 1- Calculadora de Operações Básicas:

print("1- Calculadora de Operações Básicas")

while True:
    try:
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        operador = input("Digite o operador do cálculo (+, -, / ou *): ")
        
        if operador == '+': 
            print(numero1 + numero2)
        elif operador == '-': 
            print(numero1 - numero2)
        elif operador == '/': 
            print(numero1 / numero2)
        elif operador == '*': 
            print(numero1 * numero2)
        else: 
            continue
        
        break
    except ValueError: print("Digite números válidos!")
    except ZeroDivisionError: print("Não é possível fazer divisão por zero!")

print("\n")

# 2- Calculadora Média das Notas da Turma:

print("2- Calculadora Média das Notas da Turma")

def media_notas():
    notas = []
    qtd_alunos = int(input("Digite a quantidade de alunos na turma: "))

    for i in range(qtd_alunos):
        nota = float(input(f"Digite a nota do {i + 1}º aluno: "))
        notas.append(nota)

    media = sum(notas) / len(notas)
    print(f"A média das notas da turma é: {media:.2f}")  

media_notas()  

print("\n")

# 3- Analisador de Senhas:

print("3- Analisador de Senhas Seguras")
print("Para sua senha ser segura ela deve conter:")
print("No minímo 8 caracteres;")
print("No mínimo 1 número.")

def analisador_senhas():
    senha = input("Digite uma senha e o sistema irá analisar se ela se encaixa nos padrões de senhas seguras: ")

    tamanho = len(senha) >= 8
    numero = any(char.isdigit() for char in senha)

    if tamanho and numero:
        print("Sua senha se encaixa nos padrões de segurança!")
    else:
        print("Senha inválida! A senha deve conter no mínimo 8 caracteres e conter pelo menos 1 número.")

analisador_senhas()

print("\n")

# 4- Analisador de Números Pares ou Impares:

print("4- Analisador de Números Pares ou Impares")

def classificador_numeros():
    pares = 0
    impares = 0

    while True:
        numero = input("Digite um número (ou 'sair para encerrar): ")

        if numero.lower() == 'sair':
            break

        try:
            numero_int = int(numero)
            if numero_int % 2 == 0:
                pares += 1
                print(f"O número {numero_int} é par!")
            else:
                impares += 1
                print(f"O número {numero_int} é ímpar!")
        except ValueError:
            print("Entrada inválida. Digite um número ou 'sair'.")

    print(f"Total de números pares digitados: {pares}")
    print(f"Total de números ímpares digitados: {impares}")

classificador_numeros()

