# Função que imprime uma variável
def imprimir_variavel():
    # Cria a variável texto e atribui a ela o valor 'Olá, funções em Python'
    texto = 'Olá, funções em Python'
    # Imprime o valor da variável texto
    print(texto)

# Chama a função imprimir_variavel
imprimir_variavel()

# Cria a variável texto e atribui a ela o valor 'Olá, laço for.'
texto = 'Olá, laço for.'

# Laço for que itera sobre cada caractere em texto
for item in texto:
    print('Caractere:', item)

# Laço for que itera sobre um intervalo numérico de 1 a 10
for numero in range(1, 11):
    print('Número do intervalo:', str(numero))
