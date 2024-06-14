from queue import Full
import os
from matplotlib import pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import joblib
import re


# Especificar la carpeta donde guardar los modelos
carpeta_modelos = 'C:/Users/rober/OneDrive - unizar.es/Escritorio/TFG/Analisis/modelosRF_5000/Staphylococcus epidermidis'

# Crear la carpeta si no existe
os.makedirs(carpeta_modelos, exist_ok=True)

def limpiar_nombre_archivo(nombre):
    # Reemplazar caracteres no válidos por guion bajo
    nombre_limpio = re.sub(r'[^\w\s-]', '', nombre).replace(' ', '_').replace('/', '_')
    return nombre_limpio

# Especificar la enfermedad en concreto que deseas filtrar
enfermedad = 'Staphylococcus epidermidis'

# Cargar solo las columnas seleccionadas desde el archivo Excel
columnas_usadas = ['Sexo del Paciente', 'Edad del Paciente', 'Peso', 'Descripción', 'Medicamento', 'Valor', 'Metrica']
data = pd.read_csv("Resultado_v1.5000.txt", delimiter="\t", usecols=columnas_usadas, low_memory=False)

medicamentos_unicos = data['Medicamento'].unique()

resultados = {}

# Abrir el archivo de texto para escribir los resultados
with open('modelosRF_5000/Staphylococcus epidermidis/resultados.txt', 'w') as archivo_resultados:
    for medicamento in medicamentos_unicos:
        # Filtrar los datos para incluir solo las filas con la enfermedad, medicamento y métrica especificados
        datos_filtrados = data[(data['Descripción'] == enfermedad) & 
                            (data['Medicamento'] == medicamento) &
                            (data['Metrica'] == 'Sensibilidad') &
                            (data['Valor'].notnull())]

        # Mostrar las primeras líneas del DataFrame datos_filtrados
        #archivo_resultados.write(f"Medicamento: {medicamento}, Numero filas: {len(datos_filtrados)}\n")

        if len(datos_filtrados) < 20:
            #archivo_resultados.write(f"\n")
            #print(medicamento)
            # resultados[medicamento] = {'precision': 0, 'modelo': None}
            continue
        
        # Preprocesamiento de los datos
        datos_filtrados = pd.get_dummies(datos_filtrados, columns=['Sexo del Paciente'])
        # print(datos_filtrados.head())
        # Eliminar la columna 'Metrica' del DataFrame datos_filtrados
        datos_filtrados = datos_filtrados.drop('Metrica', axis=1)
        datos_filtrados = datos_filtrados.drop('Descripción', axis=1)
        datos_filtrados = datos_filtrados.drop('Medicamento', axis=1)

        # Dividir los datos en conjunto de entrenamiento y prueba
        X = datos_filtrados.drop('Valor', axis=1)
        y = datos_filtrados['Valor']
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Crear el modelo de clasificación
        modelo = RandomForestClassifier(n_estimators=100, random_state=42)

        # Entrenar el modelo
        modelo.fit(X_train, y_train)

        # Predecir en el conjunto de prueba
        y_pred = modelo.predict(X_test)

        # Calcular la precisión del modelo
        precision = accuracy_score(y_test, y_pred)
        resultados[medicamento] = {'precision': precision, 'modelo': modelo}


        # Limpiar el nombre del archivo y conservar la extensión
        nombre_base = limpiar_nombre_archivo(f'modelo_{medicamento}')
        nombre_archivo_limpio = f'{nombre_base}.joblib'

        archivo_resultados.write(f"{medicamento}, {nombre_archivo_limpio}, {precision}, {len(datos_filtrados)}\n")
        print(f"{medicamento}, {nombre_archivo_limpio}, {precision}, {len(datos_filtrados)}\n")

        # Guardar el modelo
        nombre_archivo = os.path.join(carpeta_modelos, nombre_archivo_limpio)
        joblib.dump(modelo, nombre_archivo)        
        #archivo_resultados.write(f'Modelo para {medicamento} guardado en {nombre_archivo}\n')




