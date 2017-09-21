#!usr/bin/env
# -x- coding: utf-8 -*-

import os
from termcolor import colored
from Organizador import Organizador


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu(scheduler):
    exit = False
    invalid = False

    while (not exit):
        cls()
        showMenu()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if (option == "1"):
            menuConsultas(scheduler)
        elif (option == "2"):
            menuCargar(scheduler)
        elif (option == "3"):
            scheduler.save()
            exit = True
        else:
            invalid = True
            cls()


def menuPromedio(scheduler):
    exit = False
    invalid = False

    while (not exit):
        cls()
        showMenuPromedio()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if (option == "1"):
            scheduler.consultarPromedio(CBC = False)
        elif (option == "2"):
            scheduler.consultarPromedio(CBC = True)
        elif (option == "3"):
            exit = True
        else:
            invalid = True


def menuConsultas(scheduler):
    exit = False
    invalid = False

    while (not exit):
        cls()
        showMenuConsultas()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if (option == "1"):
            menuPromedio(scheduler)
        elif (option == "2"):
            scheduler.consultarCreditos()
        elif (option == "3"):
            scheduler.consultarMateriasCursables()
        elif (option == "4"):
            scheduler.consultarMateriasAprobadas()
        elif (option == "5"):
            scheduler.consultarEstadoCarrera()
        elif (option == "6"):
            exit = True
        else:
            invalid = True


def menuCargar(scheduler):
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
            scheduler.aprobarMateria()
        elif (option == "2"):
            scheduler.borrarNota()
        elif (option == "3"):
            scheduler.aplazarMateria()
        elif (option == "4"):
            exit = True
        else:
            invalid = True


def showMenu():
    print("ORGANIZADOR DE MATERIAS v1.3\n")
    print("1. Consultas")
    print("2. Agregar Datos")
    print("3. Salir")


def showMenuConsultas():
    print("CONSULTAS:\n")
    print("1. Promedio")
    print("2. Créditos")
    print("3. Materias Cursables")
    print("4. Materias Aprobadas")
    print("5. Estado de Carrera")
    print("6. Volver")


def showMenuCargar():
    print("MODIFICACIÓN DATOS:\n")
    print("1. Materia Aprobada")
    print("2. Borrar Nota")
    print("3. Aplazo")
    print("4. Volver")


def showMenuPromedio():
    print("CONSULTA DE PROMEDIO:\n")
    print("1. Promedio sin CBC")
    print("2. Promedio con CBC")
    print("3. Volver")

scheduler = Organizador("data/plan_test.csv", "data/config.csv")
menu(scheduler)