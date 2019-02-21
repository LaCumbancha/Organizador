from EstadoCarrera import EstadoCarrera
from Materia import Materia
from Cursada import Cursada
from termcolor import colored
import csv


def continuarPrograma():
    print("\nPresione ENTER para continuar...", end='', flush=True)
    input()


def cargarPlan(route):
    plan = []
    with open(route, encoding='utf8') as csvfile:
        planreader = csv.reader(csvfile)
        for row in planreader:
            correlativas = []
            if row[6] != "-":
                correlativas = row[6].split('-')
            materia = Materia(row[0], row[1], row[2], row[3], row[4], int(row[5]), correlativas)
            plan.append(materia)
    csvfile.close()
    return plan


class Organizer:


    def __init__(self, plan, config):
        self.cursada = Cursada(cargarPlan(plan))
        self.cargarConfig(config)
        self.config = config

    def cargarConfig(self, config):
        try:
            with open(config, encoding='utf8') as csvfile:
                planreader = csv.reader(csvfile)
                for row in planreader:
                    if row:
                        self.cursada.cerrarMateria(row[0], int(row[1]))
        except FileNotFoundError:
            csvfile = open(config, 'w')
        csvfile.close()


    def save(self):
        with open(self.config, 'w') as csvfile:
            configWriter = csv.writer(csvfile)
            for i in range(self.cursada.materiasCursadas(CBC = True)):
                configWriter.writerow(self.cursada.save(i))
        csvfile.close()


    def pedirCodigo(self, *, MOTIVO):
        cond = False

        while not cond:
            print("\nIngrese el Código de la Materia (presione Q para salir):")
            codigo = input().upper()

            if codigo == 'Q': return None

            materia = self.cursada.obtenerMateria(codigo)

            if materia:
                if MOTIVO == "CERRAR":
                    print("¿Cursaste " + self.cursada.obtenerMateria(codigo).pedirNombre() + "? Y/N")
                elif MOTIVO == "BORRAR":
                    print("¿Borrar " + self.cursada.obtenerMateria(codigo).pedirNombre() + "? Y/N")
                option = input()
                if option.upper() == 'Y' or option.upper() == 'YES':
                    cond = True
            else:
                print(colored("Materia no encontrada.", "red"))

        return codigo


    def aprobarMateria(self):

        codigo = self.pedirCodigo(MOTIVO = "CERRAR")
        cond = False

        if not codigo: return None

        while not cond:
            print("Ingrese nota (presione Q para salir):")
            strInput = input().upper()
            try:
                nota = int(strInput)
                if nota < 0 or nota > 10:
                    print(colored("Nota incorrecta. Reingrese.", "red"))
                else:
                    if not self.cursada.cerrarMateria(codigo, nota):
                        print(colored("Materia ya ingresada.", "red"))
                    cond = True
            except ValueError:
                if strInput == "Q":
                    cond = True
                else:
                    print(colored("Nota incorrecta. Reingrese.", "red"))

        #continuarPrograma()


    def aplazarMateria(self):
        codigo = self.pedirCodigo(MOTIVO = "CERRAR")
        if codigo: self.cursada.cerrarMateria(codigo, 2)

        #continuarPrograma()


    def borrarNota(self):
        print("\nMaterias Cargadas:")
        self.cursada.materiasAprobadas()
        if self.cursada.materiasCursadas(CBC = True) > 0:
            materia = self.pedirCodigo(MOTIVO = "BORRAR")
            self.cursada.borrarMateria(materia)

        #continuarPrograma()


    def consultarMateriasCursables(self):
        print(colored("\nMaterias Cursables:","blue"))
        self.cursada.consultarCursables()
        #continuarPrograma()


    def consultarPromedio(self, *, CBC):
        if CBC:
            print(colored("\nPromedio con CBC:", "blue"))
            print(self.cursada.consultarPromedio(CBC = CBC))
        else:
            print(colored("\nPromedio sin CBC:", "blue"))
            print(self.cursada.consultarPromedio(CBC = CBC))
        #continuarPrograma()


    def consultarCreditos(self):
        print(colored("\nCréditos acumulados:", "blue"))
        print(self.cursada.consultarCreditos())
        #continuarPrograma()


    def consultarMateriasAprobadas(self):
        print(colored("\nMaterias Aprobadas:", "blue"))
        self.cursada.materiasAprobadas()
        #continuarPrograma()


    def consultarEstadoCarrera(self):
        estado = EstadoCarrera(self.cursada)
        estado.consultar()
        #continuarPrograma()