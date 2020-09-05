# Creación de clase persona

class Persona():
    def __init__(self, dni, nombres, apellido_paterno, apellido_materno, edad):
        self.dni = dni
        self.nombres = nombres
        self.apellido_paterno = apellido_paterno
        self.apellido_materno = apellido_materno
        self.edad = edad

# Prueba de funcionamiento
# persona_1 = Persona('45958356', 'Charly Cristian', 'Chinchay', 'Escamilo', '30')
# print(persona_1.nombres)