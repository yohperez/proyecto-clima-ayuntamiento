# Validación de datos del dataset de clima 
#Este código valida los datos del dataset de clima, verificando que las fechas sean correctas, que las zonas sean válidas, y que los valores de temperatura, humedad y viento estén dentro de rangos razonables. También detecta filas duplicadas basándose en la combinación de fecha y zona.
#Abre el archivo csv, recorre fila por fila de cada registro, comprueba que los datos sean válidos e imprime errores
import pandas as pd

df = pd.read_csv("clima_dataset.csv")  #Abre el archivo csv y lo carga en un DataFrame 

zonas_validas = ["Centro", "Norte", "Sur", "Este", "Oeste"]   #Definimos la lista de zonas válidas

for i in range(len(df)):    #Recorremos cada una de las filas que tenga el DataFrame

    # FECHA
    fecha = df.loc[i, "fecha"]    #Obtenemos el valor de la columna "fecha" para la fila actual

    if pd.isna(fecha):     #Si el valor de la fecha estávacío, se imprime un mensaje de error indicando que la fecha está vacía
        print(f"Fila {i+2}: fecha vacía")
    else:
        try:
            pd.to_datetime(fecha, format="%Y-%m-%d")    #Compueba si la fecha tiene el formato correcto (YYYY-MM-DD) y si es válida

        except:
            print(f"Fila {i+2}: fecha incorrecta")

    # ZONA
    zona = df.loc[i, "zona"]    #Obtenemos el valor de la columna "zona" para la fila actual

    if pd.isna(zona) or zona == "":   #si la celda de la zona esta vacía
        print(f"Fila {i+2}: zona vacía")
    elif zona not in zonas_validas:      #si la zona no es válida
        print(f"Fila {i+2}: zona incorrecta")

    # TEMPERATURA
    if df.loc[i, "temperatura"] < -20 or df.loc[i, "temperatura"] > 60:  #si la celda de temperatura tiene un valor menor a -20 o mayor a 60, se imprime un mensaje de error indicando que la temperatura es incorrecta
        print(f"Fila {i+2}: temperatura incorrecta")

    # HUMEDAD
    if df.loc[i, "humedad"] < 0 or df.loc[i, "humedad"] > 100:    #si la celda de humedad tiene un valor menor a 0 o mayor a 100, se imprime un mensaje de error indicando que la humedad es incorrecta
        print(f"Fila {i+2}: humedad incorrecta")

    # VIENTO
    if df.loc[i, "viento"] < 0 or df.loc[i, "viento"] > 150:  #si la celda de viento tiene un valor menor a 0 o mayor a 150, se imprime un mensaje de error indicando que el viento es incorrecto   
        print(f"Fila {i+2}: viento incorrecto")

# DUPLICADOS 
duplicados = df.duplicated(subset=["fecha", "zona"], keep=False)   #busca las filas duplicadas, teniendo en cuenta solo las columnas fecha y hora y las marca todas

for i in range(len(df)):
    if duplicados[i]:
        print(f"Fila {i+2}: duplicado")