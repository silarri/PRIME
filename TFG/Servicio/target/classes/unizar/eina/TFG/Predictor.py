import os
import sys
import joblib
import pandas as pd


if len(sys.argv) != 5:
    print("Uso: python script.py sexo edad peso enfermedad")
    sys.exit(1)

sexo_paciente = sys.argv[1]
edad_paciente = int(sys.argv[2])
peso_paciente = float(sys.argv[3])
enfermedad = sys.argv[4]
# ------ Staphylococcus epidermidis ------
# Pedir datos de entrada al usuario
# sexo_paciente = input("Ingrese el sexo del paciente (Masculino/Femenino): ")
# edad_paciente = int(input("Ingrese la edad del paciente: "))
# peso_paciente = float(input("Ingrese el peso del paciente en kg: "))
# enfermedad = input("Ingrese la enfermedad (debe coincidir con la carpeta de los modelos): ")

# Datos de entrada proporcionados por el usuario
datos_usuario = {
    'Sexo del Paciente': sexo_paciente,
    'Edad del Paciente': edad_paciente,
    'Peso': peso_paciente,
    'Enfermedad': enfermedad
}



# Especificar la carpeta donde guardar los modelos
carpeta_modelos_relativa = 'modelosRF_5000/'+enfermedad

# Obtener el directorio de trabajo actual
directorio_actual = os.getcwd()

# Construir la ruta completa
carpeta_modelos = os.path.join(directorio_actual, carpeta_modelos_relativa)

# Especificar la carpeta donde se encuentran los modelos


# Convertir los datos del usuario en un DataFrame
df_usuario = pd.DataFrame([datos_usuario])

# Convertir la columna 'Sexo del Paciente' a variables dummy
df_usuario = pd.get_dummies(df_usuario, columns=['Sexo del Paciente'])
# print(df_usuario.columns)
# Asegurar que todas las columnas esperadas están presentes
columnas_esperadas = ['Edad del Paciente', 'Peso', 'Sexo del Paciente_F', 'Sexo del Paciente_M']
for columna in columnas_esperadas:
    if columna not in df_usuario.columns:
        df_usuario[columna] = 0

# Ordenar las columnas para que coincidan con las columnas utilizadas en el entrenamiento de los modelos
df_usuario = df_usuario[columnas_esperadas]

# Crear un diccionario para almacenar las predicciones
predicciones = {}

# # Cargar cada modelo en la carpeta y realizar la predicción
# for archivo in os.listdir(carpeta_modelos):
#     if archivo.endswith('.joblib'):
#         # Cargar el modelo
#         modelo = joblib.load(os.path.join(carpeta_modelos, archivo))

#         # Realizar la predicción
#         prediccion = modelo.predict(df_usuario)
#         # Guardar la predicción en el diccionario
#         nombre_modelo = archivo.replace('modelo_', '').replace('.joblib', '')
#         predicciones[nombre_modelo] = prediccion[0]


precisiones = {}
numFilas = {}
with open('C:/Users/rober/OneDrive - unizar.es/Escritorio/TFG/Analisis/modelosRF_5000/'+enfermedad+'/resultados.txt', 'r') as fichero:
    for linea in fichero:
        medicamento, fichModelo, precision, filas = linea.strip().split(', ')
        precisiones[medicamento.strip()] = float(precision.strip())

        # Cargar el modelo
        modelo = joblib.load(os.path.join(carpeta_modelos, fichModelo))
        # Realizar la predicción
        prediccion = modelo.predict(df_usuario)
        # Guardar la predicción en el diccionario
        predicciones[medicamento] = prediccion[0]
        numFilas[medicamento] = filas

# Mostrar las predicciones
for medicamento, prediccion in predicciones.items():
    precision = precisiones.get(medicamento, 'N/A')
    fila = numFilas.get(medicamento, 'N/A')
    print(f'Medicamento: {medicamento}, Prediccion: {prediccion}, Precision: {precision}, Filas: {fila}')

