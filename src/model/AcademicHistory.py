from math import floor, ceil
from termcolor import colored


def printTitulo():
    print(colored(('\n'  + '*' * 91),'blue'))
    print(colored(("*" + " " * 36 + 'ESTADO DE CARRERA' + ' ' * 36 + '*'),'blue'))
    print(colored(('*' * 91), 'blue') + "\n")


def printBienvenida():
    print('+' * 91)
    print("|" + " " * 89 + "|")
    print("| WELCOME TO THIS BEAUTIFUL HELL" + " " * 58 + "|")
    print("|" + " " * 89 + "|")
    print('+' * 91)


def printFirmaCuatrimestre(term):
    cuatri = ""

    if term == 1:
        cuatri = "PRIMER"
    elif term == 2:
        cuatri = "SEGUNDO"
    elif term == 3:
        cuatri = "TERCER"
    elif term == 4:
        cuatri = "CUARTO"
    elif term == 5:
        cuatri = "QUINTO"
    elif term == 6:
        cuatri = "SEXTO"
    elif term == 7:
        cuatri = "SÉPTIMO"
    elif term == 8:
        cuatri = "OCTAVO"
    elif term == 9:
        cuatri = "NOVENO"
    elif term == 10:
        cuatri = "DÉCIMO"
    elif term == 11:
        cuatri = "UNDÉCIMO"
    elif term == 12:
        cuatri = "DUODÉCIMO"

    print("| " + cuatri + " CUATRIMESTRE" + " " * (75 - len(cuatri)) + "|")


def printTituloCuatrimestre(term):
    print('-' * 91)
    printFirmaCuatrimestre(term)
    print('-' * 91)
    print('| CÓDIGO | MATERIA' + ' ' * 65 + '| NOTA |')
    print('-' * 91)


class EstadoCarrera(object):


    def __init__(self, cursada):
        self.cursada = cursada


    def consultar(self):
        cuatrimestres = self.cursada.cuatrimestresCursados()
        printTitulo()
        if cuatrimestres == 0:
            printBienvenida()
        else:
            self.printCBC(cuatrimestres)
            if cuatrimestres > 2:
                self.printFIUBA(cuatrimestres)
                self.printOptativas()


    def printCBC(self, cuatrimestres):
        print('+' * 91)
        print('+' + ' ' * 43 + 'CBC' + ' ' * 43 + '+')
        print('+' * 91)

        if cuatrimestres > 2: terms = 2
        else: terms = cuatrimestres

        for term in range(1,terms+1):
            printTituloCuatrimestre(term)
            self.printCuatrimestre(term)
        print('+' * 91 + '\n')


    def printFIUBA(self, cuatrimestres):
        print('+' * 91)
        print('+' + ' ' * 42 + 'FIUBA' + ' ' * 42 + '+')
        print('+' * 91)
        for term in range(3,cuatrimestres+1):
            printTituloCuatrimestre(term)
            self.printCuatrimestre(term)
        print('+' * 91 + '\n')


    def printCuatrimestre(self, cuatri, credsOptativas = 0):
        materias = self.cursada.materiasCuatrimestre(cuatri)
        for materia in materias:

            if materia.pedirNombre().upper() == "OPTATIVAS":
                credsNecesarios = materia.pedirCreditos()

                if credsNecesarios <= credsOptativas:
                    color = "white"
                else:
                    color = "red"

                print("|        | " + colored("OPTATIVAS",color) + " " * 63 + "|  " + colored("**",color) + "  |")
                credsOptativas -= credsNecesarios

            else:

                if self.cursada.aprobo(materia):
                    color = "white"
                else:
                    color = "red"

                codigo = "|" + " " * int(ceil((8 - len(materia.pedirCodigo())) / 2)) + colored(materia.pedirCodigo(), color) + \
                         " " * int(floor((8 - len(materia.pedirCodigo())) / 2)) + "| "
                nombre = colored(materia.pedirNombre().upper(),color) + " " * (72 - len(materia.pedirNombre())) + "|"
                nota = " " * int(ceil((6 - len(str(self.cursada.pedirAprobado(materia))))/2)) + str(self.cursada.pedirAprobado(materia)) + \
                       " " * int(floor((6 - len(str(self.cursada.pedirAprobado(materia))))/2)) + "|"

                print(codigo + nombre + nota)


    def printOptativas(self):
        print("+" * 91)
        print("+" + " " * 40 + "OPTATIVAS" + " " * 40 + "+")
        print("+" * 91)
        if self.cursada.creditosOptativos() > 0:
            print("-" * 91)
            print("| CODIGO | MATERIA" + " " * 65 + "| NOTA |")
            print("-" * 91)

            for materia in self.cursada.aprobadasOptativas():
                if materia.pedirNota() >= 4:
                    color = "white"
                else:
                    color = "red"

                codigo = "|" + " " * int(ceil((8 - len(materia.pedirCodigo())) / 2)) + colored(materia.pedirCodigo(), color) + \
                         " " * int(floor((8 - len(materia.pedirCodigo())) / 2)) + "| "
                nombre = colored(materia.pedirNombre().upper(), color) + " " * (72 - len(materia.pedirNombre())) + "|"
                nota = " " * int(ceil((6 - len(str(materia.pedirNota()))) / 2)) + str(materia.pedirNota()) + \
                       " " * int(floor((6 - len(str(materia.pedirNota()))) / 2)) + "|"
                print(codigo + nombre + nota)

        else:
            print("|" + " " * 89 + "|")
            print("| AÚN NO TIENES MATERIAS OPTATIVAS CURSADAS" + " " * 47 + "|")
            print("|" + " " * 89 + "|")

        print('+' * 91 + '\n')

