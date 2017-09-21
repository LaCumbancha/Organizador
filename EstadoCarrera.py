from Materia import Materia
from Cursada import Cursada
from math import floor, ceil
from termcolor import colored

class EstadoCarrera(object):


    def __init__(self, cursada):
        self.cursada = cursada


    def printTitulo(self):
        print('*' * 91)
        print('*' * 3 + ' ' * 34 + colored('ESTADO DE CARRERA','blue') + ' ' * 34 + '*' * 3)
        print('*' * 91)
        print('\n')

    def printCBC(self, cuatrimestres):
        print('+' * 91)
        print('|' + ' ' * 43 + 'CBC' + ' ' * 43 + '|')
        print('+' * 91)
        for term in range(1,cuatrimestres+1):
            print('-' * 91)
            print('| CODIGO | MATERIA' + ' ' * 65 + '| NOTA |')
            print('-' * 91)
            self.printCuatrimestre(term)
        print('+' * 91 + '\n')

    def printFIUBA(self, cuatrimestres):
        print('+' * 91)
        print('|' + ' ' * 42 + 'FIUBA' + ' ' * 42 + '|')
        print('+' * 91)
        for term in range(3,cuatrimestres+1):
            print('-' * 91)
            print('| CODIGO | MATERIA' + ' ' * 65 + '| NOTA |')
            print('-' * 91)
            self.printCuatrimestre(term)
        print('+' * 91 + '\n')


    def printCuatrimestre(self, cuatri):
        materias = self.cursada.finalCuatrimestre(cuatri)

        for materia in materias:
            if materia.pedirNota() >= 4:
                color = 'white'
            else:
                color = 'red'

            print('|' + ' ' * int(ceil((8 - len(materia.pedirCodigo()))/2)) + colored(materia.pedirCodigo(),color) +
                  ' ' * int(floor((8 - len(materia.pedirCodigo))/2)) +  '| ' + colored(materia.pedirNombre().upper(),color) +
                  ' ' * (72 - len(materia.pedirNombre)) + '|' + ' ' * int(ceil(6 - len(str(materia.pedirNota())))) + str(materia.pedirNota()) +
                  ' ' * int(floor(6 - len(str(materia.pedirNota())))) * '|')

        print('-' * 91)