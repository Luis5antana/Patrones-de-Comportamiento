# Sistema Local de Detección y Reconocimiento Facial en Tiempo Real

Este proyecto implementa un sistema de visión por computadora para detectar rostros y reconocer a personas en tiempo real usando la cámara del equipo. Está orientado a un uso local, sin depender de servicios en la nube, y utiliza OpenCV con un clasificador Haar Cascade y un reconocedor LBPH.

## Descripción

La aplicación permite:

- Capturar un conjunto de imágenes de rostros para crear un dataset.
- Entrenar un modelo de reconocimiento facial con LBPH.
- Ejecutar reconocimiento facial en tiempo real desde la webcam.
- Identificar personas registradas y mostrar etiquetas en pantalla.
- Detectar rostros no reconocidos con una clasificación por defecto.

El proyecto está pensado para reconocer a familiares o usuarios registrados localmente y se puede adaptar para otros casos de uso similares.

## Tecnologías utilizadas

- Python 3
- OpenCV (`cv2`)
- NumPy
- Haar Cascade para detección facial
- LBPH Face Recognizer para reconocimiento

## Estructura del proyecto

```text
2.4.1 Local Real-Time Face Detection & Recognition System/
├── face_recognition_system.py
├── haarcascade_frontalface_default.xml
├── dataset/                     # Imágenes capturadas del rostro
├── trainer.yml                  # Modelo entrenado generado automáticamente
├── requirements.txt
└── README.md
```

## Requisitos

Antes de ejecutar el proyecto, asegúrate de tener instalado:

- Python 3.8 o superior
- Pip
- Cámara web disponible o un dispositivo virtual de cámara

## Instalación

1. Abre una terminal en la carpeta del proyecto.
2. Crea un entorno virtual (opcional pero recomendado):

```bash
python -m venv venv
```

3. Activa el entorno virtual:

- Windows:

```bash
venv\Scripts\activate
```

- Linux/macOS:

```bash
source venv/bin/activate
```

4. Instala las dependencias:

```bash
pip install -r requirements.txt
```

## Ejecución

Ejecuta el archivo principal:

```bash
python face_recognition_system.py
```

Al iniciar, el sistema intentará:

1. Detectar si ya existe un modelo entrenado.
2. Si no existe dataset, iniciar la captura para registrar personas.
3. Entrenar el modelo automáticamente.
4. Abrir la cámara para reconocer rostros en tiempo real.

## Cómo funciona

### 1. Captura del dataset

El sistema solicita la cámara y captura múltiples imágenes de rostros para cada persona registrada.

- Se recomienda capturar alrededor de 40 fotos por usuario.
- Cada imagen se guarda en la carpeta `dataset` con el formato:

```text
User.<id>.<número>.jpg
```

### 2. Entrenamiento del modelo

Se recorre el dataset, se detectan los rostros y se entrena un modelo LBPH con las imágenes de entrenamiento.

### 3. Reconocimiento en tiempo real

La cámara se activa y cada rostro detectado se compara con el modelo entrenado. Si la distancia es menor al umbral configurado, el sistema reconoce a la persona; si no, la etiqueta aparece como "Usuario no reconocido".

## Configuración importante

El archivo `face_recognition_system.py` incluye configuraciones clave:

- `SUBJECT_MAP`: mapea IDs con nombres reales de usuarios.
- `MAX_DISTANCE_THRESHOLD`: umbral para decidir si una persona es reconocida o no.
- `camera_index`: índice de la cámara que se desea utilizar.

Ejemplo de configuración:

```python
SUBJECT_MAP = {
    1: "Yo Luis",
    2: "Mama Haydeé",
    3: "Hermana Andrea"
}
```

Puedes cambiar estos nombres para reflejar a tus usuarios reales.

## Teclas de uso

Durante la ejecución, puedes usar:

- `s`: iniciar la captura del dataset
- `q`: salir de la ventana de video

## Nota de uso

Para obtener mejores resultados:

- Usa buena iluminación.
- Asegúrate de que la cara esté centrada frente a la cámara.
- Captura rostros con diferentes expresiones y ángulos.
- Evita mover la cámara continuamente durante el entrenamiento.

## Licencia

Este proyecto se proporciona con fines educativos y de aprendizaje en visión artificial.

## Autor

Proyecto desarrollado como ejemplo de detección y reconocimiento facial local con OpenCV.
