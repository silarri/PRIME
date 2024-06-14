import numpy as np
import pandas as pd

# Cargar el archivo Excel
ruta_archivo = 'Sintetico_v1.10000.xlsx'
ruta_archivo_salida = 'Resultado_v1.10000.txt'
# ruta_archivo_salida = 'Resultado_v1.10000.xlsx'

df = pd.read_excel(ruta_archivo)

# Mostrar las primeras filas para verificar la carga correcta
print("Primeras filas del DataFrame original:")
print(df.head())

# Eliminar filas duplicadas basadas en la columna nCultivo
df = df.drop_duplicates(subset='Nº Cultivo')

# Identificar columnas de medicamentos
columnas_medicamentos = [col for col in df.columns if " - CMI" in col or " - Sensibilidad" in col]
otras_columnas = [col for col in df.columns if col not in columnas_medicamentos]

print("Columnas de medicamentos identificadas:")
print(columnas_medicamentos)

# Verificar si se identificaron columnas de medicamentos
if not columnas_medicamentos:
    raise ValueError("No se encontraron columnas de medicamentos con ' - CMI' o ' - Sensibilidad'.")

# Derretir el DataFrame
df_reformateado = pd.melt(df, id_vars=otras_columnas, value_vars=columnas_medicamentos,
                          var_name="Medicamento_Metrica", value_name="Valor")

# Mostrar las primeras filas del DataFrame derretido para verificación
print("Primeras filas del DataFrame derretido:")
print(df_reformateado.head())

# Separar las columnas de Medicamento y Métrica
df_reformateado[['Medicamento', 'Metrica']] = df_reformateado['Medicamento_Metrica'].str.rsplit(' - ', n=1, expand=True)
df_reformateado.drop(columns=['Medicamento_Metrica'], inplace=True)

# Verificar la separación de columnas
print("Primeras filas después de separar Medicamento y Métrica:")
print(df_reformateado.head())

# Guardar los datos transformados en un nuevo archivo de texto (txt)

df_reformateado.to_csv(ruta_archivo_salida, sep='\t', index=False)
# df_reformateado.to_excel(ruta_archivo_salida, index=False)

print(f'Datos transformados guardados en {ruta_archivo_salida}')

