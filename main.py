""""""""""
Ejercicios Modulo 3. Clases y objetos
Consideraciones a tener en cuenta:

Guardar este documento con el siguiente formato para su entrega: M3_01_nombre_apellido1_apellido2
Realizar los ejercicios con las herramientas vistas en las sesiones.
Comentar el código
Utilizar nombres de variables apropiados, si vais a guardar una nota, llamar a esa variable nota, no n o x
Ejercicio 1
Creación
Crea una clase llamada Alumno que tenga los atributos nombre y nota
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el alumno se ha creado con éxito
Crear un método llamado calificacion que imprima por pantalla si el alumno ha aprobado o suspendido en base a su nota
Experimentación
Crea algunos alumnos
Prueba a ejecutar el método calificacion de cada objeto que has creado
"""""""""

class alumno(): #Creamos la clase alumno

    def __init__(self, nombre, nota):     #
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
alumno3 = alumno("Oscar", 10)

#Llamamos al método
alumno1.calificacion()
alumno2.calificacion()
alumno3.calificacion()