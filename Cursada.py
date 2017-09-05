def showCursables(cursables):
    print("Materias Cursables:")
    for materia in cursables:
        print("(" + materia.pedirCodigo() + ")" + materia.pedirNombre() + "(" + materia.pedirCreditos() + " créditos)")

class Cursada:
    def __init__(self, plan):
        self.plan = plan
        self.cursadas = []


    def consultarCreditos(self):
        creditos = 0

        for materia in self.cursadas:
            if materia.estaAprobada():
                creditos += materia.pedirCreditos()

        return creditos


    def consultarPromedio(self):
        notas = 0
        materias = 0

        for materia in self.cursadas:
            notas += materia.pedirNota()
            materias += 1


        return notas/materias


    def consultarCursables(self):
        cursables = []

        for materia in self.plan:
            if materia.esCursable(self.cursadas):
                cursables.append(materia)

        showCursables(cursables)


    def cerrarMateria(self, codigo, nota):
        cerrada = False
        i = 0

        while (not cerrada and i < len(self.plan)):
            if (self.plan[i].pedirCodigo() == codigo):
                self.cursadas.append(self.plan[i].cerrar(nota))
                aprobada = True


    def save(self, materia):
        return self.cursadas[materia].save()


    def materiasCursadas(self):
        return len(self.cursadas)


    def obtenerMateria(self, codigo):
        for materia in self.plan:
            if (materia.pedirCodigo() == codigo):
                return materia