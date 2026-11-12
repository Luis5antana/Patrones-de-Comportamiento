# Dropbox: 4.2.1 Attackers Adapt: Evading and Hardening an ML Detector

- **Curso:** Patrones de Comportamiento de Datos (971), periodo 20262, Blackboard UABC
- **Fecha de vencimiento:** 3 de noviembre de 2026, 23:59 (UTC-8)
- **Puntos:** 100
- **Intentos restantes:** 1
- **Entrega tardía:** sí, se acepta; el intento nuevo se marca como atrasado
- **Nota sobre las instrucciones:** en la página de evaluación dice "No se agregaron instrucciones". Las instrucciones completas están en el documento del Contenido del curso. Este archivo resume ese documento.
- **Nota del libro de calificaciones:** en el libro aparece como "Calificado", pero su página de detalle dice "El elemento está vencido, y usted no lo ha enviado". Se cuenta como faltante: nada fue enviado.

## Objetivo

Mostrar cómo un atacante adapta su tráfico para evadir un detector de machine learning (un beacon C2) y cómo endurecer ese detector.

## Paso a paso

1. Implementa o usa el detector de **beacon C2** (tráfico de comando y control).
2. Aplica el **Mimic Attack** (ataque de imitación) contra el detector, con los presupuestos de ataque indicados.
3. Mide la detección del detector ante el ataque para cada presupuesto:
   - Presupuesto **0.5** → detección **1.0**
   - Presupuesto **0.75** → detección **0.900**
   - Presupuesto **1.0** → detección **0.193**
4. Implementa la función **`harden()`** para endurecer el detector frente al ataque.
5. Mide de nuevo la detección con el detector endurecido.
6. Redacta el **reporte Red Team** con los análisis pedidos en el documento.

## Archivos y parámetros clave

- Detector: beacon C2.
- Ataque: Mimic Attack.
- Presupuestos: 0.5 / 0.75 / 1.0.
- Detección ante el ataque: 1.0 / 0.900 / 0.193.
- Función de endurecimiento: `harden()`.
- Reporte: Red Team, con **4 análisis**.

## Entregables

- El código del detector, del ataque Mimic y de la función `harden()`.
- Los resultados de detección para los tres presupuestos (0.5, 0.75 y 1.0).
- El reporte Red Team con los 4 análisis.

## Rúbrica

El resumen del informe no detalla una rúbrica con porcentajes para esta actividad. Revisa el documento del Contenido antes de entregar.

## Preguntas de reflexión / validación

El reporte Red Team debe incluir los **4 análisis** indicados en el documento del Contenido. Revisa ese documento para ver cuáles son exactamente y respóndelos en el reporte.

Fuente: Blackboard UABC, Patrones de Comportamiento de Datos (971), documento del Contenido y página de evaluación, revisado 12 nov 2026. Nada entregado a Blackboard.
