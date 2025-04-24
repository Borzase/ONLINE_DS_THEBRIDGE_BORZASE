
from clase_scraping import Prenda_ropa


def chaqueta():
    
    chaqueta = Prenda_ropa("chaqueta")
      
    chaqueta.llamar_web(url ="https://www.carhartt-wip.com/es/hombre-chaquetas-y-abrigos")
    chaqueta.relleno_tabla()
    chaqueta.solicitud()
    
    filtrado = input("¿Desea filtrar por modelo, color o precio? Si o No")
    corregido = filtrado.capitalize()
    while corregido == "Si":
        opcion = int(input("""¿Cómo desea filtrar?:
                       1 - Modelo
                       2 - Color
                       3 - Precio
                       4 - Salir """))
        if opcion == 1:
            modelo = input("Escriba el modelo de la prenda.")
            chaqueta.solicitud_modelo(modelo)
            continue
        elif opcion == 2:
            color = input("Escriba el color de la prenda.")
            chaqueta.solicitud_color(color)
            continue
        elif opcion == 3:
            precio = float(input("Escriba el precio referente de la prenda. Se seleccionaran prendas por valor igual o menor al precio escogido"))
            chaqueta.solicitud_precio(precio)
            continue
        elif opcion == 4:
            chaqueta.eliminar_tabla()
            break
        break



def camiseta():
    
    camiseta = Prenda_ropa("camiseta")
    
    camiseta.llamar_web(url = "https://www.carhartt-wip.com/es/hombre-camisetas-y-polos")
    camiseta.relleno_tabla()
    camiseta.solicitud()

    filtrado = input("¿Desea filtrar por modelo, color o precio? Si o No")
    corregido = filtrado.capitalize()
    while corregido == "Si":
        opcion = int(input("""¿Cómo desea filtrar?:
                       1 - Modelo
                       2 - Color
                       3 - Precio
                       4 - Salir """))
        if opcion == 1:
            modelo = input("Escriba el modelo de la prenda.")
            camiseta.solicitud_modelo(modelo)
            continue
        elif opcion == 2:
            color = input("Escriba el color de la prenda.")
            camiseta.solicitud_color(color)
            continue
        elif opcion == 3:
            precio = float(input("Escriba el precio referente de la prenda. Se seleccionaran prendas por valor igual o menor al precio escogido"))
            camiseta.solicitud_precio(precio)
            continue
        elif opcion == 4:
            camiseta.eliminar_tabla()
            break
        break



def pantalon():
    
    pantalon = Prenda_ropa("pantalon")
       
    pantalon.llamar_web(url = "https://www.carhartt-wip.com/es/hombre-pantalones")
    pantalon.relleno_tabla()
    pantalon.solicitud()

    filtrado = input("¿Desea filtrar por modelo, color o precio? Si o No")
    corregido = filtrado.capitalize()
    while corregido == "Si":
        opcion = int(input("""¿Cómo desea filtrar?:
                       1 - Modelo
                       2 - Color
                       3 - Precio
                       4 - Salir """))
        if opcion == 1:
            modelo = input("Escriba el modelo de la prenda.")
            pantalon.solicitud_modelo(modelo)
            continue
        elif opcion == 2:
            color = input("Escriba el color de la prenda.")
            pantalon.solicitud_color(color)
            continue
        elif opcion == 3:
            precio = float(input("Escriba el precio referente de la prenda. Se seleccionaran prendas por valor igual o menor al precio escogido"))
            pantalon.solicitud_precio(precio)
            continue
        elif opcion == 4:
            pantalon.eliminar_tabla()
            break
        break

def jersey():
    
    jersey = Prenda_ropa("jersey")
    
    jersey.llamar_web(url = "https://www.carhartt-wip.com/es/hombre-jerseis")
    jersey.relleno_tabla()
    jersey.solicitud()

    filtrado = input("¿Desea filtrar por modelo, color o precio? Si o No")
    corregido = filtrado.capitalize()
    

    while corregido == "Si":
        opcion = int(input("""¿Cómo desea filtrar?:
                       1 - Modelo
                       2 - Color
                       3 - Precio
                       4 - Salir """))
        if opcion == 1:
            modelo = input("Escriba el modelo de la prenda.")
            jersey.solicitud_modelo(modelo)
            continue
        elif opcion == 2:
            color = input("Escriba el color de la prenda.")
            jersey.solicitud_color(color)
            continue
        elif opcion == 3:
            precio = float(input("Escriba el precio referente de la prenda. Se seleccionaran prendas por valor igual o menor al precio escogido"))
            jersey.solicitud_precio(precio)
            continue
        elif opcion == 4:
            jersey.eliminar_tabla()
            break
        break
    
    
def salir():
    print("Hasta pronto")
    exit()


def switch(opcion):
    diccionario = {
        1 : chaqueta,
        2 : camiseta,
        3 : pantalon,
        4 : jersey,
        5 : salir
    }
    
    if opcion > 5:
        print("Ingrese un número del 1 al 5")
    else:
        return diccionario[opcion]()



while True:
    print("""Que prenda de ropa desea consultar:
    1 - Chaquetas
    2 - Camisetas y polos
    3 - Pantalones
    4 - Jerseis
    5 - Salir""")
    try:
        opcion = int(input(""))
        switch(opcion)
    except ValueError:
        print("Por favor, introduce un número válido.")