def showCursables(cursables):
    for materia in cursables:
        salida = "(" + materia.pedirCodigo() + ") " + materia.pedirNombre()
        creditos = materia.pedirCreditos()
        if (creditos > 0):
            salida2 = " (" + str(creditos) + " créditos)"
        else:
            salida2 = " (CBC)"
        print(salida + salida2)


class Cursada:
    def __init__(self, plan):
        self.plan = plan
        self.cursadas = []


    def aprobo(self, materia):

        for cursada in self.cursadas:
            if ((cursada.pedirCodigo() == materia.pedirCodigo()) & cursada.estaAprobada()):
                return True
        return False


    def consultarCreditos(self):
        creditos = 0

        if (len(self.cursadas) == 0): return 0

        for materia in self.cursadas:
            if materia.estaAprobada():
                creditos += materia.pedirCreditos()

        return creditos


    def consultarPromedio(self, *, CBC):
        notas = 0
        materias = 0

        if self.materiasCursadas(CBC = CBC) == 0: return "Aún no tiene materias cursadas."

        for materia in self.cursadas:
            if (CBC or not materia.esCBC()):
                notas += materia.pedirNota()
                materias += 1

        return notas/materias


    def consultarCursables(self):
        cursables = []

        for materia in self.plan:
            if (materia.esCursable(self.cursadas,self.consultarCreditos()) & (not self.aprobo(materia))):
                cursables.append(materia)

        showCursables(cursables)


    def cerrarMateria(self, codigo, nota):
        cerrada = False
        i = 0

        while (not cerrada and i < len(self.plan)):
            if (self.plan[i].pedirCodigo() == codigo):
                if not self.aprobo(self.plan[i]):
                    self.cursadas.append(self.plan[i].cerrar(nota))
                else:
                    return False
                cerrada = True
            i += 1

        return True


    def save(self, materia):
        return self.cursadas[materia].save()


    def materiasCursadas(self, *, CBC):
        if CBC:
            return len(self.cursadas)
        else:
            count = 0
            for materia in self.cursadas:
                if not materia.esCBC:
                    count += 1
            return count


    def obtenerMateria(self, codigo):
        for materia in self.plan:
            if (materia.pedirCodigo() == codigo):
                return materia
        return None


    def materiasAprobadas(self):
        if (len(self.cursadas) == 0):
            print("No tiene materias cursadas.")
            return None
        for materia in self.cursadas:
            print('(' + materia.pedirCodigo() + ') ' + materia.pedirNombre() + ' - Nota: ' + str(materia.pedirNota()))


    def borrarMateria(self, codigo):
        for materia in self.cursadas:
            if (materia.pedirCodigo() == codigo):
                self.cursadas.remove(materia)