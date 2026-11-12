# Dropbox: 1.1.1 Venv setup delivery

- **Curso:** Patrones de Comportamiento de Datos (971), periodo 20262, Blackboard UABC
- **Fecha de vencimiento:** 14 de agosto de 2026, 23:59 (UTC-7)
- **Puntos:** 100
- **Intentos restantes:** 1
- **Entrega tardía:** sí, se acepta; el intento nuevo se marca como atrasado
- **Nota sobre las instrucciones:** en la página de evaluación dice "No se agregaron instrucciones". Las instrucciones completas están en el documento del Contenido del curso. Este archivo resume ese documento.

## Objetivo

Configurar un entorno virtual de Python (venv) y dejar funcionando el benchmark de referencia de la materia.

## Paso a paso

1. Crea el entorno virtual con el nombre `.venv` en la carpeta de la actividad.
2. Activa el entorno virtual.
3. Instala las dependencias desde `requirements.txt`.
4. Prepara el script `benchmark.py`, que es el archivo principal de esta actividad.
5. Ejecuta `benchmark.py` dentro del entorno activado y verifica que corra sin errores de dependencias.
6. El benchmark trabaja con un conjunto de datos de **5000 muestras x 64** (características).
7. El modelo de referencia usa capas Dense con **128, 64 y 10** neuronas (la última capa de 10 corresponde a las 10 clases de salida).
8. Guarda la salida del benchmark como evidencia de que el entorno quedó bien configurado.

## Archivos y parámetros clave

- `.venv`: entorno virtual de la actividad.
- `requirements.txt`: dependencias a instalar.
- `benchmark.py`: script del benchmark.
- Datos: 5000 muestras x 64 características.
- Modelo: Dense 128 / 64 / 10.

## Entregables

- El entorno virtual `.venv` funcionando con las dependencias instaladas.
- El archivo `benchmark.py` ejecutándose correctamente.
- `requirements.txt` con las dependencias usadas.
- Evidencia de la ejecución del benchmark (salida/resultados).

## Rúbrica

El resumen del informe no detalla una rúbrica con porcentajes para esta actividad. Revisa el documento del Contenido antes de entregar.

## Preguntas de reflexión / validación

El resumen del informe no lista preguntas de reflexión específicas para esta actividad. Si el documento del Contenido incluye preguntas, respóndelas en la entrega.

Fuente: Blackboard UABC, Patrones de Comportamiento de Datos (971), documento del Contenido y página de evaluación, revisado 12 nov 2026. Nada entregado a Blackboard.
