class Cursada:
    def __init__(self, plan, config):
        self.plan = plan
        self.aprobadas = config

    def consultarCreditos(self):
        creditos = 0

        for materia in self.aprobadas:
            creditos += materia.pedirCreditos()

        return creditos

    def consultarPromedio(self):
        notas = 0
        materias = 0

        for materia in self.aprobadas:
            notas += materia.pedirNota()
            materias += 1

        return notas/materias

    def consultarCursables():
        #TODO