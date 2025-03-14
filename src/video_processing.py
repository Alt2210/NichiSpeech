import cv2
import time

temp_video = "temp_video.avi"

def capture_video(duration=5, fps=10):
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Cannot open camera")
        return []

    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(temp_video, fourcc, fps, (800, 600))
    frames = []
    start_time = time.time()

    while time.time() - start_time < duration:
        ret, frame = cap.read()
        if ret:
            frame = cv2.resize(frame, (800, 600))
            out.write(frame)
            frames.append(frame)
        cv2.waitKey(int(1000 / fps))

    cap.release()
    out.release()
    return frames
