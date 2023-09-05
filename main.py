import csv

def carregar_lista():
    lista_nomes = []
    with open('lista_nomes.csv', 'r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        for linha in leitor_csv:
            lista_nomes.append(linha[0])
    return lista_nomes

def salvar_lista(lista_nomes):
    with open('lista_nomes.csv', 'w', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        for nome in lista_nomes:
            escritor_csv.writerow([nome])

def verificar_presenca(lista_nomes, nome):
    if nome in lista_nomes:
        print('\n\n\n---------------------------------------')
        print(f'{nome} Esta na lista.')
        print('---------------------------------------')
    else:
        print('\n\n\n---------------------------------------')
        print(f'{nome} nao esta na lista.')
        print('---------------------------------------')

def adicionar_nome(lista_nomes, nome):
    lista_nomes.append(nome)
    salvar_lista(lista_nomes)
    print('\n\n\n---------------------------------------')
    print(f'{nome} foi adicionado à lista.')
    print('---------------------------------------')

def remover_nome(lista_nomes, nome):
    if nome in lista_nomes:
        lista_nomes.remove(nome)
        salvar_lista(lista_nomes)
        print('\n\n\n---------------------------------------')
        print(f'{nome} foi marcado como presente.')
        print('---------------------------------------')
    else:
        print('\n\n\n---------------------------------------')
        print(f'{nome} não está na lista.')
        print('---------------------------------------')

def exibir_lista(lista_nomes):
    print('Lista de nomes:')
    for nome in lista_nomes:
        print(nome)

def menu():
    lista_nomes = carregar_lista()
    while True:
        print('\n--- Menu ---')
        print('1. Verificar nome')
        print('2. Adicionar nome')
        print('3. Marcar presenca')
        print('4. Exibir lista')
        print('5. Sair')
        escolha = input('Escolha uma opção: ')

        if escolha == '1':
            nome = input('Digite o nome para verificar presença na lista: ')
            verificar_presenca(lista_nomes, nome)
        elif escolha == '2':
            nome = input('Digite o nome para adicionar na lista: ')
            adicionar_nome(lista_nomes, nome)
        elif escolha == '3':
            nome = input('Digite o nome para marcar presenca: ')
            remover_nome(lista_nomes, nome)
        elif escolha == '4':
            exibir_lista(lista_nomes)
        elif escolha == '5':
            print('Encerrando o programa...')
            break
        else:
            print('Opção inválida. Tente novamente.')

menu()
