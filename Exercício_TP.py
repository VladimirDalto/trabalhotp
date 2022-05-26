clientes = []
n_clientes = 1
import json
import os

def clear_os():
    os.system('cls')

def menu() :
    option = int(input('''
[1] - Cadastrar cliente
[2] - Consultar Clientes
[3] - Editar Cliente
[4] - Sair do programa
'''))
    clear_os()
    return option

def cadastra_cliente() :
    cliente_nome = input('Digite o nome do cliente: ')
    cliente_cep = input('Digite o cep do cliente: ')
    cliente_telefone = input('Digite o telefone do cliente: ')

    clientes_dados = {"cliente_nome": cliente_nome, "cliente_cep":cliente_cep, "cliente_telefone":cliente_telefone}
    file = open("Clientes.json", "r", encoding='utf-8')

    data = file.read()
    data = json.loads(data)
    data.append(clientes_dados)

    file = open("Clientes.json", "w+", encoding='utf-8')
    data = json.dumps(data)
    file.write(data)
    file.close()
    
    print(data)
    print('Cliente adicionado')

    clear_os()

def mostrar_cliente() :
    file = open("Clientes.json", "r", encoding='utf-8')
    data = file.read()
    clientes = json.loads(data)
    for cliente in clientes:
      print(f'''
      Nome: {cliente['cliente_nome']}
      Cep: {cliente['cliente_cep']}
      Telefone: {cliente['cliente_telefone']}''')

    
def programa() :

    while True:
        option = menu()

        if option == 1 :
            cadastra_cliente()
        if option == 2 :
            mostrar_cliente()
        if option == 4 :
          break

programa()