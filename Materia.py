class Materia:
    def __init__(self, cuatrimestre, orientacion, opcion, codigo, nombre, creditos, correlativas):
        self.cuatrimestre = cuatrimestre
        self.orientacion = orientacion
        self.opcion = opcion
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
        self.correlativas = correlativas


    def pedirNombre(self):
        return self.nombre


    def pedirCreditos(self):
        return self.creditos


    def pedirCodigo(self):
        return self.codigo


    def esCursable(self, aprobadas):
        cursable = True
        if (len(aprobadas) == 0): return cursable
        for materia in self.correlativas:
            aprobada = False
            i = 0
            while (not aprobada and i < len(self.correlativas)):
                if materia == self.correlativas[i].pedirCodigo():
                    aprobada = True
                i += 1
            if aprobada == False:
                cursable = False
        return cursable


    def cerrar(self, nota):
        return Cerrada(self.cuatrimestre, self.orientacion, self.opcion, self.correlativas, self.nombre, self.creditos, self.correlativas, nota)



class Cerrada(Materia):
    def __init__(self, cuatrimestre, orientacion, opcion, codigo, nombre, creditos, correlativas, nota):
        Materia.__init__(cuatrimestre, orientacion, opcion, codigo, nombre, creditos, correlativas)
        self.nota = nota

    def pedirNota(self):
        return self.nota

    def save(self):
        return self.cuatrimestre + ',' + self.orientacion + ',' + self.opcion + ',' + self.correlativas + ',' + self.nombre + ',' + \
               str(self.creditos) + ',' + self.correlativas + ',' + str(self.nota)