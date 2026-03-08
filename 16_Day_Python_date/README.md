# Día 16: Python Datetime 📅

Hoy he aprendido a dominar el tiempo en Python gracias al módulo integrado `datetime`. Manejar fechas y horas es esencial, ya que los datos rara vez son estáticos y casi siempre tienen una marca de tiempo (*timestamp*) asociada.

### 🧠 Conceptos Aprendidos
- **El módulo `datetime`:** Contiene clases para manipular fechas (`date`), horas (`time`) y ambas cosas a la vez (`datetime`).
- **Obtener la hora actual:** Uso de `datetime.now()`.
- **Formateo de fechas (`strftime`):** Convertir un objeto de fecha en una cadena de texto legible por humanos usando códigos de formato (ej: `%Y` para el año, `%m` para el mes).
- **Lectura de fechas (`strptime`):** El proceso inverso, convertir una cadena de texto (ej: "1 Enero 2024") en un objeto `datetime` que el ordenador pueda entender y operar.
- **Operaciones de tiempo (`timedelta`):** Sumar, restar y calcular la diferencia exacta en días, segundos o microsegundos entre dos fechas.



### 💻 Ejercicios Realizados
- [x] Extracción individual de día, mes, año y hora actual.
- [x] Formateo personalizado de fechas.
- [x] Conversión de *strings* a objetos *datetime*.
- [x] Cálculo de diferencias de tiempo (cuenta atrás para Año Nuevo).
- [x] Cálculo del *timestamp* clásico (tiempo transcurrido desde el 1 de Enero de 1970).

### 🛠️ Aplicación en IA
El manejo del tiempo es el pilar de un campo entero de la Inteligencia Artificial: **Las Series Temporales (Time Series Forecasting)**.
1.  **Predicciones:** Si quieres que una IA prediga el valor en bolsa de una empresa, el clima del mes que viene o la demanda de un producto, los datos de entrada son siempre objetos `datetime`.
2.  **Logs y Monitorización:** Cuando dejas un modelo entrenando durante horas o días, usas `datetime` para registrar exactamente cuánto tarda cada época (*epoch*) de entrenamiento. 