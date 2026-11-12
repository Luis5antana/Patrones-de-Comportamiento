# Dropbox: 2.2.7 Object Detection with YOLO

- **Curso:** Patrones de Comportamiento de Datos (971), periodo 20262, Blackboard UABC
- **Fecha de vencimiento:** 6 de septiembre de 2026, 23:59 (UTC-7)
- **Puntos:** 100
- **Intentos restantes:** 1
- **Entrega tardía:** sí, se acepta; el intento nuevo se marca como atrasado
- **Nota sobre las instrucciones:** en la página de evaluación dice "No se agregaron instrucciones". Las instrucciones completas están en el documento del Contenido del curso. Este archivo resume ese documento.

## Objetivo

Detección de objetos con YOLO: etiquetar un dataset propio, entrenar un modelo YOLOv11 Nano y evaluar la detección.

## Paso a paso

1. Etiqueta las imágenes del dataset con **Roboflow** o **LabelImg**.
2. Organiza el dataset y define el archivo **`data.yaml`** con la configuración de rutas y clases.
3. Entrena el modelo **YOLOv11 Nano durante 10 épocas**, con **batch 16** e **imagen de 640** (img 640).
4. El dataset de la actividad tiene **5 clases, con 50 imágenes por clase**.
5. Evalúa el modelo entrenado y registra los resultados de detección.

## Archivos y parámetros clave

- Etiquetado: Roboflow / LabelImg.
- `data.yaml`: configuración del dataset.
- Modelo: YOLOv11 Nano.
- Entrenamiento: 10 épocas, batch 16, img 640.
- Clases: 5 clases, 50 imágenes por clase.

## Entregables

- El dataset etiquetado y el archivo `data.yaml`.
- El código de entrenamiento del modelo YOLOv11 Nano.
- El modelo entrenado.
- Los resultados de la evaluación de detección.

## Rúbrica

El resumen del informe no detalla una rúbrica con porcentajes para esta actividad. Revisa el documento del Contenido antes de entregar.

## Preguntas de reflexión / validación

El resumen del informe no lista preguntas de reflexión específicas para esta actividad. Si el documento del Contenido incluye preguntas, respóndelas en la entrega.

Fuente: Blackboard UABC, Patrones de Comportamiento de Datos (971), documento del Contenido y página de evaluación, revisado 12 nov 2026. Nada entregado a Blackboard.
