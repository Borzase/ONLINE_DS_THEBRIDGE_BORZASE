import sqlite3

conexion = sqlite3.connect("./Data_piezas/proveedores_piezas.db")                        
cursor = conexion.cursor()
datos_proveedores = {
    1: ("Ladrillos Reunidos", "Av. Los Pinos 123", "Bilbao", "Bizkaia"),
    2: ("Cementos del Sur", "Calle Real 45", "Cádiz", "Cádiz"),
    3: ("Hierros y Aceros Goya", "Plaza Mayor 12", "Madrid", "Madrid"),
    4: ("Ferretería Central", "Calle del Río 78", "Zaragoza", "Zaragoza"),
    5: ("Maderas Romero", "Av. Libertad 9", "Sevilla", "Sevilla"),
    6: ("Pinturas y Revestimientos", "Calle Innovación 33", "Málaga", "Málaga"),
    7: ("Bloques La Huerta", "Camino Verde 22", "Murcia", "Murcia"),
    8: ("Yesos del Este", "Paseo del Mar 17", "Valencia", "Valencia"),
    9: ("Tuberías y Conducciones", "Calle Palma 88", "Santa Cruz", "Tenerife"),
    10: ("Hormigones Norte", "Av. Industria 54", "Santander", "Cantabria"),
    11: ("Aislantes Plus", "Calle Papel 1", "Logroño", "La Rioja"),
    12: ("Tejas Vega", "Av. Andalucía 90", "Granada", "Granada"),
    13: ("Paneles La Espiga", "Calle Pan 3", "Toledo", "Toledo"),
    14: ("Vigas Selectas", "Calle Ternera 45", "Salamanca", "Salamanca"),
    15: ("Gravas y Áridos Cantábricos", "Muelle Norte 21", "Gijón", "Asturias"),
    16: ("Canalones Ruiz", "Polígono Motor 10", "Valladolid", "Valladolid"),
    17: ("Puertas Roble", "Camino Forestal 66", "Soria", "Soria"),
    18: ("Azulejos Sol", "Calle Diseño 14", "Alicante", "Alicante"),
    19: ("Construcciones del Sur", "Av. Construcción 5", "Jaén", "Jaén"),
    20: ("Pavimentos Manolo", "Calle Niñez 23", "Huelva", "Huelva"),
    21: ("Materiales Barcelona", "Paseo Moda 3", "Barcelona", "Barcelona"),
    22: ("Ventanas Luna", "Calle Suela 98", "Tarragona", "Tarragona"),
    23: ("Accesorios para Obra", "Av. Bebidas 29", "Burgos", "Burgos"),
    24: ("Herramientas Techno", "Calle Circuito 67", "Pamplona", "Navarra"),
    25: ("Morteros del Sur", "Calle Bolígrafo 8", "Almería", "Almería"),
    26: ("Andamios López", "Calle Almacén 50", "Ciudad Real", "Ciudad Real"),
    27: ("Impermeabilizantes Mediterráneo", "Av. Costa 101", "Castellón", "Castellón"),
    28: ("La Pincelada Divertida", "Calle Luz 36", "León", "León"),
    29: ("Tornillería Antártida", "Paseo Frío 4", "Lugo", "Lugo"),
    30: ("Maquinaria para Obra", "Av. Aroma 7", "Ourense", "Ourense")
}


for clave,valores in datos_proveedores.items():
    nombre = valores[0]
    direccion = valores[1]
    ciudad = valores[2]
    provincia = valores[3]
    query = f"INSERT INTO proveedores (ID_PROVEEDOR, NOMBRE, DIRECCION, CIUDAD, PROVINCIA) VALUES ({clave},'{nombre}', '{direccion}', '{ciudad}', '{provincia}' )"
    cursor.execute(query)
conexion.commit()



datos_obtencion = {
    1: 1001,
    2: 1002,
    3: 1003,
    4: 1004,
    5: 1005,
    6: 1006,
    7: 1007,
    8: 1008,
    9: 1009,
    10: 1010,
    11: 1011,
    12: 1012,
    13: 1013,
    14: 1014,
    15: 1015,
    16: 1016,
    17: 1017,
    18: 1018,
    19: 1019,
    20: 1020,
    21: 1021,
    22: 1022,
    23: 1023,
    24: 1024,
    25: 1025,
    26: 1026,
    27: 1027,
    28: 1028,
    29: 1029,
    30: 1030

}

for clave,valor in datos_obtencion.items():
    
    query = f"INSERT INTO obtener_proveedor (ID_PROVEEDOR, CODIGO_PIEZA) VALUES ({clave},{valor} )"
    cursor.execute(query)
conexion.commit()

