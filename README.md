# M3_01_Cristina_Suarez_Limon
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