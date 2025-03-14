import whisper
import os
import cv2

def analyze_speech(audio_path):
    if not os.path.exists(audio_path):
        return "Không thể phân tích giọng nói.", 0

    model = whisper.load_model("base")
    result = model.transcribe(audio_path)
    text = result["text"]
    speed = len(text.split()) / (whisper.load_audio(audio_path).shape[0] / 16000) * 60
    return text, speed

def analyze_image(frames):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    eye_contact_count = 0

    for frame in frames:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        if len(faces) > 0:
            eye_contact_count += 1

    eye_contact_percentage = (eye_contact_count / len(frames)) * 100 if frames else 0
    return eye_contact_percentage, "neutral"
