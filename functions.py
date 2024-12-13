Alunos = {}
Materias = {}
cmat = 250000000


def home():
    print("----------Sistema de Gerenciamento------------")
    print("1-Gerenciar Alunos")
    print("2-Gerenciar Materias")
    return input("--> ")

def Materias(nt):
    print(nt," Materias encontradas")
    print("1-Criar Materia")
    print("2-Excluir Materia")
    print("3-Listar Materias")
    return input("--> ")

def alunos(na):
    print(na," Alunos encontrados")
    print("1-Cadastrar Aluno")
    print("2-Remover Aluno")
    print("3-Listar Alunos")
    return input("--> ")

def cadastroaluno(alunos,cmat):
    print("----------------------")
    nome = input("Nome completo do Aluno: ")
    gmail = input("Gmail do Aluno: ")
    if nome in alunos:
         print("Erro: Nome ja cadastrado")
    else:
        alunos[cmat] = {"nome": nome, "gmail": gmail}
        cmat += 1
        print("Aluno Cadastrado com Sucesso!")
        print("----------------------")

def cadastroMateria(Materias):
    print("----------------------")
    NomeMat = input("Nome da Materia: ")
    CodigoMateria = input("Codigo da Materia: ")
    if CodigoMateria in Materias:
         print("Erro: Codigo de Materia ja cadastrado")
    elif NomeMat in Materias:
        print("Erro: Materia ja Cadastrada")
    else:
        Materias[CodigoMateria] = {"materia": NomeMat}
        print("Materia Cadastrada com sucesso!")
        print("----------------------")

def removerMateria(Materias):
    print("----------------------")
    x = input("Codigo da materia que deseja remover: ")
    if x not in Materias:
         print("Erro: Codigo de Materia nao encontrado")
    else:
        nomer = Materias[x]["nome"]
        del Materias[x]
        print(f"Materia {nomer} removida com sucesso!")

def removerAluno(alunos):
    print("----------------------")
    x = input("Matricula do aluno que deseja remover: ")
    if x not in alunos:
         print("Erro: Matricula nao encontrada")
    else:
        nomer = alunos[x]["nome"]
        del alunos[x]
        print(f"Aluno {nomer} removido com sucesso!")

def listarM(dict):
    if not dict:
        print("Nenhuma Materia Cadastrada.")
    else:
        n = 0 
        for codigo in dict.items():
            print(f"{n}- Codigo:{codigo} Materia:{codigo["materia"]}  ")
            n += 1

def listarA(dict):
    if not dict:
        print("Nenhuma Aluno Cadastrado.")
    else:
        n = 0 
        for c in dict.items():
            print(f"{n}- Matricula:{c} Nome:{c["nome"]} Gmail:{c["gmail"]}  ")
            n += 1