datos_pieza = {
    1001: ("Ladrillo macizo", "Rojo", 0.45, 201),
    1002: ("Cemento Portland", "Gris", 4.50, 202),
    1003: ("Bloque de hormigón", "Gris claro", 1.20, 203),
    1004: ("Viga IPN 100", "Metal", 18.75, 204),
    1005: ("Teja cerámica curva", "Terracota", 0.95, 205),
    1006: ("Panel aislante EPS", "Blanco", 3.10, 206),
    1007: ("Arena fina", "Beige", 25.00, 207),
    1008: ("Grava 20mm", "Gris oscuro", 22.00, 207),
    1009: ("Malla electrosoldada", "Plateado", 5.20, 204),
    1010: ("Mortero seco", "Gris", 3.95, 208),
    1011: ("Yeso blanco", "Blanco", 4.20, 209),
    1012: ("Azulejo blanco 20x20", "Blanco brillante", 12.50, 210),
    1013: ("Pavimento antideslizante", "Gris piedra", 15.90, 210),
    1014: ("Tubo PVC 90mm", "Gris", 2.10, 211),
    1015: ("Codo PVC 90°", "Gris", 1.00, 211),
    1016: ("Llave de paso", "Plateado", 6.80, 211),
    1017: ("Tornillo 6x50", "Zincado", 0.10, 212),
    1018: ("Anclaje químico", "Transparente", 7.90, 212),
    1019: ("Silicona neutra", "Blanco", 4.60, 213),
    1020: ("Espuma poliuretano", "Amarillo", 5.75, 213),
    1021: ("Madera pino cepillada", "Natural", 3.50, 214),
    1022: ("Puerta interior DM", "Blanco", 75.00, 214),
    1023: ("Manilla aluminio", "Plateado", 8.20, 215),
    1024: ("Caja eléctrica", "Negro", 1.60, 216),
    1025: ("Canaleta plástica", "Blanco", 0.90, 216),
    1026: ("Interruptor sencillo", "Blanco", 3.00, 216),
    1027: ("Foco LED empotrable", "Blanco", 12.90, 217),
    1028: ("Pintura plástica blanca", "Blanco mate", 22.00, 218),
    1029: ("Rodillo pintura", "Amarillo", 2.80, 219),
    1030: ("Cinta métrica 5m", "Amarillo/Negro", 6.50, 219)

}


for clave,valores in datos_pieza.items():
    nombre = valores[0]
    color = valores[1]
    precio = valores[2]
    codigo = valores[3]
    query = f"INSERT INTO pieza (CODIGO_PIEZA, NOMBRE_PIEZA, COLOR, PRECIO, CODIGO_CATEGORIA) VALUES ({clave},'{nombre}', '{color}', {precio}, {codigo} )"
    cursor.execute(query)
conexion.commit()


datos_pieza_disponible = {
    1001: ("2025-03-01", 1200),
    1002: ("2025-02-15", 300),
    1003: ("2025-01-20", 850),
    1004: ("2025-03-10", 120),
    1005: ("2025-03-05", 1500),
    1006: ("2025-02-28", 450),
    1007: ("2025-03-15", 75),
    1008: ("2025-03-16", 60),
    1009: ("2025-03-12", 210),
    1010: ("2025-03-08", 320),
    1011: ("2025-02-26", 290),
    1012: ("2025-01-30", 140),
    1013: ("2025-03-04", 170),
    1014: ("2025-02-22", 500),
    1015: ("2025-02-25", 600),
    1016: ("2025-02-20", 250),
    1017: ("2025-03-11", 900),
    1018: ("2025-03-06", 180),
    1019: ("2025-03-14", 300),
    1020: ("2025-03-09", 230),
    1021: ("2025-02-27", 350),
    1022: ("2025-01-18", 75),
    1023: ("2025-02-18", 130),
    1024: ("2025-03-13", 400),
    1025: ("2025-02-21", 550),
    1026: ("2025-02-23", 370),
    1027: ("2025-03-02", 150),
    1028: ("2025-03-07", 95),
    1029: ("2025-02-24", 220),
    1030: ("2025-03-03", 160)

}

for clave,valores in datos_pieza_disponible.items():
    fecha = valores[0]
    cantidad = valores[1]
    query = f"INSERT INTO pieza_disponible (CODIGO_PIEZA, FECHA, CANTIDAD) VALUES ({clave},'{fecha}', {cantidad} )"
    cursor.execute(query)
conexion.commit()

datos_categoria = {
    201: "Albañilería",
    202: "Cementos",
    203: "Prefabricados",
    204: "Estructuras metálicas",
    205: "Cubiertas",
    206: "Aislamientos",
    207: "Áridos y agregados",
    208: "Morteros y adhesivos",
    209: "Yesos y acabados",
    210: "Revestimientos y pavimentos cerámicos",
    211: "Fontanería",
    212: "Fijaciones",
    213: "Selladores y espumas",
    214: "Carpintería de madera",
    215: "Herrajes",
    216: "Electricidad e instalaciones",
    217: "Iluminación",
    218: "Pinturas y recubrimientos",
    219: "Herramientas manuales"

}

for clave,valor in datos_categoria.items():
    
    query = f"INSERT INTO categoria (NOMBRE, CODIGO_CATEGORIA) VALUES ('{valor}',{clave})"
    cursor.execute(query)
conexion.commit()


conexion.close()
