# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# numero1 = int(input("Digite o primeiro número:"))
# numero2 = int(input( "Digite o segundo número"))
# soma = numero1 + numero2
# print("A soma dos números é:", soma)

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
# numero = int(input("Digite um número: "))
# resto = numero % 5
# print("O resto da divisão por 5 é:", resto)

# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
# numero1 = int(input("Digite o primeiro número:"))
# numero2 = int(input( "Digite o segundo número"))
# produto = numero1 * numero2
# print("A mutiplicação dos números é:", produto)

# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
# numero1 = int(input("Digite o primeiro número:"))
# numero2 = int(input( "Digite o segundo número: "))
# divisão = numero1 / numero2
# print("A divisão dos números é:", divisão)

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
# numero = int(input("Digite um número: "))
# quadrado = numero ** 2
# print("O quadrado do número é:", quadrado)

# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
# numero1 = float(input("Digite o primeiro número flutuante: "))
# numero2 = float(input("Digite o segundo número flutuante: "))
# soma = numero1 + numero2

# print("A soma dos números flutuantes é:", soma)

# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
# numero1 = float(input("Digite o primeiro número flutuante: "))
# numero2 = float(input("Digite o segundo número flutuante: "))
# media = (numero1 + numero2) /2

# print(f"A media  dos números flutuantes, {numero1}  e {numero2},  é:", media)

# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
# base = float(input("Digite a base: "))
# expoente = float(input("Digite o expoente: "))
# potencia = base ** expoente
# print(f"A potência de {base} elevado a {expoente} é:", potencia)

# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
# celsius = float(input("Digite a temperatura em Celsius: "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"A temperatura em Fahrenheit é: {fahrenheit}")

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
# raio = float(input("Digite o raio do círculo: "))
# area = 3.14159 * (raio ** 2)
# print(f"A área do círculo com raio {raio} é: {area}")

# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
# string = input("Digite uma string: ")
# maiusculas = string.upper()
# print("A string em maiúsculas é:", maiusculas)

# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
# nome = input("Digite seu nome completo: ")
# minusculas = nome.lower()
# print(f"Seu nome em minusculas e: {minusculas}")

# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
# frase = input("Digite uma frase: ")
# frase_sem_espacos =frase.strip()
# print("A frase sem espacos: ",frase_sem_espacos)

# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
# data = input("Digite uma data no formato dd/mm/aaaa:")
# dia, mes, ano = data.split("/")
# print(f"Dia: {dia}, Mes: {mes}, Ano: {ano}")

# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
# string1 = input("Digite a primeira string: ")
# string2 = input("Digite a segunda string: ")
# juntas = string1 + string2
# print("As strings 1 re 2 juntas sao: ", juntas)


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
# expressao1 = input("Digite a primeira expessao booleana (True/False): ")
# expressao2 = input("Digite a segunda expessao booleana (True/False): ")
# logica_and = expressao1 and expressao2
# print("O resultado da operacao AND e: ", logica_and)

# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# expressao1 = input("Digite a primeira expessao booleana (True/False): ")
# expressao2 = input("Digite a segunda expessao booleana (True/False): ")
# logica_or = expressao1 or expressao2
# print("O resultado da operacao OR e: ", logica_or)

# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# booleano = input("Digite um valor booleano (True/False): ")
# inverte = not booleano
# print("O valor digitado invertido e: ", inverte)


# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
# numero1 = int(input("Digite o primeiro número:"))
# numero2 = int(input( "Digite o segundo número"))
# iguais = numero1 == numero2
# print("Os numeros sao iguais?", iguais)

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
# numero1 = int(input('Digite o primeiro numero: '))
# numero2 = int(input('Digite o segundo numero: '))
# diferentes = numero1 != numero2
# print("Os numeros sao diferentes?", diferentes)


# #### try-except e if

# 21: Conversor de Temperatura
# try:
#     celsius = float(input("Digite a temperatura em Celsius:"))
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"A temperatura em Fahrenheit é: {fahrenheit}")
# except ValueError:
#     print("Por favor, insira um valor numérico válido para a temperatura.")

# 22: Verificador de Palíndromo
numero = 23
pali = "ADA"
nao_pai= "Casa"
if isinstance(pali, str) == True: 
    string_sem_espacos = string.replace(" ", "").lower()
    if string_sem_espacos == string_sem_espacos[::-1]:
        print("A string é um palíndromo.")
    else:
        print("A string não é um palíndromo.")
else:
    print("Por favor, insira uma string válida.")
 

# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
