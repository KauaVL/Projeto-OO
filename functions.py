class Pessoa:
    def __init__(self,nome,gmail):
        self.__nome = nome
        self.__gmail = gmail

    def get_nome(self):
        return self.__nome
        
    def get_gmail(self):
        return self.__gmail


class Aluno(Pessoa):

    __mat = 250000000

    def __init__(self,nome,gmail):
        super().__init__(nome,gmail)
        self.__matricula = Aluno.__mat
        Aluno.__mat += 1
    
    def get_matricula(self):
        return self.__matricula
    
    def exibir(self):  
        print(f"Aluno: {self.get_nome()} - Matrícula: {self.__matricula}")
    

class Materia():
    def __init__(self,nome,codigo):
        self.__codigo = codigo
        self.__nome = nome
    
    def get_codigo(self):
        return self.__codigo
    
    def get_nome(self):
        return self.__nome
    
    def exibir(self):  
        print(f"Materia: {self.get_nome()} - Código: {self.__codigo}")


def home():
    print("----------Sistema de Gerenciamento------------")
    print("1 - Gerenciar Alunos")
    print("2 - Gerenciar Materias")
    print("3 - Sair") 
    return input("--> ")

def Materias():
    print("----------------------")
    print("1 - Cadastrar Materia")
    print("2 - Excluir Materia")
    print("3 - Listar Materias")
    print("4 - Exibir Última Materia Cadastrada")
    return input("--> ")


def alunos():
    print("----------------------")
    print("1 - Cadastrar Aluno")
    print("2 - Remover Aluno")
    print("3 - Listar Alunos")
    print("4 - Exibir Último Aluno Cadastrado")
    return input("--> ")


def cadastroaluno(alunos):
    print("----------------------")
    nome = input("Nome completo do Aluno: ")
    gmail = input("Gmail do Aluno: ")

    for aluno in alunos.values():
        if aluno.get_nome() == nome:
            print("Erro: Nome já cadastrado")
            print("----------------------")
            return  

    novo_aluno = Aluno(nome , gmail)
    alunos[novo_aluno.get_matricula()] = novo_aluno
    print(f"Aluno Cadastrado com Sucesso! Matrícula: {novo_aluno.get_matricula()}")
    print("----------------------")
    
    return 

def cadastroMateria(Materias):
    print("----------------------")
    NomeMat = input("Nome da Materia: ")
    CodigoMateria = input("Codigo da Materia: ")
    if CodigoMateria in Materias:
         print("Erro: Codigo de Materia ja cadastrado")
    else:
        nova_materia = Materia(NomeMat, CodigoMateria)
        Materias[CodigoMateria] = nova_materia
        print("Materia Cadastrada com sucesso!")
        print("----------------------")

def removerMateria(Materias):
    print("----------------------")
    x = input("Codigo da materia que deseja remover: ")
    if x not in Materias:
         print("Erro: Codigo de Materia nao encontrado")
    else:
        nomer = Materias[x].get_nome()
        del Materias[x]
        print(f"Materia {nomer} removida com sucesso!")

def removerAluno(alunos):
    print("----------------------")
    x = input("Matricula do aluno que deseja remover: ")
    if int(x) not in alunos:
         print("Erro: Matricula nao encontrada")
    else:
        nomer = alunos[int(x)].get_nome()
        del alunos[int(x)]
        print(f"Aluno {nomer} removido com sucesso!")

def listarM(dict):
    if not dict:
        print("Nenhuma Materia Cadastrada.")
    else:
        n = 0 
        for materia in dict.values():
            print(f"{n} - Codigo:{materia.get_codigo()}   Materia:{materia.get_nome()}  ")
            n += 1

def listarA(dict):
    if not dict:
        print("Nenhuma Aluno Cadastrado.")
    else:
        n = 1
        for dados in dict.values():
            print(f"{n} - Matricula:{dados.get_matricula()} Nome:{dados.get_nome()} Gmail:{dados.get_gmail()} \n")
            n += 1

def ultimo_cadastrado(colecao):
    if colecao:
        ultimo_item = list(colecao.values())[-1] 
        ultimo_item.exibir()  
    else:
        print("Nenhum item cadastrado.")