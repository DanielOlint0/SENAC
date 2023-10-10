alunos = {
    'Carlos' : {'Nota1' : 8.7, 'Nota2' : 9.3, 'Nota3' : 4.8, 'Frequencia' : 80},
    'Bob' : {'Nota1': 9.0, 'Nota2':  8.5, 'Nota3' : 7.0, 'Frequencia' : 97},
    'Alice': {'Nota1': 7.0, 'Nota2':  5.4, 'Nota3' : 10.0, 'Frequencia' : 75}
}

def listar_alunos():
    for nome, info in alunos.items():
        notas = {key: value for key, value in info.items() if key.startswith('Nota')}
        frequencia = info['Frequencia']
        media = calcular_media(notas)
        aprovacao = verificar_aprovacao(media, frequencia)
        print(f"\nAluno: {nome}\nNotas: {notas}\nFrequência: {frequencia}%\nMédia: {media:.2f}\nAprovação: {aprovacao}")

def calcular_media(notas):
    return sum(notas.values()) / len(notas)

def verificar_aprovacao(media, frequencia):
    if media >= 6.0 and frequencia >= 75:
        return "Aprovado"
    else:
        return "Reprovado"
    
while True:
    opcao = input("\nListar alunos'1'\nAdicionar aluno(a)'2'\nRemover aluno(a)'3'\nSair'4'\nOque deseja realizar: ")
    
    if opcao == '1':
        listar_alunos()
    
    elif opcao == '2':
        nomeAluno = input("Digite o nome do aluno: ")
        nota1 = float(input("Digite a nota 1 do aluno: "))
        nota2 = float(input("Digite a nota 2 do aluno: "))
        nota3 = float(input("Digite a nota 3 do aluno: "))
        frequencia = float(input("Digite a frequência do aluno (0 a 100): "))
        # Armazena as informações do aluno na coleção
        alunos[nomeAluno] = {'Nota1': nota1, 'Nota2': nota2,'Nota3': nota3,'Frequencia' : frequencia}
    
    elif opcao == '3':
        nomeAluno = input("Digite o nome do aluno: ")
        del alunos[nomeAluno.capitalize()]
        print("Aluno(a) excluido com sucesso\n")
    
    elif opcao == '4':
        listar_alunos()
        print("\nFinalizado")
        break
