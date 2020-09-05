# Programa principal
import os
from docente import Docente
from alumno import Alumno


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# carga de datos en el sistema
Alumno.cargar_alumno()
Docente.cargar_docente()
input("presionar enter")

salir = False
while not salir:
    clear()
    print("*-----------SISTEMA DOCENTES Y ALUMNOS-----------*")
    print()
    print("*Ingresar módulo")
    print()
    print("A) Módulo docente")
    print("B) Módulo alumno")
    print("Z) Salir del sistema")
    print()

    modulo = input("> ")
    
    print()

    if modulo == "A":
        while not salir:
            clear()
            print("*-----------MODULO DE DOCENTES-----------*")
            modulo = ""

            print()
            print("*Ingresar opción de módulo")
            print()
            print("A) Registar docente")
            print("B) Reporte docente")
            print("Z) retornar a menú principal")
            print()

            modulo = input("> ")

            if modulo == "A":
                docente = {}

                print()
                print("*Datos de docente")
                print()
                print("> DNI: ", end="")
                docente["dni"] = input()
                print("> Nombres: ", end="")
                docente["nombres"] = input()
                print("> Apellido paterno: ", end="")
                docente["apellido_paterno"] = input()
                print("> Apellido materno: ", end="")
                docente["apellido_materno"] = input()
                print("> Edad: ", end="")
                docente["edad"] = int(input())

                Docente.registrar_docente(docente)
                print()
                print(Docente.lista_docente)
                print("> Docente registrado correctamente. Enter para salir: ")
                input()
            elif modulo == "B":
                print()
                print("*Descarga de archivo docente (.txt)")
                print()
                Docente.reporte_docentes()
                print("> Descargar de reporte realizado. Enter para salir: ")
                input()
            elif modulo == "Z":
                modulo = ""
                break

    elif modulo == "B":
        while not salir:
            
            clear()
            print("*-----------MODULO DE ALUMNOS-----------*")
            modulo = ""
            
            print()
            print("*Ingresar opción de módulo")
            print()
            print("A) Registar alumno")
            print("B) Registar notas de alumno")
            print("C) Reporte alumno")
            print("D) Reporte notas")
            print("Z) retornar a menú principal")
            print()

            modulo = input("> ")

            if modulo == "A":
                alumno = {}

                print()
                print("*Datos de alumno")
                print()
                print("> DNI: ", end="")
                alumno["dni"] = input()
                print("> Nombres: ", end="")
                alumno["nombres"] = input()
                print("> Apellido paterno: ", end="")
                alumno["apellido_paterno"] = input()
                print("> Apellido materno: ", end="")
                alumno["apellido_materno"] = input()
                print("> Edad: ", end="")
                alumno["edad"] = int(input())

                Alumno.registrar_alumno(alumno)
                print()
                print(Alumno.lista_alumno)
                print("> Alumno registrado correctamente. Enter para salir: ")
                input()
            elif modulo == "B":
                lista_notas = []

                print()
                print("*Notas de alumno")
                print()

                print("> DNI: ", end="")
                dni = input()

                numero_nota = 0
                while True:
                    numero_nota += 1
                    print(f"> Nota{numero_nota}: ", end="")
                    nota = int(input())
                    lista_notas.append(nota)

                    if numero_nota >= 4:
                        print("Desea ingresar mas notas?")
                        respuesta = input("> Y/N: ")
                        if respuesta == "N":
                            break

                Alumno.registrar_nota_alumno(dni, lista_notas)
                print()
                print(Alumno.lista_alumno)
                print("> Nota(s) de alumno registrado correctamente. Enter para salir: ")
                input()
            elif modulo == "C":
                print()
                print("*Descarga de archivo alumno (.txt)")
                print()
                Alumno.reporte_alumnos()
                print("> Descargar de reporte realizado. Enter para salir: ")
                input()
            elif modulo == "D":
                print()
                print("*Descarga de archivo de notas de alumno (.txt)")
                print()
                Alumno.reporte_notas_alumnos()
                print("> Descargar de reporte de notas . Enter para salir: ")
                input()
            elif modulo == "Z":
                modulo = ""
                break

    elif modulo == "Z":
        salir = True
