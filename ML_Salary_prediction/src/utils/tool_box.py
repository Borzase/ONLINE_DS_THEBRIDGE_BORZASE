## Se necesitan importar las siguientes librerias

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency, f_oneway, ttest_ind, mannwhitneyu, pearsonr

def describe_df(dataframe):
    """ 
    La función trabaja sobre un dataframe y clasifica los datos de las variables según el tipo de datos que contiene cada variable, 
    el porcentaje de nulos, los valores unicos de la variable y en función de esta última la cardinalidad que presenta.

    Argumentos:
    dataframe (pandas dataframe) = es el dataframe sobre el que se quiere aplicar la función

    Retorna:
    Devuelve un nuevo dataframe organizado cuyo índice son los cuatro descriptores
    
    """
    dic_columnas = {}
    for columna in dataframe.columns:
        a = dataframe[columna].dtype
        b = round((len(dataframe.loc[dataframe[columna].isna()])/len(dataframe)*100),2)
        c = dataframe[columna].nunique()
        d = round(dataframe[columna].nunique()/len(dataframe)*100, 2)
        dic_columnas[columna] = [a, b, c, d]

    indice = ["DATA_TYPE", "MISSINGS (%)", "UNIQUE_VALUES", "CARDIN (%)"]
    df = pd.DataFrame(dic_columnas, index = indice)
    return df



def tipifica_variables (df_in, umbral_categoria = 10, umbral_continua=20.0):
    """ 
    La función se utiliza para categorizar las columnas de un dataframe en binaria, categorica, 
    numérica discontinua y numerico continua. Para clasificar las numericas se utilizan los umbrales.
    
    Argumentos:
    df_in (pandas dataframe) = El dataframe a categorizar
    umbral_categoria (int) = Por defecto el umbral de categoria son 10.
    umbral_continua (float) = Por defecto el umbral de continua son 20
    
    Retorna:
    Devuelve un dataframe con el nombre de la columna y su tipo de categoria"""
    
    diccion = {}
    for columna in df_in.columns:
      if df_in[columna].nunique() == 2:
        diccion[columna] = "Binaria"
      if df_in[columna].nunique() > 2 and df_in[columna].nunique() < umbral_categoria:
        diccion[columna] = "Categórica"
      if df_in[columna].nunique() >= umbral_categoria:
        diccion[columna] = "Numérica discreta"
      if (df_in[columna].nunique()/len(df_in[columna]) * 100) >= umbral_continua:
          diccion[columna] = "Numérica continua"
        
    categoria = pd.Series(diccion)
    df = pd.DataFrame(categoria)
    
    return df.rename(columns={0:"Categoria"})


def get_features_num_regression(dataframe, target_col,umbral_corr, pvalue = None):
    """ 
    La función se utiliza sobre una columna numérica continua para saber la correlación frente a
    otras columnas numéricas. Se utiliza un umbral de correlación para seleccionar las correlaciones
    que superen dicho valor y un pvalor que por defecto es None y que sirve para confirmar significación
    estadística.
    
    Argumentos:
    dataframe (pandas dataframe) = dataframe que se quiere analizar
    target_col (string) = la columna objetivo del dataframe
    umbral_corr (float)= nivel límite de correlación entre las variables
    pvalue (None) = por defecto None pero espera un float 
    
    Retorna
    Devuelve una lista con las variables numéricas que han superado el umbral de correlación, 
    y en caso de introducir el pvalue, de las varibales cuyo p-valor está por debajo del pvalue indicado.
    Se ofrece además de manera visual una matriz de correlación entre la columna target y las variables seleccionadas
    """
    try:
        if not isinstance(dataframe, pd.DataFrame):
            print("Error: 'df' no es un DataFrame.")
            return None 
        if dataframe[target_col].nunique()/len(dataframe) * 100 >= 20:  # Condición de que la columna target sea numerica continua
            lista_columnas = []
            tabla = dataframe.drop(target_col, axis=1)
            for col in tabla.columns:
                if dataframe[col].dtype != 'object' and dataframe[col].dtype != 'bool':
                    corrs = pearsonr(dataframe[target_col], dataframe[col])
                    if pvalue != None:
                        if np.abs(corrs[0]) > umbral_corr and corrs[1] <= pvalue:
                            lista_columnas.append(col)
                    else:
                        if np.abs(corrs[0]) > umbral_corr:
                            lista_columnas.append(col)
    
            lista_columnas.insert(0, target_col)
            corr_matrix = dataframe[lista_columnas].corr()
            figura = plt.figure(figsize=(10,10))
            sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, square=True, linewidths=.5) # el cmap es el rango de colores usado para representar "el calor"
            plt.title('Matriz de Correlación')
            plt.xticks(rotation=45)  # Rota las etiquetas de las x si es necesario
            plt.yticks(rotation=45)  # Rota las etiquetas de las y si es necesario
            lista_columnas.remove(target_col)

            return lista_columnas, figura
        else: 
            return print(f"La variable {target_col} no cumple con el umbral de variable numérica continua")
    except KeyError: 
        print(f"¡Lo siento, la columna '{target_col}' no existe! Revisa que esté bien escrita")


