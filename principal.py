import funciones as fn
pedidos = []

while True:
    print("bienvenido\n1 comprar gas \n2. ver lista de pedidos\n3. selecionar comuna\n4. salir")
    opcion = int(input("ingrese una opcion: "))
    if opcion==1:
        fn.comprar_gas(pedidos)
    elif opcion==2:
        fn.lista_de_pedidos(pedidos)
    elif opcion==3:
        fn.imprimir_planilla(pedidos)
    elif opcion==4:
        break
