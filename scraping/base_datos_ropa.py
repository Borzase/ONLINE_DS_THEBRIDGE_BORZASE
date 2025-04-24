
import sqlite3

prendas = ["chaqueta", "camiseta", "pantalon", "jersey"]
conexion = sqlite3.connect("base_datos_ropa.db")                        
cursor = conexion.cursor()
for prenda in prendas:
    query_create = f''' 
    CREATE TABLE {prenda} (
    MODELO     TEXT NOT NULL,
    COLOR      TEXT NOT NULL,
    PRECIO      FLOAT
    ) '''
    cursor.execute(query_create)
conexion.commit()
conexion.close()