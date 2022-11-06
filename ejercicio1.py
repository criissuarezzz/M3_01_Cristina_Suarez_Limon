from ast import main
class alumno(): #Creamos la clase alumno

    def __init__(self, nombre, nota):     #construir la clase
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asignado
        self.nota = nota # Definimos que el atributo nota, sera la nota asignada
        print("Se ha creado con éxito el alumno")

    def calificacion(self):
        if int(self.nota) < 5:
            print("Ha suspendido {} con un {}".format(self.nombre, self.nota))
        else :
            print("Ha aprobado {} con un {}".format(self.nombre, self.nota))
        return

alumno1 = alumno("Valentina", 9.8) #Instancia
alumno2 = alumno("María", 4)
alumno3 = alumno("Óscar", 10)

#Llamamos al método
alumno1.calificacion()
alumno2.calificacion()
alumno3.calificacion()

if __name__=="__main__":
    main()