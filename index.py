import functions

Alunos = {}
Materias = {}

while True:
    x = functions.home()

    if x == "1":
        x2 = functions.alunos()
        if x2 == "1":
            functions.cadastroaluno(Alunos)
        elif x2 == "2":
            functions.removerAluno(Alunos)
        elif x2 == "3":
            functions.listarA(Alunos)
        elif x2 == "4":  # Nova opção para ver o último aluno
            functions.ultimo_cadastrado(Alunos)

    elif x == "2":
        x2 = functions.Materias()
        if x2 == "1":
            functions.cadastroMateria(Materias)
        elif x2 == "2":
            functions.removerMateria(Materias)
        elif x2 == "3":
            functions.listarM(Materias)
        elif x2 == "4":  # Nova opção para ver a última matéria
            functions.ultimo_cadastrado(Materias)

    elif x == "3":
        break