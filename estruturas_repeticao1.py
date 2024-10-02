# Cria a variável entrada_idade e atribui a ela o valor ''
entrada_idade = ''

# Inicia o loop while que continua enquanto entrada_idade for diferente de '0'
while str(entrada_idade) != '0':
    # Solicita ao usuário que digite um número ou 0 para sair
    entrada_idade = input('Digite um número qualquer ou 0 para sair: ')
    # Imprime o número digitado pelo usuário
    print('Número digitado:', entrada_idade)
