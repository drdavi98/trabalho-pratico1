# Cria a variável saida e atribui a ela o valor ''
saida = ''

# Função que realiza a adição de dois números
def adicao(a, b):
    return a + b

# Função que realiza a subtração de dois números
def subtracao(a, b):
    return a - b

# Função que realiza a multiplicação de dois números
def multiplicacao(a, b):
    return a * b

# Função que realiza a divisão de dois números
def divisao(a, b):
    if b == 0:
        return "Não foi possível realizar a divisão por 0"
    else:
        return a / b

# Função calculadora que recebe dois números e a operação desejada
def calculadora(num1, num2, operacao):
    if operacao == '+' or operacao.lower() == 'adicao':
        resultado = adicao(num1, num2)
    elif operacao == '-' or operacao.lower() == 'subtracao':
        resultado = subtracao(num1, num2)
    elif operacao == '*' or operacao.lower() == 'multiplicacao':
        resultado = multiplicacao(num1, num2)
    elif operacao == '/' or operacao.lower() == 'divisao':
        resultado = divisao(num1, num2)
    else:
        resultado = "Operação inválida"
    return resultado

# Laço while que continua enquanto saida for diferente de 'n' ou 'N'
while saida.lower() != 'n':
    # Solicita ao usuário que digite o primeiro número
    num1 = float(input('Digite o primeiro número: '))
    # Solicita ao usuário que digite o segundo número
    num2 = float(input('Digite o segundo número: '))
    # Solicita ao usuário que digite a operação desejada
    operacao = input('Digite a operação desejada (+, -, *, / ou o nome da operação): ')
    # Chama a função calculadora e armazena o resultado
    resultado = calculadora(num1, num2, operacao)
    # Imprime o resultado da operação
    print('Resultado da operação:', resultado)
    # Pergunta ao usuário se deseja continuar ou sair
    saida = input('Deseja continuar? (S/N): ')

print('Programa encerrado.')
