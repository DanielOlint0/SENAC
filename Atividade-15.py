class Aluno:
    def __init__(self, nome, matriculas):
        self.__nome = nome
        self.__matriculas = matriculas

    def get_nome(self):
        return self.__nome
   
    def set_nome(self, valor):
        self.__nome = valor

    def get_matriculas(self):
        return self.__matriculas

    def set_matriculas(self, valor):
        self.__matriculas = valor

    def adicionar_curso(self, curso):
        if len(self.__matriculas) < 2:
            self.__matriculas.append(curso)
        else:
            print(f"O aluno {self.__nome} já está matriculado em 2 cursos e não pode ser matriculado em mais cursos.")

    def apresentar(self):
        return f"Aluno: {self.__nome}"

class Professor:
    def __init__(self, nome, valorHora, disciplina):
        self.__nome = nome
        self.__valorHora = valorHora
        self.__disciplina = disciplina
        self.__matriculas = []

    def get_nome(self):
        return self.__nome

    def get_valorHora(self):
        return self.__valorHora

    def get_disciplina(self):
        return self.__disciplina
    
    def get_matriculas(self):
        return self.__matriculas

    def adicionar_curso(self, curso):
        if len(self.__matriculas) < 1:
            self.__matriculas.append(curso)
        else:
            print(f"O professor {self.__nome} já está matriculado em 1 curso e não pode ser matriculado em mais cursos.")

    def apresentar(self):
        return f"Professor: {self.__nome}, Disciplina: {self.__disciplina}"

class Curso:
    def __init__(self, nome, alunos, professores, cargaHorariaSemana, quantidadeDeAulasPorSemana):
        self.__nome = nome
        self.__alunos = alunos
        self.__professores = professores
        self.__cargaHorariaSemana = cargaHorariaSemana
        self.__quantidadeDeAulasPorSemana = quantidadeDeAulasPorSemana

    def get_nome(self):
        return self.__nome
    
    def get_quantidadeDeAulasPorSemana(self):
        return self.__quantidadeDeAulasPorSemana

    def get_alunos(self):
        return self.__alunos
    
    def get_professores(self):
        return self.__professores
    
    def set_professores(self, valor):
        self.__professores = valor

    def criar_curso(self, nome, alunos, professores, cargaHorariaSemana, quantidadeDeAulasPorSemana):
        if len(self.__alunos) > 0 and self.__cargaHorariaSemana/self.__quantidadeDeAulasPorSemana <= 40:
            self.__nome = nome
            self.__alunos = alunos
            self.__professores = professores
            self.__cargaHorariaSemana = cargaHorariaSemana
            self.__quantidadeDeAulasPorSemana = quantidadeDeAulasPorSemana
        else: 
            return print("O curso nao pode ser criado")

    def horas_por_semana(self):
        if self.__cargaHorariaSemana/self.__quantidadeDeAulasPorSemana == 40:
                self.__matriculas.append(Curso)
                self.__carga_horaria_semana += Curso.get_carga_horaria()
                Curso.adicionar_professor(self)
        else:
            print(f"O professor {self.__nome} já atingiu a carga horária máxima de 40 horas por semana.")          

    def adicionar_aluno(self, aluno):
        self.__alunos.append(aluno)
        aluno.adicionar_curso(self)
        
    def listar_alunos(self):
        return [aluno.apresentar() for aluno in self.__alunos]

    def apresentar_curso(self):
        lista_professores = [professor.apresentar() for professor in self.__professores]
        return f"Curso: {self.__nome}\nProfessores: {', '.join(lista_professores)}\nAlunos matriculados:\n{', '.join(self.listar_alunos())}"

professor1 = Professor("Joao", 10, ["Matemática", "Física"])
professor2 = Professor("Pedro", 12, ["Redes"])
aluno1 = Aluno("Alice", ["Matemática"])
aluno2 = Aluno("Bob", ["Física"])
nomeAluno = input("Nome do aluno(a): ")
aluno3 = Aluno(nomeAluno, [])

curso_matematica = Curso("Matemática Básica", [], [professor1], 76, 70)
curso_matematica.criar_curso("Matemática Básica", [], [professor1], 76, 70)
curso_matematica.adicionar_aluno(aluno1)  
curso_matematica.adicionar_aluno(aluno2)  
curso_matematica.adicionar_aluno(aluno1) 
curso_matematica.adicionar_aluno(aluno3)
curso_matematica.adicionar_aluno(professor2)
curso_matematica.adicionar_aluno(professor2)
curso_matematica.horas_por_semana()