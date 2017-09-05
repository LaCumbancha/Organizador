from Materia import Materia
from Cursada import Cursada
from termcolor import colored
import csv


class Organizador:


    def __init__(self, plan, config):
        self.cursada = Cursada(self.cargarPlan(plan))
        self.cargarConfig(config)
        self.config = config


    def cargarPlan(self, route):
        plan = []
        with open(route, encoding='utf8') as csvfile:
            planreader = csv.reader(csvfile)
            for row in planreader:
                correlativas = []
                if (row[6] != "-"):
                    correlativas = row[6].split('-')
                materia = Materia(row[0], row[1], row[2], row[3], row[4], int(row[5]), correlativas)
                plan.append(materia)
        csvfile.close()
        return plan


    def cargarConfig(self, config):
        try:
            with open(config, encoding='utf8') as csvfile:
                planreader = csv.reader(csvfile)
                for row in planreader:
                    self.cursada.cerrarMateria(row[3], int(row[7]))
        except FileNotFoundError:
            csvfile = open(config, 'w')
        csvfile.close()


    def save(self):
        with open(self.config, 'w') as csvfile:
            configWriter = csv.writer(csvfile)
            for i in range(self.cursada.materiasCursadas()):
                configWriter.writerow(self.cursada.save(i))
        csvfile.close()


    def aprobarMateria(self, codigo, nota):
        self.cursada.cerrarMateria(codigo, nota)


    def aplazarMateria(self, codigo):
        self.cursada.cerrarMateria(codigo, 2)


    def consultarCursables(self):
        return self.cursada.consultarCursables()


    def consultarPromedio(self):
        return self.cursada.consultarPromedio()


    def consultarCreditos(self):
        return self.cursada.consultarCreditos()


    def consultarEstadoCarrera(self):
        print(colored("Pendiente", "blue"))