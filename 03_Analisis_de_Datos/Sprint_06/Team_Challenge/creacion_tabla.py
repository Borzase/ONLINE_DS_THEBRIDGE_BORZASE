import sqlite3


conexion = sqlite3.connect("proveedores_piezas.db")                        
cursor = conexion.cursor()

query_create = ''' 
    CREATE TABLE proveedores (
    ID_PROVEEDOR     INT PRIMARY KEY,
    NOMBRE          TEXT NOT NULL,
    DIRECCION       TEXT NOT NULL,
    CIUDAD          TEXT NOT NULL,
    PROVINCIA       TEXT NOT NULL
    ) '''
    
cursor.execute(query_create)
conexion.commit()

query_obtener = ''' 
    CREATE TABLE obtener_proveedor (
    ID_PROVEEDOR     INT PRIMARY KEY,
    CODIGO_PIEZA     INT 
    ) '''
    
cursor.execute(query_obtener)
conexion.commit()

query_pieza = ''' 
    CREATE TABLE pieza (
    CODIGO_PIEZA     INT PRIMARY KEY,
    NOMBRE_PIEZA     TEXT NOT NULL,
    COLOR            TEXT NOT NULL,
    PRECIO           FLOAT,
    CODIGO_CATEGORIA INT 
    ) '''
    
cursor.execute(query_pieza)
conexion.commit()

query_disponible = ''' 
    CREATE TABLE pieza_disponible (
    CODIGO_PIEZA    INT PRIMARY KEY,
    FECHA           DATETIME,
    CANTIDAD        INT  
    ) '''
    
cursor.execute(query_disponible)
conexion.commit()

query_categoria = ''' 
    CREATE TABLE categoria (
    NOMBRE              TEXT NOT NULL,
    CODIGO_CATEGORIA    INT PRIMARY KEY
    ) '''
    
cursor.execute(query_categoria)
conexion.commit()

conexion.close()