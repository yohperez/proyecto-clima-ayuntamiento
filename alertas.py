# alertas.py

# Configuración de umbrales según el MVP y la guía técnica
ALERTAS_CONFIG = {
    'calor_roja':    {'campo': 'temperatura', 'umbral': 40, 'msj': '🔴 ALERTA ROJA: Calor extremo (≥40ºC). Protocolo activado.'},
    'calor_naranja': {'campo': 'temperatura', 'umbral': 35, 'msj': '🟠 ALERTA NARANJA: Calor alto (≥35ºC). Precaución.'},
    'viento_fuerte': {'campo': 'viento',      'umbral': 70, 'msj': '💨 ALERTA VIENTO: Riesgo por rachas fuertes (>70 km/h).'},
    'humedad_ext':   {'campo': 'humedad',     'umbral': 90, 'msj': '💧 ALERTA HUMEDAD: Humedad extrema (≥90%).'},
    'hielo':         {'campo': 'temperatura', 'umbral': 0,  'msj': '❄️ AVISO HELADA: Riesgo de placas de hielo.', 'tipo': 'frio'}
}

def analizar_riesgos(registro):
    """
    Analiza un diccionario de registro y detecta situaciones de riesgo.
    Retorna una lista con los mensajes de alerta encontrados.
    """
    alertas_detectadas = []
    
    try:
        # Validamos que los datos necesarios existan y sean numéricos
        for clave, conf in ALERTAS_CONFIG.items():
            valor_sensor = registro.get(conf['campo'])
            
            if valor_sensor is None:
                continue
                
            valor = float(valor_sensor)
            
            # Lógica para frío (menor o igual) y calor/viento/humedad (mayor o igual)
            if conf.get('tipo') == 'frio':
                if valor <= conf['umbral']:
                    alertas_detectadas.append(conf['msj'])
            else:
                if valor >= conf['umbral']:
                    alertas_detectadas.append(conf['msj'])

    except (ValueError, TypeError):
        return ["❌ Error: Los datos climáticos para alertas deben ser numéricos."]

    # Mostrar resultados por consola para el operario
    if not alertas_detectadas:
        print("✅ Información: Sin riesgos detectados en esta zona.")
    else:
        print(f"🚨 ALERTAS DETECTADAS:")
        for msj in alertas_detectadas:
            print(f"   {msj}")
            
    return alertas_detectadas