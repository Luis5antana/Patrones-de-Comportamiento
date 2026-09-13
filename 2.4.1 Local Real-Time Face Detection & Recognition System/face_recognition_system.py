import cv2
import os
import numpy as np


# =====================================================================
# SYSTEM CONFIGURATION & PATHS (Rutas absolutas basadas en la ubicación del script)
# =====================================================================
# Obtiene la ruta exacta de la carpeta donde está guardado este archivo .py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Define las rutas relativas pero asegurando que pertenezcan a esta carpeta
DATASET_DIR = os.path.join(BASE_DIR, "dataset")
TRAINER_FILE = os.path.join(BASE_DIR, "trainer.yml")
CASCADE_PATH = os.path.join(BASE_DIR, "haarcascade_frontalface_default.xml")


# Map integer IDs to the registered family members (3 relatives required).
# Reemplaza estos nombres por los de tus familiares reales (ej. "Mama Maria").
SUBJECT_MAP = {
    1: "Yo Luis",
    2: "Mama Haydeé",
    3: "Hermana Andrea"
}


# Recognition threshold settings (LBPH distance cutoff)
# Lower distance means better match. Distance > MAX_DISTANCE_THRESHOLD is unrecognized.
MAX_DISTANCE_THRESHOLD = 50.0  # Above 70 distance -> Unrecognized user


def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)


