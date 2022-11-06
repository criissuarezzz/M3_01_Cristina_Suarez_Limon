from ast import main
class alumno(): #Creamos la clase alumno

    def __init__(self, nombre, nota):     #
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asignado
        self.nota = nota # Definimos que el atributo nota, sera la nota asignada
        print("Se ha creado con éxito el alumno")

    def calificacion(self):
        if int(self.nota) < 5:
            print("Ha suspendido")
        else :
            print("Ha aprobado")
        return
    
    def __str__(self): 
        return("{} ha sacado un {}".format(self.nombre, self.nota)) 


alumno1 = alumno("Valentina", 9.8) 
alumno2 = alumno("María", 4)
alumno3 = alumno("Óscar", 10)

#Llamamos al método

print(str(alumno1))
print(str(alumno2))
print(str(alumno3))


if __name__=="__main__":
    main()