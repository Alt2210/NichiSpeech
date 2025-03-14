def generate_feedback(speed, eye_contact, emotion):
    feedback = "Phân tích kỹ năng thuyết trình:\n\n"
    
    if speed < 100:
        feedback += f"- Tốc độ nói: Chậm ({speed} từ/phút). Cố gắng tăng tốc độ lên 120-150 từ/phút.\n"
    elif speed > 160:
        feedback += f"- Tốc độ nói: Nhanh ({speed} từ/phút). Hãy nói chậm lại.\n"
    else:
        feedback += f"- Tốc độ nói: Tốt ({speed} từ/phút).\n"

    if eye_contact < 30:
        feedback += f"- Giao tiếp mắt: Kém ({eye_contact}%). Nhìn thẳng vào máy quay nhiều hơn.\n"
    elif eye_contact < 70:
        feedback += f"- Giao tiếp mắt: Trung bình ({eye_contact}%). Cần duy trì ánh nhìn với người nghe.\n"
    else:
        feedback += f"- Giao tiếp mắt: Tốt ({eye_contact}%).\n"

    if emotion == "neutral":
        feedback += "- Cảm xúc: Trung tính. Thử biểu cảm hơn để thu hút người nghe.\n"
    else:
        feedback += f"- Cảm xúc: {emotion}.\n"
    
    return feedback
