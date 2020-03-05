def agenda_completa():
    if AGENDA:
        for contato in AGENDA:
            buscar_contato(contato)
    else:
        print('NENHUM CONTATO EM SUA AGENDA!')


def buscar_contato(contato):
    try:
        print('')
        print(f'Nome: {contato.capitalize()}')
        print(f'Telefone: {AGENDA[contato]["tel"]}')
        print(f'E-mail: {AGENDA[contato]["email"]}')
        print(f'Endereço: {AGENDA[contato]["endereco"].title()}')
    except KeyError:
        print(f'O CONTATO {contato.capitalize().strip()} NÃO EXISTE NA AGENDA!')
    except:
        print('ERRO INESPERADO!')


def inserir_contato(contato):
    if contato.capitalize() not in AGENDA and contato.strip() != '':
        AGENDA[contato] = {
            'tel': str(input(f'Digite o telefone de {contato.capitalize()}: ')),
            'email': str(input(f'Digite o e-mail de {contato.capitalize()}: ')),
            'endereco': str(input(f'Digite o endereço de {contato.capitalize()}: ')),
        }
        print(f'CONTATO {contato.lower().capitalize()} ADICIONADO COM SUCESSO!')
        save()
    else:
        print('CONTATO INVÁLIDO, TALVEZ ESTE JÁ EXISTA EM SUA AGENDA!')


def editar_contato(contato):
    while True:
        print('O que deseja editar?')
        print('1 - Telefone')
        print('2 - Endereço')
        print('3 - E-mail')
        try:
            mudar = int(input())
            if mudar == 1:
                valor = str(input('Digite o novo número: '))
                AGENDA[contato.capitalize()]['tel'] = valor
                buscar_contato(nome)
                print(f'O CONTATO {contato.capitalize()} FOI EDITADO COM SUCESSO!')
                save()
                break
            elif mudar == 2:
                valor = str(input('Digite o novo endereço: '))
                AGENDA[contato.capitalize()]['endereco'] = valor
                buscar_contato(nome)
                print(f'O CONTATO {contato.capitalize()} FOI EDITADO COM SUCESSO!')
                save()
                break
            elif mudar == 3:
                valor = str(input('Digite o novo e-mail: '))
                AGENDA[contato.capitalize()]['email'] = valor
                buscar_contato(nome)
                print(f'O CONTATO {contato.capitalize()} FOI EDITADO COM SUCESSO!')
                save()
                break
            else:
                print('OPÇÃO INVÁLIDA')
        except ValueError:
            print('OPÇÃO INVÁLIDA')


def excluir_contato(contato):
    try:
        AGENDA.pop(contato.capitalize())
        print('CONTATO EXCLUÍDO COM SUCESSO!')
        save()
    except KeyError:
        print(f'O CONTATO {contato.capitalize()} NÃO EXISTE EM SUA AGENDA!')


def exportar_agenda(filename):
    try:
        with open(filename+'.csv', 'w') as file:
            for contato in AGENDA:
                tel = AGENDA[contato]['tel']
                email = AGENDA[contato]['email']
                endereco = AGENDA[contato]['endereco']
                file.write(f'{contato};{tel};{email};{endereco}\n')
            print('AGENDA EXPORTADA COM SUCESSO!')
    except:
        print('ERRO INESPERADO!')


def importar_agenda(filename):
    global AGENDA
    try:
        with open(filename+'.csv', 'r') as file:
            file = file.readlines()
            for linha, i in enumerate(file):
                contato = file[linha].split(';')
                AGENDA = {
                    contato[0]: {
                        'tel': contato[1],
                        'email': contato[2],
                        'endereco': contato[3].strip(),
                    }
                }
            print('AGENDA IMPORTADA COM SUCESSO!')
    except FileNotFoundError:
        print('ARQUIVO NÃO ENCONTRADO!')
    except:
        print('ERRO INESPERADO!')


def save():
    exportar_agenda('database')


def load():
    importar_agenda('database')


AGENDA = dict()
load()
while True:
    print('')
    print('===============MENU==============')
    print('1 - Ver Agenda')
    print('2 - Buscar contato')
    print('3 - Adicionar contato')
    print('4 - Editar contato')
    print('5 - Excluir contato')
    print('6 - Exportar Agenda')
    print('7 - Importar Agenda')
    print('0 - Sair')
    print('')
    try:
        opcao = int(input('Escolha uma opção: '))
        if opcao == 1:
            agenda_completa()
        elif opcao == 2:
            nome = str(input('Digite o nome do contato: '))
            buscar_contato(nome)
        elif opcao == 3:
            nome = str(input('Digite o nome do contato: '))
            inserir_contato(nome)
            buscar_contato(nome)
        elif opcao == 4:
            nome = str(input('Digite o nome do contato: '))
            buscar_contato(nome)
            editar_contato(nome)
        elif opcao == 5:
            nome = str(input('Digite o nome do contato: '))
            excluir_contato(nome)
        elif opcao == 6:
            filename = str(input('Digite o nome do arquivo: '))
            exportar_agenda(filename)
        elif opcao == 7:
            filename = str(input('Digite o nome do arquivo: '))
            importar_agenda(filename)
        elif opcao == 0:
            break
    except ValueError:
        print('DIGITE UMA OPÇÃO VÁLIDA!')
    except KeyboardInterrupt:
        print('\nFinalizando...')
        break
    except:
        print('ERRO INESPERADO!')
