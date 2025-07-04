# Descripción del Proyecto

Este proyecto de Machine Learning tiene como objetivo orientar a profesionales que buscan empleo en el sector tecnológico, especialmente en áreas relacionadas con la Inteligencia Artificial. A través del análisis de datos, el modelo estima cifras salariales que los candidatos pueden tomar como referencia durante entrevistas de trabajo. De esta forma, se facilita una preparación más sólida y segura a la hora de negociar el sueldo.

Para abordar este problema, se ha planteado un enfoque supervisado de regresión, con el fin de predecir el salario esperado en función de diversas variables (como el puesto, experiencia, ubicación, entre otras). Se han comparado varios modelos de regresión (como árboles de decisión, Random Forest, XGBoost, etc.), evaluando su rendimiento mediante la métrica MAE (Mean Absolute Error).

Se ha optado por el MAE como métrica principal debido a su interpretabilidad directa en unidades monetarias (por ejemplo, euros o dólares), lo cual facilita comprender el error medio de predicción del modelo en un contexto salarial. A diferencia de otras métricas como el RMSE, el MAE no penaliza de forma desproporcionada los errores grandes, lo que lo hace más robusto frente a posibles outliers en los datos salariales.

# Fuente de Datos

El conjunto de datos utilizado en este proyecto fue obtenido de Kaggle, una plataforma pública de competencias y recursos de ciencia de datos y aprendizaje automático. Los datos estaban disponibles de forma gratuita y se descargaron en formato CSV. El dataset incluye información relevante sobre puestos de trabajo en el sector tecnológico y de IA, como títulos de empleo, salarios, niveles de experiencia, ubicación de la empresa, entre otros.

URL: https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025/data

# Estructura del Repositorio

El repositorio cuenta con una carpeta llamada 'src' la cual contiene información organizada de la siguiente manera. 
- Una carpeta llamada 'data_sample', donde se encuentra una parte de los datos utilizados
- Una carpeta llamada 'models', donde está guardado el mejor modelo obtenido y optimizado (modelo_optuna.pkl). Los otros modelos clusterizados corresponden a una alternativa que finalmente se ha descartado.
- Una carpeta llamada 'notebooks' donde se pueden encontrar diferentes códigos de análisis
        - codigo : primera aproximación al dataset, analisis visual, EDA bivariante
        - codigo_2 : enfocado más a feature engineering, selección de features mediante modelos
        - codigo_3 : parecido al codigo_2 pero al final se le aplica clusterización al target para comparar métricas por separado y valorar la posibilidad de abordar el problema de manera mixta mediante clasificación y regresión.
- Una carpeta llamada 'utils' donde quedan guardados ficheros de funciones empleados para el analisis y visualización de los datos.

El repositorio también cuenta, en el nivel raíz, con el notebook principal llamado 'main.ipynb' donde se recoge todo el código empleado, ordenado y comentado, y organizado según los pasos para alcanzar el resultado final.

Se facilita un documento soporte en formato PDF que sintetiza todo el proyecto, llamado 'presentación.pdf'.


----------------------


# Project Description

This Machine Learning project is aimed at helping professionals seeking employment in the tech industry, particularly in roles related to Artificial Intelligence. By analyzing relevant data, the model estimates salary figures that candidates can use as a reference during job interviews. This enables more confident and well-informed salary negotiations.

To tackle this challenge, a supervised regression approach was used to predict expected salaries based on various factors (such as job title, experience, location, and more). Multiple regression models were compared (including Decission Tree, Random Forest, XGBoost, etc.), and their performance was evaluated using the MAE (Mean Absolute Error) metric.

MAE was chosen as the primary evaluation metric because of its direct interpretability in monetary units (e.g., euros or dollars), which makes it easier to understand the average prediction error in a real-world salary context. Unlike other metrics such as RMSE, MAE does not disproportionately penalize large errors, making it more robust to potential outliers in salary data.

# Data Source

The dataset used in this project was obtained from Kaggle, a public platform for data science and machine learning competitions. The data was freely accessible and downloaded in CSV format. It contains information relevant to job positions in the tech and AI sectors, including job titles, salaries, experience levels, company locations, and more.

URL: https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025/data

# Repository Structure

The repository includes a folder named src which contains organized project resources structured as follows:

- A folder named 'data_sample', which contains a portion of the dataset used.
- A folder named 'models', where the best optimized model obtained is stored (modelo_optuna.pkl). The other clustered models correspond to an alternative that has finally been discarded.
- A folder named 'notebooks', which contains various analysis notebooks.
        - codigo : first approach to the dataset, visual analysis, bivariate EDA
        - codigo_2 : more focused on feature engineering, feature selection using models
        - codigo_3 : similar to codigo_2 but at the end clustering is applied to the target to compare metrics separately and evaluate the possibility of approaching the problem in a mixed way by classification and regression.
- A folder named 'utils', which holds function scripts used for data analysis and visualization.

At the root level of the repository, there is a main notebook called 'main.ipynb', which consolidates all the code used in the project. It is well-structured, commented, and organized according to the steps taken to reach the final results.

Additionally, a supporting document in PDF format named 'presentación.pdf' is provided, offering a concise summary of the entire project.
