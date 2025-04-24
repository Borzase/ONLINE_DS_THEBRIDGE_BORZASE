import pandas as pd
import requests
from bs4 import BeautifulSoup
import sqlite3



class Prenda_ropa:
    
    

    def __init__(self, prenda_ropa):
        self.prenda = prenda_ropa
        self.datos = []
         
    
    def llamar_web(self, url):
        
                                                # Llamamos con el objeto requests a la página web y creamos la sopa mediante beautiful soup
        real = requests.get(url)                                                    
        soup = BeautifulSoup(real.text, "lxml")
        elementos = soup.find_all("article")                               # Extraemos los datos de la prenda y los almacenamos en una lista de diccionarios
        for elem in elementos:
            modelo = elem.find("p", attrs={"class":"descr"})
            color = elem.find("p", attrs={"class":"color"})
            precio = elem.find("span", attrs={"class": "country_eur"})
            self.datos.append({
                "Modelo": modelo.text,
                "Color": color.text,
                "Precio": float(precio.text.replace(",","."))
            })
        return self.datos
    
    def relleno_tabla(self):
        conexion = sqlite3.connect("base_datos_ropa.db")              #relleno los datos de la tabla para la prenda objeto solicitada acudiendo a la base de datos creada comun a la clase          
        cursor = conexion.cursor()
        for unidad in self.datos:
            Modelo = unidad["Modelo"]
            Color = unidad["Color"]
            Precio = unidad["Precio"]
            query = f"INSERT INTO {self.prenda} (Modelo, Color, Precio) VALUES ('{Modelo}', '{Color}', '{Precio}')"
            cursor.execute(query)
        conexion.commit()

        return 
    
    
    def solicitud(self):
        conexion = sqlite3.connect("base_datos_ropa.db")
        df = pd.read_sql(f"SELECT * FROM {self.prenda} ", conexion)
        conexion.close()
        return print(df)
        
    
    def solicitud_modelo(self,  modelo):
        conexion = sqlite3.connect("base_datos_ropa.db")  
        df = pd.read_sql(f"SELECT * FROM {self.prenda} WHERE Modelo LIKE '%{modelo}%' ", conexion)
        conexion.close()
        return print(df)
    
    def solicitud_color(self, color):
        conexion = sqlite3.connect("base_datos_ropa.db")
        df = pd.read_sql(f"SELECT * FROM {self.prenda} WHERE Color LIKE '%{color}%' ", conexion)
        conexion.close()
        return print(df)
    
    def solicitud_precio(self, precio):
        conexion = sqlite3.connect("base_datos_ropa.db")
        df = pd.read_sql(f"SELECT * FROM {self.prenda}  WHERE Precio <= {precio} ", conexion)
        conexion.close()
        return print(df)
    
    def eliminar_tabla(self):
        conexion = sqlite3.connect("base_datos_ropa.db")
        cursor = conexion.cursor()
        query = f''' DELETE FROM {self.prenda}'''
        cursor.execute(query)
        conexion.commit()
        conexion.close
        pass