def plot_features_num_regression(dataframe, target_col, lista = [], umbral_corr = 0.0, pvalue = None):
    """ 
    La función tiene por objeto analizar las funciones numéricas de un dataframe o las variables
    introducidas por lista y conocer la correlación frente a la columna target.
    
    Argumentos:
    dataframe (pandas dataframe) = el dataframe sobre el que se va a trabajar
    target_col ('string') = el nombre de la columna target
    lista (list) = es una lista que por defecto va vacia
    umbral_corr (float) = por defecto tiene valor 0 
    pvalue (None) = por defecto None, se espera que sea un valor float
    
    Retorna:
    La función devuelve un pairplot con las columnas que han superado los umbrales de correlación
    y, en caso de incluir el pvalue, cuyo p-valor sea inferior al pvalue."""
    try:
        if not isinstance(dataframe, pd.DataFrame):
            print("Error: 'df' no es un DataFrame.")
            return None 
        if dataframe[target_col].nunique()/len(dataframe) * 100 >= 20:
            lista_columnas = []
            if len(lista) == 0:
                tabla = dataframe.drop(target_col, axis=1)
                for col in tabla.columns:
                    if dataframe[col].dtype != 'object' and dataframe[col].dtype != 'bool':
                        corrs = pearsonr(dataframe[target_col], dataframe[col])
                        if pvalue != None:
                            if np.abs(corrs[0]) > umbral_corr and corrs[1] <= pvalue:
                                lista_columnas.append(col)
                        else:
                            if np.abs(corrs[0]) > umbral_corr:
                                lista_columnas.append(col)
                lista_columnas.insert(0, target_col)
                return sns.pairplot(dataframe[lista_columnas])

            else:
                try:
                    lista
                    for col in lista:
                    
                        corrs = pearsonr(dataframe[target_col], dataframe[col])
                        if pvalue != None:
                            if np.abs(corrs[0]) < umbral_corr or corrs[1] > pvalue:
                                lista.remove(col)
                        else:
                            if np.abs(corrs[0]) < umbral_corr:
                                lista_columnas.remove(col)
                    
                    lista.insert(0, target_col)
                    return sns.pairplot(dataframe[lista])
                except Exception:
                    print(f"La columna '{col}' no es numérica")
                
        else: 
            return print(f"La variable {target_col} no cumple con el umbral de variable numérica continua")
        
    except KeyError: 
        print(f"¡Lo siento, la columna '{target_col}' no existe! Revisa que esté bien escrita")

def get_features_cat_regression(df, target_col, pvalue=0.05):
    '''La funcion tiene como objetivo estudiar la correlación entre la variable objetivo con el resto de columnas y estudiar su independencia.
       
       Argumentos:
       df (pandas dataframe) = corresponden a los datos a los que se les quiere hacer el estudio.
       target_col ('string') = nombre de la columna objetivo
       pvalue ('float') = pvalor de referencia para aceptar o rechazar la hipotesis

       Retorna:
       
       La funcion devuelve una lista con las variables cuyo p valor es menor al pvalue de referencia y por tanto rechaza la hopotesis nula.
    '''
    
    if not isinstance(df, pd.DataFrame):
        print("Error: 'df' no es un DataFrame.")
        return None
    if not isinstance(target_col, str):
        print("Error: 'target_col' debe ser un string.")
        return None
    if target_col not in df.columns:
        print(f"Error: '{target_col}' no está en el DataFrame.")
        return None
    if not (0 < pvalue < 1):
        print("Error: 'pvalue' debe estar entre 0 y 1.")
        return None
    
    if not np.issubdtype(df[target_col].dtype, np.number): #Utilizamos issubdtype porque 'df[target_col].dtype' no es un número, sino un objeto dtype y si usamos isinstance aunque sea numérica devuelve error.
        print("Error: 'target_col' no es una variable numérica.")
        return None
    if df[target_col].nunique()/len(df)*100 < 10:
        print("Error: 'target_col' no tiene suficiente cardinalidad para considerarse continua o discreta adecuada.")
        return None
    
    columnas_categoricas = df.select_dtypes(include= ['object','category','bool']).columns.to_list()
    selected_features = []
    for col in columnas_categoricas: 
        if df[col].nunique() ==2:
            categorias = df[col].dropna().unique() #Obtenemos las categorías de la columna (binomial)
            grupo1 = df[df[col] == categorias[0]][target_col].dropna() #Primera categoría
            grupo2 = df[df[col] == categorias[1]][target_col].dropna() #Segunda categoría
            if len(grupo1) > 1 and len(grupo2) >1: #Necesitamos que tenga mas de un elemento para poder hacer el test.
                stats, p = mannwhitneyu(grupo1, grupo2)
            if p < pvalue:
                selected_features.append(col)
        elif df[col].nunique() > 2:
            grupos = df[col].dropna().unique()
            valor_grupo= [df[df[col] == grupo][target_col].dropna() for grupo in grupos]
            if all(len(elementos) > 2 for elementos in valor_grupo) and len(valor_grupo) >= 2:
                stats, p = f_oneway(*valor_grupo)#H0 implica que tienen medias similares y no influye sobre la variable target (son independientes)
                if p < pvalue: #Se rechaza H0 y los grupos tienen una elevada varianza. Cada grupo categórico tiene influencia en la variable target (son dependientes)
                    selected_features.append(col)
    return selected_features