# =====================================================================
# STEP 1: FAMILY DATASET CAPTURE ROUTINE (Con selección de cámara)
# =====================================================================
def capture_dataset(subject_id, total_samples=40, camera_index=0):
    ensure_directory(DATASET_DIR)
    cam = cv2.VideoCapture(camera_index)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    detector = cv2.CascadeClassifier(CASCADE_PATH)

    subject_name = SUBJECT_MAP.get(subject_id, 'Unknown')
    print(f"\n[PREP] Preparando captura para ID {subject_id}: {subject_name}")
    print("[INFO] Sienta a la persona frente a la cámara y presiona la tecla 's' en la ventana de video para comenzar.")

    # Fase de espera (pausa para sentarse y acomodarse)
    ready_to_capture = False
    while not ready_to_capture:
        ret, frame = cam.read()
        if not ret:
            break

        # Mostrar instrucciones en pantalla
        cv2.putText(frame, f"Siguiente: {subject_name}", (30, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.putText(frame, "Presiona 's' para COMENZAR a capturar", (30, 90),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        frame_resized = cv2.resize(frame, (1280, 720))
        cv2.imshow("Dataset Collection Routine", frame_resized)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):  # Presionar 's' para iniciar la captura de fotos
            ready_to_capture = True
        elif key == ord('q'):  # Salir si es necesario
            cam.release()
            cv2.destroyAllWindows()
            exit()

    count = 0
    print(f"[INFO] ¡Capturando fotos para {subject_name}! Mueve ligeramente la cabeza...")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("[ERROR] Failed to grab frame from webcam.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(100, 100))

        for (x, y, w, h) in faces:
            count += 1
            face_img = gray[y:y+h, x:x+w]
            file_path = os.path.join(DATASET_DIR, f"User.{subject_id}.{count}.jpg")
            cv2.imwrite(file_path, face_img)

            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
            cv2.putText(frame, f"Capturing: {count}/{total_samples}", (x, y-10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        frame_resized = cv2.resize(frame, (1280, 720))
        cv2.imshow("Dataset Collection Routine", frame_resized)

        if cv2.waitKey(100) & 0xFF == ord('q') or count >= total_samples:
            break

    cam.release()
    cv2.destroyAllWindows()
    print(f"[SUCCESS] Dataset capture finished. Saved {count} samples for ID {subject_id}.\n")


# =====================================================================
# STEP 2: LBPH MODEL TRAINING ROUTINE
# =====================================================================
def train_model():
    print("[INFO] Training LBPH Face Recognizer model on the family dataset...")
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier(CASCADE_PATH)

    image_paths = [os.path.join(DATASET_DIR, f) for f in os.listdir(DATASET_DIR) if f.endswith(".jpg")]
    face_samples = []
    ids = []

    for image_path in image_paths:
        gray_img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        subject_id = int(os.path.split(image_path)[-1].split(".")[1])

        faces = detector.detectMultiScale(gray_img)
        for (x, y, w, h) in faces:
            face_samples.append(gray_img[y:y+h, x:x+w])
            ids.append(subject_id)

    if len(face_samples) == 0:
        print("[ERROR] No face training samples found in dataset directory.")
        return False

    recognizer.train(face_samples, np.array(ids))
    recognizer.write(TRAINER_FILE)
    print(f"[SUCCESS] Model trained successfully on {len(np.unique(ids))} family members. Saved to {TRAINER_FILE}.\n")
    return True


# =====================================================================
# STEP 3: REAL-TIME WEBCAM RECOGNITION SYSTEM (Con selección de cámara)
# =====================================================================
def run_realtime_recognition(camera_index=0):
    if not os.path.exists(TRAINER_FILE):
        print("[ERROR] Trainer file not found. Please train the model first.")
        return

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer.read(TRAINER_FILE)
    detector = cv2.CascadeClassifier(CASCADE_PATH)

    cam = cv2.VideoCapture(camera_index)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
    print(f"[INFO] Starting local video feed using camera index {camera_index}. Press 'q' to quit application.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("[ERROR] Unable to capture video stream.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(120, 120)
        )

        for (x, y, w, h) in faces:
            subject_id, distance = recognizer.predict(gray[y:y+h, x:x+w])

            # Distance mapping to precision/confidence %
            # In LBPH: 0 distance = perfect match, >100 distance = high variation
            confidence_pct = max(0.0, min(100.0, 100.0 * (1.0 - (distance / 100.0))))

            # Classification threshold rule
            if distance < MAX_DISTANCE_THRESHOLD and subject_id in SUBJECT_MAP:
                name_label = SUBJECT_MAP[subject_id]
                display_text = f"{name_label} - {confidence_pct:.1f}%"
                box_color = (0, 200, 0)  # Green for registered family members
            else:
                display_text = "Usuario no reconocido"
                box_color = (0, 0, 220)  # Red for people outside the family database

            # Draw bounding box and text overlay
            cv2.rectangle(frame, (x, y), (x+w, y+h), box_color, 2)

            # Background rectangle for text contrast
            cv2.rectangle(frame, (x, y - 35), (x + w, y), box_color, cv2.FILLED)
            cv2.putText(frame, display_text, (x + 6, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 2)

        cv2.imshow("Local Face Identification System - UABC", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


# =====================================================================
# MAIN ENTRY POINT
# =====================================================================
if __name__ == "__main__":
    print("==================================================")
    print(" UABC COMPUTER VISION: FAMILY FACE RECOGNITION SETUP")
    print("==================================================")
    
    # Preguntar al usuario qué cámara desea utilizar
    try:
        cam_input = input("Ingresa el índice de la cámara a utilizar (Ej. 0 para cámara física, 1 para OBS Virtual Camera): ").strip()
        CAMERA_INDEX = int(cam_input) if cam_input != "" else 0
    except ValueError:
        CAMERA_INDEX = 0
        print("[AVISO] Entrada no válida. Usando cámara predeterminada (0).")

    print(f"[INFO] Usando dispositivo de video ID: {CAMERA_INDEX}")
    print("==================================================")

    # Direct execution of webcam stream (assuming trainer.yml exists)
    if not os.path.exists(TRAINER_FILE):
        print("[SETUP] Training model automatically from existing dataset...")
        if os.path.exists(DATASET_DIR) and len(os.listdir(DATASET_DIR)) > 0:
            train_model()
        else:
            print("[NOTICE] No dataset found. Running family capture for all 3 relatives...")
            capture_dataset(subject_id=1, total_samples=40, camera_index=CAMERA_INDEX)
            capture_dataset(subject_id=2, total_samples=40, camera_index=CAMERA_INDEX)
            capture_dataset(subject_id=3, total_samples=40, camera_index=CAMERA_INDEX)
            train_model()

    run_realtime_recognition(camera_index=CAMERA_INDEX)