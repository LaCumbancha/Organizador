#!usr/bin/env
# -x- coding: utf-8 -*-

import os
import Cursada
import Organizador
import Materia
from termcolor import colored


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
            exit = True
        else:
            invalid = True
            cls()

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
            scheduler.consultarPromedio()
        elif (option == "2"):
            scheduler.consultarCreditos()
        elif (option == "3"):
            scheduler.consultarMateriasCursables()
        elif (option == "4"):
            scheduler.consultarEstadoCarrera()
        elif (option == "5"):
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
            scheduler.aplazarMateria()
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

scheduler = Organizador('Organizador/plan.csv', 'Organizador/config.csv')
menu(scheduler)