
# Registrar venta: Para registrar una venta se requiere lo siguiente: Título del libro, Cantidad
# vendida, precio por unidad y precio final. Debe validar que el título exista en el inventario y
# que la cantidad no exceda el stock disponible. Simule una boleta estándar

# Imprimir reporte de ventas: Para imprimir el reporte de ventas, el usuario puede seleccionar
# imprimir todos o por un género en específico. Estos géneros deben estar previamente
# definidos en una colección de Python en el código y por lo menos deben ser tres, por ejemplo:
# "Ficción", "No Ficción", "Ciencia".

# Generar TXT: Debe exportar a un archivo txt con el registro de las ventas
# Cada una de estas opciones de la aplicación debe estar desarrollada en una función que debe
# ser llamada desde el programa principal.
# Debe cargar el archivo nombreApellido.py a la entrega además del link de github

listlibros=[]
titulo={}
autor={}
genero={"Ficcion","Romance","Accion"}
precio={}
cantidadvent=0

def reglibro():
        
    resp="si"
    
    while resp == "si":    
        print("Para registrar tu libro necesitare que me proporciones\nla siguiente informacion:")
        
        titulo=input("Porfavor dime el titulo de tu libro: ")
    
        autor=input("Ahora necesitare saber cual es el nombre del autor: ")

        genero=input("Estos son los generos que tenemos para que escogas\nFiccion\nRomance\nAccion\nEscribe el genero: ")

        precio=int(input("Indica el precio de tu libro: "))
        
        resp=input("¿Deseas agregar otro libro?(Si/No)\n")
        
        registro={
            "titulo" : titulo,
            "autor" : autor,
            "genero" : genero,
            "precio" : precio
        }
        
        listlibros.append(registro)

def listarlibros():
    for i in listlibros:
            print(i,end=(""))
            print()
    
    
def regventa():
    
    salidaventa="si"
    
    while salidaventa==("si"):    
        print("¡Has decidido comprar un libro\npara comprar un libro debes ver el stock que esta en la opcion numero 2\nseguido de eso procedamos!")
        titventa=input("ingresa el titulo del libro que deseas: ")
        
        if titventa == listlibros(["titulo"]):
            vntcant=int(input("Ingresa la cantidad de libros que deseas: "))
            print(f"el precio por unidad de el libro que has decidido es de {listlibros}")
            print(f"y el precio de el total por los libros que has llevado es de {vntcant*listlibros}")
        else:
            salidaventa=input("Ese titulo no se encuentra en nuestros registros\nDeseads intentar nuevamente? (si/no)")

def impreporte():
    print("")
    
def generartxt():
    print("")
    

        

    



