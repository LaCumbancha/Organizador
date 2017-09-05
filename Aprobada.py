import Materia

class Aprobada(Materia):
    def __init__(self, materia, nota):
        Materia.__init__(materia.cuatrimestre, materia.orientacion, materia.opcion, materia.codigo, materia.nombre, materia.creditos, materia.correlativas)
        self.nota = nota

    def pedirNota():
        return self.nota