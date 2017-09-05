#!usr/bin/env
# -x- coding: utf-8 -*-

import os
from termcolor import colored

class Organizador:
    def __init__(self, plan, config):
        self.cursada = Cursada(self.cargarPlan(plan), self.cargarConfig(config))

    def cargarPlan(self, plan):
        #TODO

    def cargarConfig(self, config):
        #TODO

    def aprobarMateria(self, codigo, nota):
        #TODO

    def aplazarMateria(self, codigo):
        #TODO

    def consultarCursables(self):
        return self.cursada.cursables()

    def consultarPromedio(self):
        return self.cursada.promedio()

    def consultarCreditos(self):
        return self.cursada.creditos()

    def consultarEstadoCarrera(self):
        #TODO

class Cursada:
    def __init__(self, plan, config):
        self.plan = plan
        self.aprobadas = config

    def consultarCreditos(self):
        creditos = 0

        for materia in self.aprobadas:
            creditos += materia.pedirCreditos()

        return creditos

    def consultarPromedio(self):
        #TODO


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


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def consultaPromedio():
    print("Consulta de Promedio")
    input("Presione Enter para continuar")

def consultaCreditos():
    print("Consulta de Creditos")
    input("Presione Enter para continuar")

def consultaMateriasCursables():
    print("Consulta de Materias Cursables")
    input("Presione Enter para continuar")

def consultaEstadoCarrera():
    print("Consulta de Estado Carrera")
    input("Presione Enter para continuar")

def aprobar():
    print("Aprobar materia")
    input("Presione Enter para continuar")

def aplazar():
    print("Aplazar materia")
    input("Presione Enter para continuar")

def menu():
    cls()
    exit = False
    invalid = False

    while (not exit):
        showMenu()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if (option == "1"):
            menuConsultas()
        elif (option == "2"):
            menuCargar()
        elif (option == "3"):
            exit = True
        else:
            invalid = True

def menuConsultas():
    cls()
    exit = False
    invalid = False

    while (not exit):
        showMenuConsultas()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if (option == "1"):
            consultaPromedio()
        elif (option == "2"):
            consultaCreditos()
        elif (option == "3"):
            consultaMateriasCursables()
        elif (option == "4"):
            consultaEstadoCarrera()
        elif (option == "5"):
                exit = True
        else:
            invalid = True

def menuCargar():
    exit = False
    invalid = False

    while (not exit):
        cls()
        showMenuCargar()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if (option == "1"):
            aprobar()
        elif (option == "2"):
            aplazar()
        elif (option == "3"):
            exit = True
        else:
            invalid = True

def showMenu():
    print("ORGANIZADOR DE MATERIAS v1.0\n")
    print("1. Consultas")
    print("2. Agregar Datos")
    print("3. Salir")

def showMenuConsultas():
    print("CONSULTAS:\n")
    print("1. Promedio")
    print("2. Créditos")
    print("3. Materias Cursables")
    print("4. Estado de Carrera")
    print("5. Volver")

def showMenuCargar():
    print("AGREGAR DATOS:\n")
    print("1. Materia Aprobada")
    print("2. Aplazo")
    print("3. Volver")

organizador = Organizador()
menu()
