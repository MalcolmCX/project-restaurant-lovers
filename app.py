import os

restaurantes = ['Outback', 'Coco Bambu', 'Paris 6', 'Madero']

def exibir_nome_do_programa():
    print('''

██████╗░███████╗░██████╗████████╗░█████╗░██╗░░░██╗██████╗░░█████╗░███╗░░██╗████████╗
██╔══██╗██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║░░░██║██╔══██╗██╔══██╗████╗░██║╚══██╔══╝
██████╔╝█████╗░░╚█████╗░░░░██║░░░███████║██║░░░██║██████╔╝███████║██╔██╗██║░░░██║░░░
██╔══██╗██╔══╝░░░╚═══██╗░░░██║░░░██╔══██║██║░░░██║██╔══██╗██╔══██║██║╚████║░░░██║░░░
██║░░██║███████╗██████╔╝░░░██║░░░██║░░██║╚██████╔╝██║░░██║██║░░██║██║░╚███║░░░██║░░░
╚═╝░░╚═╝╚══════╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░░░╚═╝░░░

██╗░░░░░░█████╗░██╗░░░██╗███████╗██████╗░░██████╗
██║░░░░░██╔══██╗██║░░░██║██╔════╝██╔══██╗██╔════╝
██║░░░░░██║░░██║╚██╗░██╔╝█████╗░░██████╔╝╚█████╗░
██║░░░░░██║░░██║░╚████╔╝░██╔══╝░░██╔══██╗░╚═══██╗
███████╗╚█████╔╝░░╚██╔╝░░███████╗██║░░██║██████╔╝
╚══════╝░╚════╝░░░░╚═╝░░░╚══════╝╚═╝░░╚═╝╚═════╝░\n''')

def exibir_opçoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurates')
    print('3. Ativar restaurantes')
    print('4. Sair\n')

def finalizar_app():
    exibir_subtitulo ('Finalizando o app\n')

def voltar_menu_principal():
    input('\nDigite  uma tecla para voltar ao menu principal')
    main()   

def opcao_invalida():
    print('Opção Invalida!\n')
    
    voltar_menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes: \n')
    nome_do_restaurante = input ('Digite o nome do restaurante que deseja cadastrar: \n')
    restaurantes.append (nome_do_restaurante)
    print(f'\nO restaurante {nome_do_restaurante} foi cadastrado com sucesso!')
    
    voltar_menu_principal()

def listar_restaurante():
    exibir_subtitulo(' Listando os restaurantes:\n')
    
    for restaurante in restaurantes:
        print(f'{restaurante}')

    voltar_menu_principal()

def escolher_opçao():
    try:
        opçao_escolhida = int (input('Escolha uma opção: '))
        print(f'Você escolheu a opção: {opçao_escolhida}!\n')

        if opçao_escolhida == 1:
            cadastrar_restaurante()
        elif opçao_escolhida == 2:
             listar_restaurante()
        elif opçao_escolhida == 3:
            print('Ativar restaurantes')
        elif opçao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opçoes()
    escolher_opçao()
    
if __name__ == '__main__':
    main()

