COMUNAS = ['valparaiso','quillota','limache']

def comprar_gas(pedidos):
    nombre = input("ingrese nombre")
    dirrecion = input("ingrese dirrecion")
    comuna = input("ingese su comuna porfavor (valparaiso,quillota,limache): ").lower()
    while comuna not in COMUNAS:
        comuna = input("ingese su comuna porfavor (valparaiso,quillota,limache): ").lower()
    cili5kg = int(input("ingrese la cantidad de cuantos cilindros de 5 kg quiere"))
    cili15kg = int(input("ingrese la cantidad de cuantos cilindros de 15 kg quiere"))
    cili45kg = int(input("ingrese la cantidad de cuantos cilindros de 45 kg quiere"))


    pedidos.append({
        'nombre' : nombre,
        'dirrecion' : dirrecion,
        'comuna' : comuna,
        'cilindros de 5 kg' : cili5kg,
        'cilindros de 15 kg' : cili15kg,
        'cilindros de 45 kg' : cili45kg
    })





def lista_de_pedidos(pedidos):
    print("lista de pedidos")
    for pedido in pedidos:
        print(pedido)
            

        
def imprimir_planilla(pedidos):
    selecicioneunacomuna = input("ingrese una comuna cual desea ver o si decea ver todas precione ENTER")
    if selecicioneunacomuna == '':
        imprimir_comuna = pedidos
        nombrearchivo = f'todas_las_comunas.txt'
    elif selecicioneunacomuna in COMUNAS:
        imprimir_comuna = []
        for pedido in pedidos:
            if pedido['comuna'] == selecicioneunacomuna:
                imprimir_comuna.append({pedido})
        nombrearchivo = f'la_comunas_es_{selecicioneunacomuna}.txt'
        with open(nombrearchivo,'w') as archivo:
            for pedido in imprimir_comuna:
                archivo.write(f'nombre: {pedido['nombre']}\n')
                archivo.write(f'dirrecion: {pedido['dirrecion']}\n')
                archivo.write(f'nombre: {pedido['nombre']}\n')
                archivo.write(f'nombre: {pedido['nombre']}\n')
                archivo.write(f'nombre: {pedido['nombre']}\n')
                archivo.write(f'nombre: {pedido['nombre']}\n')


        

        

    



