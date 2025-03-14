import audio_processing
import video_processing
import analysis
import feedback
import gui

def main():
    print("Khởi động hệ thống...")
    
    # Xử lý âm thanh
    audio_data = audio_processing.process_audio("input_audio.wav")
    
    # Xử lý video
    video_data = video_processing.process_video("input_video.mp4")
    
    # Phân tích dữ liệu
    analysis_results = analysis.analyze(audio_data, video_data)
    
    # Sinh phản hồi từ kết quả phân tích
    response = feedback.generate_response(analysis_results)
    print("Phản hồi: ", response)
    
    # Khởi chạy giao diện đồ họa (nếu có)
    gui.run()

if __name__ == "__main__":
    main()
