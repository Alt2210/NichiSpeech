# NichiSpeech - Presentation Skills Improvement System
## Features
- Audio Recording: Captures audio during a presentation and analyzes speech patterns.

- Video Recording: Records video to analyze eye contact and facial expressions.

- Speech Analysis: Transcribes speech and calculates speaking speed (words per minute).

- Visual Analysis: Detects eye contact percentage and dominant emotion (happy, neutral, sad).

- Feedback Generation: Provides detailed feedback on presentation skills, including suggestions for improvement.

- Interactive GUI: Built with Tkinter, offering a user-friendly interface for recording, analyzing, and reviewing presentations.
## Setting

### You can install the required libraries using the following command:
```
pip install -r requirements.txt

```

### Additionally, you need to install the whisper model:

```
pip install git+https://github.com/openai/whisper.git
```
### You also need to install the ffmpeg for voice and video

[Click here to download FFmpeg](https://github.com/BtbN/FFmpeg-Builds/releases/download/latest/ffmpeg-master-latest-win64-gpl.zip)

- After download successfully, you need to add the path of folder ```bin``` of ffmpeg to the ```PATH``` of the Environment Variables

- Then, Open the cmd to check for ffmpeg by the command

```
ffmpeg
```
## How to use

### Clone this repo

```
git clone https://github.com/Alt2210/NichiSpeech.git
cd NichiSpeech

```

### Run the application

```
python main.py
```
### Using the Application:

- Start Recording: Click the "Bắt đầu" button to start recording your presentation.

- Pause/Resume: Use the "Tạm dừng" button to pause and resume recording.

- Stop Recording: Click the "Dừng" button to stop recording and begin analysis.

- View Results: After analysis, the application will display feedback on your presentation skills, including speaking speed, eye contact, and emotional expression.

- Replay Recording: Use the "Xem lại" button to replay your recorded presentation.


