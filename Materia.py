class Materia:
    def __init__(self, cuatrimestre, orientacion, opcion, codigo, nombre, creditos, correlativas):
        self.cuatrimestre = cuatrimestre
        self.orientacion = orientacion
        self.opcion = opcion
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.correlativas = correlativas

    def pedirCorrelativas(self):
        return self.correlativas

    def pedirCreditos(self):
        return self.creditos

    def pedirCodigo(self):
        return self.codigo