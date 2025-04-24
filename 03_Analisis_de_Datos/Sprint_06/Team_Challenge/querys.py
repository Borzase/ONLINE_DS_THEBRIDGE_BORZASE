
import sqlite3
import pandas as pd

conexion = sqlite3.connect("proveedores_piezas.db")                        
cursor = conexion.cursor()


df = pd.read_sql(f"SELECT * FROM pieza ", conexion)
print(df)