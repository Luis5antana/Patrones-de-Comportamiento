# Dropbox: 4.2.2 Containment: Stopping a Worm Before It Spreads

- **Curso:** Patrones de Comportamiento de Datos (971), periodo 20262, Blackboard UABC
- **Fecha de vencimiento:** 3 de noviembre de 2026, 23:59 (UTC-8)
- **Puntos:** 100
- **Intentos restantes:** 1
- **Entrega tardía:** sí, se acepta; el intento nuevo se marca como atrasado
- **Nota sobre las instrucciones:** en la página de evaluación dice "No se agregaron instrucciones". Las instrucciones completas están en el documento del Contenido del curso. Este archivo resume ese documento.

## Objetivo

Contener la propagación de un gusano (worm) en una red, eligiendo dónde intervenir para reducir al mínimo los equipos infectados.

## Paso a paso

1. Modela la propagación del gusano sobre una red de **249 hosts**.
2. Usa el parámetro de propagación **beta 0.25**.
3. Mide la propagación **sin defensa**: se infecta el **70.4%** de los hosts.
4. Aplica la estrategia de parchar los hubs: al parchar **9 hubs**, la infección baja al **25.9%**.
5. Implementa la función **`defend(g)`**, que elige las intervenciones de defensa sobre el grafo `g`.
6. La defensa debe usar **como máximo 10 cambios** y lograr como objetivo que la infección quede **por debajo del 15%**.

## Archivos y parámetros clave

- Hosts de la red: 249.
- beta: 0.25.
- Sin defensa: 70.4% infectado.
- Parchando 9 hubs: 25.9% infectado.
- Función de defensa: `defend(g)`.
- Límite: máximo 10 cambios.
- Objetivo: infección menor al 15%.

## Entregables

- El código del modelo de propagación del gusano.
- La función `defend(g)` con su estrategia de defensa.
- Los resultados: sin defensa (70.4%), parchando 9 hubs (25.9%) y con la defensa propuesta (objetivo < 15% con ≤ 10 cambios).
- El reporte con la estrategia y los resultados.

## Rúbrica

El resumen del informe no detalla una rúbrica con porcentajes para esta actividad. Revisa el documento del Contenido antes de entregar.

## Preguntas de reflexión / validación

El resumen del informe no lista preguntas de reflexión específicas para esta actividad. Si el documento del Contenido incluye preguntas, respóndelas en la entrega.

Fuente: Blackboard UABC, Patrones de Comportamiento de Datos (971), documento del Contenido y página de evaluación, revisado 12 nov 2026. Nada entregado a Blackboard.
