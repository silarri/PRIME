import pandas as pd
import random
import numpy as np
from datetime import datetime, timedelta

# Nombre del archivo de entrada y salida
archivo_entrada = 'Antibiogramav0.10.xlsx'
archivo_salida = 'Sintetico_v1.10000.xlsx'

# Cargar el archivo CSV en un DataFrame de pandas
try:
    df = pd.read_excel(archivo_entrada)
except FileNotFoundError:
    print(f"El archivo {archivo_entrada} no se encontró.")
except pd.errors.EmptyDataError:
    print(f"El archivo {archivo_entrada} está vacío.")
except pd.errors.ParserError:
    print(f"Error al analizar el archivo {archivo_entrada}. ¿Es un archivo XlSX válido?")



columnas_aux = ['Fecha', 'Fecha de solicitud', 'Extracción', 'Fecha de Activación', 'Número', 
                'Fecha Nacimiento', 'Sexo del Paciente', 'Edad del Paciente', 'Historia H.Clinico', 
                'Tipo de Paciente', 'Servicio', 'Prueba', 'Muestra','Nº Cultivo']

datos_generados = []
n_cultivo_counter = 1  # Inicializar el contador para n_cultivo
historia_H_counter = 10000  # Inicializar el contador para n_cultivo
numero_counter = 10000000  # Inicializar el contador para n_cultivo
for _ in range(10000):

#-------------------------------------------------------------------------------------------------------------
    # Definir el rango de fechas para el año 2022
    fecha_inicio = datetime(2022, 1, 1)
    fecha_fin = datetime(2022, 12, 31)

    # Calcular la diferencia entre las fechas de inicio y fin
    diferencia = fecha_fin - fecha_inicio

    # Generar una fecha aleatoria dentro del rango
    fecha_aleatoria = fecha_inicio + timedelta(days=random.randint(0, diferencia.days))
    fecha_formateada = fecha_aleatoria.strftime("%d/%m/%y")

#-------------------------------------------------------------------------------------------------------------
    # Generar una hora aleatoria entre 0 y 23 para las horas
    hora = random.randint(0, 23)
    # Generar una hora aleatoria entre 0 y 59 para los minutos
    minutos = random.randint(0, 59)

    # Formatear la hora aleatoria en una cadena de texto en formato HH:MM:SS
    hora_aleatoria = "{:02d}:{:02d}".format(hora, minutos)

#-------------------------------------------------------------------------------------------------------------
    # Generar una hora aleatoria entre 0 y 59 para los minutos
    fecha_aleatoria_act = fecha_aleatoria
    minutos_mas = random.randint(0, 59)
    minutos += minutos_mas
    if minutos > 60: 
        hora = hora + 1
        minutos = minutos - 60
    if hora >= 24: 
        hora = 0
        fecha_aleatoria_act  = fecha_aleatoria_act + timedelta(days=1)
    # Formatear la hora aleatoria en una cadena de texto en formato HH:MM:SS
    hora_aleatoria_mas = "{:02d}:{:02d}".format(hora, minutos)
    fecha_formateada_act = fecha_aleatoria_act.strftime("%d/%m/%y")

#-------------------------------------------------------------------------------------------------------------
    #numero = random.randint(10000000, 99999999) 
    numero = numero_counter  # Asignar el valor del contador
    numero_counter += 1  # Incrementar el contador para la siguiente iteración

#-------------------------------------------------------------------------------------------------------------
    # Parámetros de la distribución de edades
    media_1, std_1, peso_1 = 10, 5, 0.3  # Infancia
    media_2, std_2, peso_2 = 70, 10, 0.7  # Vejez

    # Elegir cuál de las dos distribuciones usar según los pesos
    if np.random.rand() < peso_1:
        edad = np.random.normal(media_1, std_1)
    else:
        edad = np.random.normal(media_2, std_2)

    # Asegurar que la edad esté en el rango válido
    edad = np.clip(edad, 0, 100).astype(int)

    edad = int(edad)  # Asegurarse de que es un entero estándar de Python

    # Calcular la fecha de nacimiento
    fecha_actual = datetime.today()
    dias_edad = int(edad * 365.25)  # Considerar años bisiestos de forma aproximada
    fecha_nac_aleatoria = fecha_actual - timedelta(days=dias_edad)
    
    # Formatear la fecha de nacimiento
    fecha_nac_formateada = fecha_nac_aleatoria.strftime("%d/%m/%y")

#-------------------------------------------------------------------------------------------------------------
    # Generar una cadena aleatoria entre valor1 y valor2
    sexo = random.choice(["F", "M"])

