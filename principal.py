import funciones as fn

while True:
    opcion=int(input("\n¡Bienvenido a tu libreria virtual\na continuacion veras las opciones\nque tenemos para ofrecerte\n1)Registrar un libro\n2)Mostrar todos los libros\n3)Registrar una venta\n4)Imprimir reporte de ventas\n5)Generar un TxT\n6)Salir !\nSelecciona el numero: "))
    
    if opcion==1:
        fn.reglibro()
    elif opcion==2:
        fn.listarlibros()
    elif opcion==3:
        fn.regventa()
    elif opcion==4:
        fn.impreporte()
    elif opcion==5:
        fn.generartxt()
    elif opcion==6:
        print("¡Gracias por preferirnos!")
        break
    else:
        print("¡PORFAVOR ESCOGE UNA OPCION CORRECTA!")

