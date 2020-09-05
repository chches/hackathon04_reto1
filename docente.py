# Creación de clase Docente, hereda todo de persona

import os
import shutil
from persona import Persona

class Docente(Persona):
    
    lista_docente = {}
    lista_docente["docente"] = []

    def __init__(self, dni, nombres, apellido_paterno, apellido_materno, edad):
        super().__init__(dni, nombres, apellido_paterno, apellido_materno, edad) 

    @classmethod
    def cargar_docente(cls): # self, dni, nombres, apellido_paterno, apellido_materno, edad):
        docente = {}
        list= []
        try:
            archivo = open("docente.txt", "r")
            # texto = docente["dni"] + "|" + docente["nombres"] + "|" + docente["apellido_materno"] + "|" + docente["apellido_materno"] + "|" + str(docente["edad"]) + "\n"
            for line in archivo:
                list.append(line)
            # datos_archivo = archivo.readlines()
            print(list)
            
        except Exception as e:
            print(f"error: {e}")
        finally:
            print("finalizado")
            if archivo:
                archivo.close()

    @classmethod
    def guardar_docente(cls, docente): # self, dni, nombres, apellido_paterno, apellido_materno, edad):
        try:
            archivo = open("docente.txt", "a")
            texto = docente["dni"] + "|" + docente["nombres"] + "|" + docente["apellido_paterno"] + "|" + docente["apellido_materno"] + "|" + str(docente["edad"]) + "\n"
            archivo.write(texto)
        except Exception as e:
            print(f"error: {e}")
        finally:
            print("finalizado")
            if archivo:
                archivo.close()
    
    @classmethod
    def registrar_docente(cls, docente):
        lista = [docente]
        cls.lista_docente["docente"].append(docente)
        Docente.guardar_docente(docente)

    @classmethod
    def registrar_nota_docente(cls, dni, notas):
        datos_docente = {}
        docente_encontrado = False
        lista = cls.lista_docente["docente"]
        
        for docente in lista:
            # print(f"hola {docente}")
            if docente["dni"] == dni:
                datos_docente = docente
                docente_encontrado = True
            
            if docente_encontrado:
                break

        if docente_encontrado:
            datos_docente["notas"] = notas
    
    @classmethod
    def reporte_docentes(cls):
        lista = cls.lista_docente["docente"]
        archivo = open("reporte_docentes.txt", "w")
        if lista:
            try:
                for docente in lista:
                    texto = docente["dni"] + "|" + docente["nombres"] + "|" + docente["apellido_paterno"] + "|" + docente["apellido_materno"] + "|" + str(docente["edad"]) + "\n"
                    print(texto)
                    archivo.write(texto)
            except Exception as e:
                print(f"Error {e}")
            finally:
                print("reporte finalizado")
                if archivo:
                    archivo.close()
        else:
            print("No existen docentes registrados en el sistema")



# #Sentencia de prueba de objeto
# docente_1 = Docente('45958356', 'Charly Cristian', 'Chinchay', 'Escamilo', '30')
# print(f"Docente: {docente_1.dni} - {docente_1.nombres} - {docente_1.edad}")