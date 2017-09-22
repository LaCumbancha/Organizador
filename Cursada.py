def showCursables(cursables):
    for materia in cursables:
        salida = "(" + materia.pedirCodigo() + ") " + materia.pedirNombre()
        creditos = materia.pedirCreditos()
        if creditos > 0:
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
            if (cursada.pedirCodigo() == materia.pedirCodigo()) & cursada.estaAprobada():
                return True
        return False


    def consultarCreditos(self):
        creditos = 0

        if len(self.cursadas) == 0: return 0

        for materia in self.cursadas:
            if materia.estaAprobada:
                creditos += materia.pedirCreditos()

        return creditos


    def consultarPromedio(self, *, CBC):
        notas = 0
        materias = 0

        if self.materiasCursadas(CBC = CBC) == 0: return "Aún no tiene materias cursadas."

        for materia in self.cursadas:
            if CBC or not materia.esCBC():
                notas += materia.pedirNota()
                materias += 1

        return round(notas/materias,2)


    def consultarCursables(self):
        cursables = []

        for materia in self.plan:
            if not materia.pedirNombre().upper() == "OPTATIVAS" and materia.esCursable(self.cursadas, self.consultarCreditos()) and (not self.aprobo(materia)):
                cursables.append(materia)

        showCursables(cursables)


    def cerrarMateria(self, codigo, nota):
        cerrada = False
        i = 0

        while not cerrada and i < len(self.plan):
            if self.plan[i].pedirCodigo() == codigo:
                if not self.aprobo(self.plan[i]):
                    self.cursadas.append(self.plan[i].cerrar(nota))
                else:
                    return False
                cerrada = True
            i += 1

        return True


    def materiasCursadas(self, *, CBC):
        if CBC:
            return len(self.cursadas)
        else:
            count = 0
            for materia in self.cursadas:
                if not materia.esCBC():
                    count += 1
            return count


    def obtenerMateria(self, codigo):
        for materia in self.plan:
            if materia.pedirCodigo() == codigo:
                return materia
        return None


    def materiasAprobadas(self):
        if len(self.cursadas) == 0:
            print("No tiene materias aprobadas.")
            return None
        for materia in self.cursadas:
            print('(' + materia.pedirCodigo() + ') ' + materia.pedirNombre() + ' - Nota: ' + str(materia.pedirNota()))


    def pedirAprobado(self, buscada):
        nota = 0

        for materia in self.cursadas:
            if materia.pedirCodigo() == buscada.pedirCodigo() and materia.pedirNota() > nota:
                nota = materia.pedirNota()

        if nota == 0: nota = ""

        return nota


    def creditosOptativos(self):
        creditos = 0

        for materia in self.cursadas:
            if materia.esOptativa():
                creditos += materia.pedirCreditos()

        return creditos


    def aprobadasOptativas(self):
        optativas = []

        for materia in self.cursadas:
            if materia.esOptativa():
                optativas.append(materia)

        return optativas


    def borrarMateria(self, codigo):
        for materia in self.cursadas:
            if materia.pedirCodigo() == codigo:
                self.cursadas.remove(materia)


    def materiasCuatrimestre(self, cuatri):
        materias = []

        for materia in self.plan:
            if materia.pedirCuatrimestre() == cuatri:
                materias.append(materia)

        return materias


    def cuatrimestresCursados(self):
        cuatri = 0

        for materia in self.cursadas:
            if materia.pedirCuatrimestre() > cuatri:
                cuatri = materia.pedirCuatrimestre()

        return cuatri


    def save(self, materia):
        return self.cursadas[materia].save()