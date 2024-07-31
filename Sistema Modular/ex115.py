opcao = 0
pessoas = []
arquivo = 'pasta.txt'

while True:
    print('-='*45)
    print('Seja bem vindo a página de cadastro de clientes, selecione a ação que deseja realizar!')
    print('-='*45)
    while True:
        opcao = int(input('1) Cadastrar nova pessoa\n2) Listar todas as pessoas cadastradas\n'))
        if opcao != 1 and opcao != 2:
            print('Opção inváida!')
        else:
            break

    if opcao == 1:
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        pessoa = {'Nome': nome, 'Idade': idade}
        pessoas.append(pessoa)
        with open (arquivo, 'a') as file:
            file.write(f'{nome}, {idade}\n')
        nada = str(input('Cadastro realizado com sucesso! Aperte enter para continuar.'))

    if opcao == 2:
        with open (arquivo, 'r') as file:
            conteudo = file.readlines()

            for linha in conteudo:
                print(linha.strip())

        nada = str(input('Leitura feita com sucesso! Aperte enter para continuar.'))