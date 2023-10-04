agendaDeContatos = {
        'Bob': {'telefone': '987-654-3210'},
        'Alice': {'telefone': '123-456-7890'}
        }

while True:
    opcao = int(input("Adicionar contato(1) Listar contatos(2) Pesquisar contatos(3) Sair(4):"))
    if opcao == 1:
        nomeDoNovoContato = input("Nome do novo contato:")
        telefoneDoNovoContato = input("Telefone do novo contato:")
        agendaDeContatos[nomeDoNovoContato] = {'telefone': telefoneDoNovoContato}
        print("Novo contato adicionado")
    
    elif opcao == 2:
        print(agendaDeContatos)
    
    elif opcao == 3:
        pesquisarContato = input("Nome do contato que deseja pesquisar:")
        print(agendaDeContatos[pesquisarContato])
    
    elif opcao == 4:
        break

    else: print("Valor invalido")