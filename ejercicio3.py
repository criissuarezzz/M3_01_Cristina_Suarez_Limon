from ast import main

class producto():
    
    def __init__(self, codigo, nombre, precio, tipo):
        self.codigo=codigo
        self.nombre=nombre
        self.precio=precio
        self.tipo=tipo
        print("Se ha creado el producto con éxito")
    
    def __str__(self):
        return("El producto con nombre {} y código {}, vale {}€ y pertenece a la sección de {}".format(self.nombre, self.codigo, self.precio, self.tipo))

producto1=producto(8480000860293, "Pulpis Mix", 1.10, "golosinas")
producto2=producto(8480000225566, "Acondicionador instantáneo", 2.00, "Cuidado del cabello")
producto3=producto(8425514214583, "Berlina Glacé", 1.35, "bollería")

producto1.__str__()
producto2.__str__()
producto3.__str__()

producto1.precio=0.9
producto1.__str__()

if __name__=="__main__":
    main()