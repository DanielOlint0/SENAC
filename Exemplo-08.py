contatos = {
    'Bob': {'telefone': '987-654-3210', 'email': 'bob@email.com'},
    'Alice': {'telefone': '123-456-7890', 'email': 'alice@email.com'}
}

#01. Acessar as informações de contato de uma pessoa específica a partir do dicionário "contatos". Por exemplo, imprimir o telefone e o email de "Alice".
print(contatos['Alice'])

#02. Adicionar novas pessoas e suas informações de contato ao dicionário "contatos".
contatos['Carlos'] = {'telefone': '321-654-7890', 'email': 'carlos@email.com'}
print(contatos['Carlos'])

#03. Modificar as informações de contato de uma pessoa existente no dicionário "contatos". Por exemplo, atualizar o email de "Bob".
contatos['Bob']['email'] = 'bobinho@gmail.com'
print(contatos['Bob'])

#04. Excluir um contato específico do dicionário "contatos". Por exemplo, remover o contato de "Alice".
del contatos['Alice']
print(contatos)

#05. Desafio (+1 pt): listar todos os nomes de pessoas no dicionário "contatos" em ordem alfabética.
nomes_ordenados = sorted(list(contatos.keys()))
for nome in nomes_ordenados:
    print(nome)