import cv2

def display_frame(frame):
    """Display a single video frame."""
    cv2.imshow("AI Scouter", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        return False
    return True
