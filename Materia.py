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


    def esCursable(self, cursadas, creditos):
        if (len(self.correlativas) == 0): return True
        if (len(cursadas) == 0): return False

        if "créditos" in self.correlativas[0]:
            pedidos =  int(self.correlativas[0].rsplit(' ',1)[0])
            if creditos > pedidos:
                return True

        for materia in self.correlativas:
            aprobada = False
            i = 0

            while (not aprobada and i < len(cursadas)):
                if ((materia == cursadas[i].pedirCodigo()) & (cursadas[i].pedirNota() >= 4)):
                    aprobada = True
                i += 1
            if (not aprobada): return False

        return True


    def esCBC(self):
        return (self.cuatrimestre is "CBC")


    def cerrar(self, nota):
        return Cerrada(self.cuatrimestre, self.orientacion, self.opcion, self.codigo, self.nombre, self.creditos, self.correlativas, nota)



class Cerrada(Materia):
    def __init__(self, cuatrimestre, orientacion, opcion, codigo, nombre, creditos, correlativas, nota):
        super().__init__(cuatrimestre, orientacion, opcion, codigo, nombre, creditos, correlativas)
        self.nota = nota


    def pedirNota(self):
        return self.nota


    def save(self):
        correl = ''
        if (len(self.correlativas) != 0):
            for materia in self.correlativas:
                correl += (materia + '-')
                correl = correl[:-1]
        return ((self.codigo,str(self.nota)))


    def estaAprobada(self):
        return (self.nota >= 4)