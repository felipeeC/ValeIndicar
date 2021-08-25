from pip._vendor.distlib.compat import raw_input

identificador=0

def main():
    pessoas = []
    while True:
        exibir_menu()
        opcao = int(input('Opção? '))
        if opcao == 1:
            cadastrar(pessoas)
        elif opcao == 2:
            listar(pessoas)
        elif opcao == 3:
            buscar(pessoas)
        elif opcao == 4:
            buscarPorNome(pessoas)
        else:
            print('Opção inválida')

def exibir_menu():
    print('''Escolha uma opção:

    1. Cadastrar uma pessoa
    2. Listar pessoas cadastradas
    3. Procurar pessoa por id
    4. Procurar pessoa por nome
    ''')

def cadastrar(pessoas):
    identificador = len(pessoas) + 1
    nome = raw_input('Nome? ').upper()
    idade = int(input('Idade? '))

    pessoas.append((identificador, nome, idade))

def listar(pessoas):
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        print(f'Nome: {nome}, idade: {idade}, id: {identificador}')

def buscar(pessoas):
    identificador_desejado = int(input('Id? '))
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        if identificador == identificador_desejado:
            print(f'Nome: {nome}, idade: {idade}, id: {identificador}')
            break
    else:
        print(f'Pessoa com id {identificador_desejado} não encontrada')

def buscarPorNome(pessoas):
    nome_desejado = raw_input('Nome? ').upper()
    for pessoa in pessoas:
        identificador, nome, idade = pessoa
        if nome == nome_desejado:
            print(f'Nome: {nome}, idade: {idade}, id: {identificador}')
            break
    else:
        print(f'Pessoa com o Nome {nome_desejado} não encontrada')



if __name__ == '__main__':
    main()


