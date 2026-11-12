# Dropbox: 2.2.5 Automated Box Counter on High-Speed Conveyor Belt

- **Curso:** Patrones de Comportamiento de Datos (971), periodo 20262, Blackboard UABC
- **Fecha de vencimiento:** 30 de agosto de 2026, 23:59 (UTC-7)
- **Puntos:** 100
- **Intentos restantes:** 1
- **Entrega tardía:** sí, se acepta; el intento nuevo se marca como atrasado
- **Nota sobre las instrucciones:** en la página de evaluación dice "No se agregaron instrucciones". Las instrucciones completas están en el documento del Contenido del curso. Este archivo resume ese documento.

## Objetivo

Contar automáticamente las cajas que pasan por una banda transportadora de alta velocidad, detectando cada cruce por una línea de conteo.

## Paso a paso

1. Detecta las cajas en cada cuadro del video de la banda transportadora.
2. Calcula el centroide de cada caja detectada con los momentos de la imagen: **centroide = M10 / M00** (coordenada x) y el equivalente para y.
3. Descarta las detecciones con área menor a **AREA_MIN = 2000**.
4. Define una línea de conteo y registra el cruce cuando la posición vertical de la caja pasa de un lado a otro de la línea, es decir, cuando se cumple **y_prev < y_line <= y_curr**.
5. Incrementa el contador en cada cruce detectado.
6. Verifica el conteo contra el video y guarda la evidencia.

## Archivos y parámetros clave

- Centroide: M10 / M00.
- AREA_MIN: 2000.
- Condición de cruce: y_prev < y_line <= y_curr.
- Video de evidencia: máximo **45 segundos**.

## Entregables

- El código del contador automático de cajas.
- El video de evidencia (máximo 45 s) mostrando el conteo en la banda.
- El reporte con el conteo obtenido.

## Rúbrica

El resumen del informe no detalla una rúbrica con porcentajes para esta actividad. Revisa el documento del Contenido antes de entregar.

## Preguntas de reflexión / validación

El resumen del informe no lista preguntas de reflexión específicas para esta actividad. Si el documento del Contenido incluye preguntas, respóndelas en la entrega.

Fuente: Blackboard UABC, Patrones de Comportamiento de Datos (971), documento del Contenido y página de evaluación, revisado 12 nov 2026. Nada entregado a Blackboard.
