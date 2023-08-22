print("departamento de confeccion")
print("1. Ingresar producto")
print("2. Ingresar producto a fabrica")
print("0. Salir")
opcion=int(input("Digita una opcion: "))
opcion=100
ListaProductos=[]
while opcion!=0:
    opcion=int(input("Digita una opcion: "))
    if opcion==1:
        producto=input("Digita el producto que ingresa a fabricacion: ")
        #agregar un producto a la lista de productos
        ListaProductos.append(producto)
        
    elif opcion==2:
        print("Mostrar el inventario: ")
        print(ListaProductos)
    elif opcion==0:
        print("gracias, hasta pronto...")
    else:
        print("opcion invalida...")
print("fin del programa")