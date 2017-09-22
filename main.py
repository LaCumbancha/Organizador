#!usr/bin/env
# -x- coding: utf-8 -*-

import os
from termcolor import colored
from Organizador import Organizador


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu(organizer):
    exit_value = False
    invalid = False

    while not exit_value:
        #cls()
        showMenu()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if option == "1":
            menuConsultas(organizer)
        elif option == "2":
            menuCargar(organizer)
        elif option == "3":
            cls()
        elif option == "4":
            organizer.save()
            exit_value = True
        else:
            invalid = True
            cls()


def menuPromedio(organizer):
    exit_value = False
    invalid = False

    while not exit_value:
        #cls()
        showMenuPromedio()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if option == "1":
            organizer.consultarPromedio(CBC = False)
        elif option == "2":
            organizer.consultarPromedio(CBC = True)
        elif option == "3":
            exit_value = True
        else:
            invalid = True


def menuConsultas(organizer):
    exit_value = False
    invalid = False

    while not exit_value:
        #cls()
        showMenuConsultas()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if option == "1":
            menuPromedio(organizer)
        elif option == "2":
            organizer.consultarCreditos()
        elif option == "3":
            organizer.consultarMateriasCursables()
        elif option == "4":
            organizer.consultarMateriasAprobadas()
        elif option == "5":
            organizer.consultarEstadoCarrera()
        elif option == "6":
            exit_value = True
        else:
            invalid = True


def menuCargar(organizer):
    exit_value = False
    invalid = False

    while not exit_value:
        #cls()
        showMenuCargar()
        if invalid:
            print(colored("Opción inválida. Reingrese.","red"))
            invalid = False
        option = input()

        if option == "1":
            organizer.aprobarMateria()
        elif option == "2":
            organizer.borrarNota()
        elif option == "3":
            organizer.aplazarMateria()
        elif option == "4":
            exit_value = True
        else:
            invalid = True


def showMenu():
    print("\nORGANIZADOR DE MATERIAS v1.0\n")
    print("1. Consultas")
    print("2. Agregar Datos")
    print("3. Limpiar Pantalla")
    print("4. Salir")


def showMenuConsultas():
    print("\nCONSULTAS:\n")
    print("1. Promedio")
    print("2. Créditos")
    print("3. Materias Cursables")
    print("4. Materias Aprobadas")
    print("5. Estado de Carrera")
    print("6. Volver")


def showMenuCargar():
    print("\nMODIFICACIÓN DATOS:\n")
    print("1. Materia Aprobada")
    print("2. Borrar Nota")
    print("3. Aplazo")
    print("4. Volver")


def showMenuPromedio():
    print("\nCONSULTA DE PROMEDIO:\n")
    print("1. Promedio sin CBC")
    print("2. Promedio con CBC")
    print("3. Volver")

scheduler = Organizador("/home/cris/FIUBA/.organizador/data/plan.csv", "/home/cris/FIUBA/.organizador/data/config.csv")
menu(scheduler)