#-------------------------------------------------------------------------------------------------------------
    # Generar el peso del usuario según la edad y el genero
    def generar_peso_aleatorio(edad, genero):
        # Definir los rangos de peso basados en la edad y el género
        rangos_peso = {
            'M': {
                (0, 5): (10, 20),
                (6, 12): (20, 40),
                (13, 18): (40, 70),
                (19, 30): (60, 90),
                (31, 50): (70, 100),
                (51, 70): (65, 90),
                (71, 100): (60, 85)
            },
            'F': {
                (0, 5): (9, 19),
                (6, 12): (18, 35),
                (13, 18): (35, 60),
                (19, 30): (50, 80),
                (31, 50): (60, 85),
                (51, 70): (55, 80),
                (71, 100): (50, 75)
            }
        }
        
        # Encontrar el rango de peso correspondiente a la edad y el género
        for rango_edad, rango_peso in rangos_peso[genero].items():
            if rango_edad[0] <= edad <= rango_edad[1]:
                peso_min, peso_max = rango_peso
                peso_aleatorio = random.uniform(peso_min, peso_max)
                return peso_aleatorio
        
        raise ValueError("Edad fuera de rango.")

    peso = int(generar_peso_aleatorio(edad, sexo))
    print(f"Peso generado para un {sexo} de {edad} años: {peso:.2f} kg")

#-------------------------------------------------------------------------------------------------------------
    #historia_H = random.randint(10000, 999999)
    historia_H = historia_H_counter  # Asignar el valor del contador
    historia_H_counter += 1  # Incrementar el contador para la siguiente iteración

#-------------------------------------------------------------------------------------------------------------
    tipo_paciente = "Ingresado"

#-------------------------------------------------------------------------------------------------------------
    servicio = random.choice(["UCI Médica", "UCI Central", "UCI Quirúrgica"])

#-------------------------------------------------------------------------------------------------------------
    hcul = "HCUL"

#-------------------------------------------------------------------------------------------------------------
    muestra = "Sangre"

#-------------------------------------------------------------------------------------------------------------
    n_cultivo = n_cultivo_counter  # Asignar el valor del contador
    n_cultivo_counter += 1  # Incrementar el contador para la siguiente iteración


#-------------------------------- CARGA DE DATOS ---------------------------------------------------
#---------------------------------------------------------------------------------------------------

    # Aquí se insertan los datos adicionales al nuevo archivo Excel
    # Se crea un nuevo DataFrame con tus datos y agregarlo al archivo Excel
    fila = [fecha_formateada, fecha_formateada + " " + hora_aleatoria, "",fecha_formateada_act + " " + hora_aleatoria_mas,
            numero, fecha_nac_formateada, sexo, edad, peso, historia_H, 
            tipo_paciente, servicio, hcul, muestra,n_cultivo]
    # Escribir los datos adicionales en el archivo Excel
    noNan = False
    # Seleccionar una fila aleatoria del DataFrame original
    fila_aleatoria = df.sample(n=1)

    # Obtener una lista de todas las columnas excepto las dos que deseas excluir
    columnas_a_mantener = [col for col in df.columns if col not in columnas_aux]

    # Obtener los valores de las columnas deseadas de la fila seleccionada
    valores_columnas_deseadas = fila_aleatoria[columnas_a_mantener].values.tolist()

    fila.extend(valores_columnas_deseadas[0])

    # Agregar la fila al conjunto de datos generados
    datos_generados.append(fila)


# Obtener el índice de la columna "Edad del Paciente"
indice_edad = df.columns.get_loc("Edad del Paciente")

# Dividir las columnas originales en dos partes, antes y después de la columna "Edad del Paciente"
columnas_antes = df.columns[:indice_edad + 1]  # +1 para incluir la columna "Edad del Paciente"
columnas_despues = df.columns[indice_edad + 1:]

# Crear una lista de columnas para el DataFrame nuevo, insertando la nueva columna después de "Edad del Paciente"
columnas_nuevo_df = list(columnas_antes) + ['Peso'] + list(columnas_despues)

# Crear el DataFrame usando las columnas actualizadas
nuevo_df = pd.DataFrame(datos_generados, columns=columnas_nuevo_df)


# Guardar el nuevo DataFrame como un archivo de Excel
try:
    nuevo_df.to_excel(archivo_salida, index=False)
    print(f"Se ha creado el archivo {archivo_salida} con los datos generados.")
except PermissionError:
    print(f"No se puede escribir en el archivo {archivo_salida}. ¿Tienes permiso para escribir en esta ubicación?")
except Exception as e:
    print(f"Se produjo un error al guardar el archivo: {str(e)}")
