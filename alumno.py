# Creación de clase Alumno heredado de Persona
import os
import shutil
import persona

class Alumno(persona.Persona):

    lista_alumno = {}
    lista_alumno["alumno"] = []

    def __init__(self, dni, nombres, apellido_paterno, apellido_materno, edad, notas):
        super().__init__(dni, nombres, apellido_paterno, apellido_materno, edad)
        self.notas = notas

    @classmethod
    def cargar_alumno(cls): # self, dni, nombres, apellido_paterno, apellido_materno, edad):
        alumno = {}
        try:
            archivo = open("alumno.txt", "r")
            # texto = alumno["dni"] + "|" + alumno["nombres"] + "|" + alumno["apellido_materno"] + "|" + alumno["apellido_materno"] + "|" + str(alumno["edad"]) + "\n"
            datos_archivo = archivo.read().splitlines()
            for registro in datos_archivo:
                campos = registro.split("|")
                alumno = {}
                index = 0
                for campo in campos:
                    index += 1
                    if index == 1:
                        alumno["dni"] = campo
                    elif index == 2:
                        alumno["nombres"] = campo
                    elif index == 3:
                        alumno["apellido_paterno"] = campo
                    elif index == 4:
                        alumno["apellido_materno"] = campo
                    elif index == 5:
                        alumno["edad"] = int(campo)
                    elif index == 6:
                        alumno["notas"] = campo
                    
                cls.lista_alumno["alumno"].append(alumno)

            print(cls.lista_alumno)

        except Exception as e:
            print(f"error: {e}")
        finally:
            print("finalizado")
            if archivo:
                archivo.close()
    
    @classmethod
    def guardar_alumno(cls, alumno): # self, dni, nombres, apellido_paterno, apellido_materno, edad):
        try:
            archivo = open("alumno.txt", "a")
            texto = alumno["dni"] + "|" + alumno["nombres"] + "|" + alumno["apellido_paterno"] + "|" + alumno["apellido_materno"] + "|" + str(alumno["edad"]) + "\n"
            archivo.write(texto)
        except Exception as e:
            print(f"error: {e}")
        finally:
            print("finalizado")
            if archivo:
                archivo.close()
    
    @classmethod
    def registrar_alumno(cls, alumno):
        lista = [alumno]
        cls.lista_alumno["alumno"].append(alumno)
        Alumno.guardar_alumno(alumno)

    @classmethod
    def registrar_nota_alumno(cls, dni, notas):
        datos_alumno = {}
        alumno_encontrado = False
        lista = cls.lista_alumno["alumno"]
        
        for alumno in lista:
            # print(f"hola {alumno}")
            if alumno["dni"] == dni:
                datos_alumno = alumno
                alumno_encontrado = True
            
            if alumno_encontrado:
                break

        if alumno_encontrado:
            datos_alumno["notas"] = notas
    
    @classmethod
    def reporte_notas_alumnos(cls):
        lista = cls.lista_alumno["alumno"]
        lista_reporte_notas = Alumno.obtener_notas_alumnos(lista)
        archivo = open("reporte_notas_alumno.txt", "w")
        if lista_reporte_notas:
            try:
                for alumno in lista_reporte_notas:
                    texto = alumno["dni"] + "|" + alumno["nombres"] + "|" + alumno["apellido_materno"] + "|" + alumno["apellido_materno"] + "|" + str(alumno["edad"]) + "|" + str(alumno["nota_min"]) + "|" + str(alumno["nota_max"]) + "|" + str(alumno["nota_promedio"]) + "\n"
                    print(texto)
                    archivo.write(texto)
            except Exception as e:
                print(f"Error {e}")
            finally:
                print("reporte finalizado")
                if archivo:
                    archivo.close()
        else:
            print("Alumnos sin notas cargadas")
    
    @staticmethod
    def obtener_notas_alumnos(alumnos):
        lista_alumnos = []
        datos_alumno = {}
        print("Imprimiendo datos de alumunos: ME->obtener_notas_alumnos")
        print(alumnos)
        for alumno in alumnos:
            if "notas" in alumno:
                notas = alumno["notas"]
                if notas:
                    nota_min = min(notas)
                    nota_max = max(notas)
                    nota_promedio = round(sum(notas)/len(notas))

                    datos_alumno = alumno
                    datos_alumno.pop("notas")
                    datos_alumno["nota_min"] = nota_min
                    datos_alumno["nota_max"] = nota_max
                    datos_alumno["nota_promedio"] = nota_promedio
                    lista_alumnos.append(datos_alumno)
                

        print("Imprimiendo resultado de alumnos: ME->obtener_notas_alumnos")
        print(lista_alumnos)
        if lista_alumnos:
            return lista_alumnos

    @classmethod
    def reporte_alumnos(cls):
        lista = cls.lista_alumno["alumno"]
        archivo = open("reporte_alumnos.txt", "w")
        if lista:
            try:
                for alumno in lista:
                    texto = alumno["dni"] + "|" + alumno["nombres"] + "|" + alumno["apellido_paterno"] + "|" + alumno["apellido_materno"] + "|" + str(alumno["edad"]) + "\n"
                    print(texto)
                    archivo.write(texto)
            except Exception as e:
                print(f"Error {e}")
            finally:
                print("reporte finalizado")
                if archivo:
                    archivo.close()
        else:
            print("No existen alumnos registrados en el sistema")


# # Sentencias de pruebas para mostrar alumnos.
# alumno_1 = {
#     "dni" : "45958356",
#     "nombres": "Charly Cristian",
#     "apellido_paterno" : "Chinchay",
#     "apellido_materno" : "Escamilo",
#     "edad" : 30,
#     }
# Alumno.registrar_alumno(alumno_1)

# alumno_2 = {
#     "dni" : "48475006",
#     "nombres": "Grecia Edith",
#     "apellido_paterno" : "Ayala",
#     "apellido_materno" : "Asipali",
#     "edad" : 26
#     }
# Alumno.registrar_alumno(alumno_2)
# print(Alumno.lista_alumno)

# notas_alumno = [10, 20, 15, 16]
# Alumno.registrar_nota_alumno("45958356", notas_alumno)

# notas_alumno = [5, 11, 12, 18]
# Alumno.registrar_nota_alumno("48475006", notas_alumno)
# print(Alumno.lista_alumno)

# print("imprimiendo reporte de notas de alumnos")
# Alumno.reporte_notas_alumnos()
