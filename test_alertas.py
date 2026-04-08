# test_alertas.py
from alertas import analizar_riesgos

def test_alerta_calor_extremo():
    """Valida la detección de calor extremo >= 40ºC"""
    datos = {'temperatura': 42.5, 'viento': 10, 'humedad': 30}
    resultado = analizar_riesgos(datos)
    assert any("ALERTA ROJA" in s for s in resultado)

def test_alerta_viento_fuerte():
    """Valida la detección de viento fuerte > 70 km/h"""
    datos = {'temperatura': 20, 'viento': 85, 'humedad': 50}
    resultado = analizar_riesgos(datos)
    assert any("VIENTO" in s for s in resultado)

def test_alerta_humedad_extrema():
    """Valida la detección de humedad extrema >= 90%"""
    datos = {'temperatura': 15, 'viento': 5, 'humedad': 95}
    resultado = analizar_riesgos(datos)
    assert any("HUMEDAD" in s for s in resultado)

def test_datos_invalidos():
    """Asegura que el programa no explote con datos erróneos"""
    datos = {'temperatura': "Mucho calor", 'viento': 10, 'humedad': 30}
    resultado = analizar_riesgos(datos)
    assert any("Error" in s for s in resultado)

if __name__ == "__main__":
    # Ejecución manual si no usan pytest
    print("🧪 Ejecutando suite de pruebas locales...")
    try:
        test_alerta_calor_extremo()
        test_alerta_viento_fuerte()
        test_alerta_humedad_extrema()
        test_datos_invalidos()
        print("¡Pruebas superadas con éxito! ✅")
    except AssertionError as e:
        print(f"❌ Error en los tests: {e}")