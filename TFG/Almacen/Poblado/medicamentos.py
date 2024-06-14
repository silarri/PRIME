from googletrans import Translator
import pandas as pd

# Leer el archivo con los nombres de medicamentos en español (reemplaza 'nombres_unicos.xls' con el nombre de tu archivo)
archivo_nombres_es = 'medicamentos.xlsx'
df_nombres_es = pd.read_excel(archivo_nombres_es)

# Función para traducir nombres de medicamentos de español a inglés
def traducir_nombres(nombres_es):
    translator = Translator()
    nombres_en = []

    for nombre_es in nombres_es:
        translation = translator.translate(nombre_es, src='es', dest='en')
        nombres_en.append(translation.text)

    return nombres_en

# Traducir los nombres de medicamentos de español a inglés
nombres_es = df_nombres_es['Nombres'].tolist()
nombres_en = traducir_nombres(nombres_es)

# Crear un diccionario de mapeo de nombres en español a nombres en inglés
mapa_nombres = dict(zip(nombres_es, nombres_en))

# Crear una columna de nombres en inglés en el DataFrame de nombres en español
df_nombres_es['Drug Name'] = df_nombres_es['Nombres'].map(mapa_nombres)

# Leer el archivo con los datos de los medicamentos en inglés (reemplaza 'medicamentos_en_ingles.xls' con el nombre de tu archivo)
archivo_datos_en = 'data.xlsx'
df_datos_en = pd.read_excel(archivo_datos_en)

# Fusionar los datos basándonos en los nombres de los medicamentos
df_fusionado = pd.merge(df_nombres_es, df_datos_en, on='Drug Name', how='left')

# Guardar el DataFrame fusionado en un nuevo archivo Excel en formato .xls
archivo_salida = 'datos_fusionados.xls'
df_fusionado.to_excel(archivo_salida, index=False, engine='openpyxl')

print(f"Los datos fusionados se han guardado en '{archivo_salida}'.")