def plot_features_cat_regression(df,target_col= "", columns = [], pvalue = 0.05, with_individual_plot = False):
    '''La función tiene como objetivo pintar los histogramas de las variables categóricas que tengan unos pvalores menores al de referencia.

       Argumentos:
       df (pandas dataframe) = corresponden a los datos a los que se les quiere hacer el estudio.
       target_col ('string') = nombre de la columna objetivo
       pvalue ('float') = pvalor de referencia para aceptar o rechazar la hipotesis
       with_individual_plot (None) = argumento por defecto None

       Retorna:

       La funcion retorna los histogramas de las variables categóricas que cumplan los test con la variable objetivo (target) 
    '''
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Por favor, introduce un argumento que sea un DataFrame")
    if not isinstance(target_col,str) or target_col not in df.columns:
        raise ValueError(f"Por favor, revisa que la columna {target_col} introducida existe en el DataFrame.")
    if not isinstance(columns, list):
        raise ValueError("Debes de introducir una lista de columnas")
    missing_cols = [col for col in columns if col not in df.columns]
    if missing_cols:
        raise ValueError("Revisa las columnas, no se encuentran en el DataFrame")
    if not (0 < pvalue < 1):
        raise ValueError("El 'pvalue' introducido debe de estar entre 0 y 1")
    if not isinstance(with_individual_plot, bool):
        raise ValueError("El valor de este parámetro solo puede ser True or False")
    if not np.issubdtype(df[target_col].dtype, np.number):
        print("Error: 'target_col' no es una variable numérica.")
        return None
    if df[target_col].nunique()/len(df)*100 < 10:
        print("Error: 'target_col' no tiene suficiente cardinalidad para regresión.")
        return None
    
    selected_features = []

    if len(columns) == 0: 
        columnas_categoricas = df.select_dtypes(include= ['object','category','bool']).columns.to_list()
        selected_features = []
        for col in columnas_categoricas: 
            if df[col].nunique() ==2:
                categorias = df[col].dropna().unique() #Obtenemos las categorías de la columna (binomial)
                grupo1 = df[df[col] == categorias[0]][target_col].dropna() #Primera categoría
                grupo2 = df[df[col] == categorias[1]][target_col].dropna() #Segunda categoría
                if len(grupo1) > 1 and len(grupo2) >1: #Necesitamos que tenga mas de un elemento para poder hacer el test.
                    stats, p = mannwhitneyu(grupo1, grupo2)
                if p < pvalue:
                    selected_features.append(col)
            elif df[col].nunique() > 2:
                grupos = df[col].dropna().unique()
                valor_grupo= [df[df[col] == grupo][target_col].dropna() for grupo in grupos]
                if all(len(elementos) > 2 for elementos in valor_grupo) and len(valor_grupo) >= 2:
                    stats, p = f_oneway(*valor_grupo)#H0 implica que tienen medias similares y no influye sobre la variable target (son independientes)
                    if p < pvalue: #Se rechaza H0 y los grupos tienen una elevada varianza. Cada grupo categórico tiene influencia en la variable target (son dependientes)
                        selected_features.append(col)
                        sns.histplot(data = df, x= target_col, hue = col)
                        plt.title(f'Histograma entre {target_col} y {col}')
                        plt.tight_layout()
                        plt.show()
    

    if len(columns) > 0:
        columnas_categoricas = [col for col in columns if df[col].dtype in ['object', 'category', 'bool']]
    
        for col in columnas_categoricas: 
            if df[col].nunique() ==2:
                categorias = df[col].dropna().unique() #Obtenemos las categorías de la columna (binomial)
                grupo1 = df[df[col] == categorias[0]][target_col].dropna() #Primera categoría
                grupo2 = df[df[col] == categorias[1]][target_col].dropna() #Segunda categoría
                if len(grupo1) > 1 and len(grupo2) >1: #Necesitamos que tenga mas de un elemento para poder hacer el test.
                    stats, p = mannwhitneyu(grupo1, grupo2)
                if p < pvalue:
                    selected_features.append(col)
            elif df[col].nunique() > 2:
                grupos = df[col].dropna().unique()
                valor_grupo= [df[df[col] == grupo][target_col].dropna() for grupo in grupos]
                if all(len(elementos) > 2 for elementos in valor_grupo) and len(valor_grupo) >= 2:
                    stats, p = f_oneway(*valor_grupo)#H0 implica que tienen medias similares y no influye sobre la variable target (son independientes)
                    if p < pvalue: #Se rechaza H0 y los grupos tienen una elevada varianza. Cada grupo categórico tiene influencia en la variable target (son dependientes)
                        selected_features.append(col)
                        sns.histplot(data = df, x=target_col, hue = col)
                        plt.title(f'Histograma entre {target_col} y {col}')
                        plt.tight_layout()
                        plt.show()
    return selected_features

