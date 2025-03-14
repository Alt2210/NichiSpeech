from tkinter import Tk, Label, Button, Frame, Text, Scrollbar, StringVar
from audio_processing import record_audio
from video_processing import capture_video
from analysis import analyze_speech, analyze_image
from feedback import generate_feedback

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Hệ thống cải thiện kỹ năng thuyết trình")
        self.root.geometry("800x600")

        self.result_text = Text(root, height=10, width=90)
        self.result_text.pack()

        self.start_button = Button(root, text="Bắt đầu", command=self.start_analysis)
        self.start_button.pack()

    def start_analysis(self):
        audio_path = record_audio(5)
        frames = capture_video(5)

        if audio_path:
            speech_text, speech_speed = analyze_speech(audio_path)
            eye_contact, emotion = analyze_image(frames)
            feedback = generate_feedback(speech_speed, eye_contact, emotion)
            self.result_text.insert("1.0", feedback)

if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()
