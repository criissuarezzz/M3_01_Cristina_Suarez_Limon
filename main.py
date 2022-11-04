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
Ejercicio 2
Creación
Copia el ejercicio anterior y realicemos una modificación:

Junto al método init y calificacion, vamos a crear otro método especial de Python, el método str. Al igual que init, debe ir encerrado entre dobles guiones bajos, y debe tener el siguiente formato:

def __str__(self): return "Lo que quiero mostrar"

Este método nos sirve para imprimir por pantalla la información de un objeto, si tenemos un objeto alumno1 creado y realizamos print(alumno1), Python ejecutará el contenido del método str (el método str lo que tiene que hacer es maquetar la información que desea en un string).

Experimentación
Implementa el método str y haz que muestre el nombre y la nota del alumno
Crea algun objeto de la clase Alumno
Realiza print de esos objetos para visualizar por pantalla la información del str
Ejercicio 3
Creación
Crea una clase llamada Producto que tenga los atributos codigo, nombre, precio y tipo.
Crea el constructor de la clase. Añadir en el constructor un print para informar de que el producto se ha creado con éxito
Crea el método __str__ para visualizar por pantalla la información de los productos
Experimentación
Crea algunos productos
Prueba a mostrar los datos de algun producto y a modificar algun valor, por ejemplo, prueba a modificar el precio de un producto

"""""""""""

class alumno(): #Creamos la clase alumno

    def __init__(self, nombre, nota):
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asignado
        self.nota = nota # Definimos que el atributo nota, sera la nota asignada
        print

    def constructor(self):
        alumno = ("Hola soy {} y mi nota es un {}") #Mensaje
        print(alumno.format(self.nombre, self.nota)) #Usamos FORMAT

    def calificacion(self):
        if int(self.nota) < 5:
            print("Ha suspendido")
        else :
            print("Ha aprobado")
        return

alumno1 = alumno("Pedro", "4") #Instancia
alumno2 = alumno("Cristina", "10")
alumno3 = alumno("Lucia", "10")




#Llamamos al método

alumno1.constructor()
alumno1.calificacion()

alumno2.constructor()
alumno2.calificacion()

alumno3.constructor()
alumno3.calificacion()