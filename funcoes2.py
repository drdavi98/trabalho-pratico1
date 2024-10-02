# Define a função loginUsuario que recebe o parâmetro perfil
def loginUsuario(perfil):
    # Verifica se o valor do parâmetro perfil é igual a 'admin' (ignorando maiúsculas/minúsculas)
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

# Chama a função loginUsuario com diferentes valores de parâmetro
loginUsuario('Admin')
loginUsuario('admin')
loginUsuario('User')
loginUsuario('usuário')
