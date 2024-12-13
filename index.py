import functions

Alunos = {}
Materias = {}
cmat = 250000000


while True:

    x = functions.home()
    if x == "1":
        x2 = functions.alunos(len(Alunos))
        if x2 == "1":
            cmat = functions.cadastroaluno(Alunos,cmat)
        elif x2 == "2":
            functions.removerAluno(Alunos)
        elif x2 == "3":
            functions.listarA(Alunos)
    elif x == "2":
        x2 = functions.Materias(len(Materias))
        if x2 == "1":
            functions.cadastroMateria(Materias)
        elif x2 == "2":
            functions.removerMateria(Materias)
        elif x2 == "3":
            functions.listarM(Materias)
    elif x == "3":
        break