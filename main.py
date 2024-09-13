import cv2
import numpy as np

def draw_parking_lines(frame):
    height, width, _ = frame.shape
    overlay = frame.copy()
    
    # Define the positions for the inverted red lines
    line_thickness = 5
    start_point1 = (int(width * 0.4), height)
    end_point1 = (int(width * 0.3), int(height * 0.5))
    
    start_point2 = (int(width * 0.6), height)
    end_point2 = (int(width * 0.7), int(height * 0.5))
    
    # Draw red inverted lines
    cv2.line(overlay, start_point1, end_point1, (0, 0, 255), line_thickness)
    cv2.line(overlay, start_point2, end_point2, (0, 0, 255), line_thickness)
    
    # Draw horizontal lines to indicate distance
    cv2.line(overlay, (int(width * 0.2), int(height * 0.8)), (int(width * 0.8), int(height * 0.8)), (0, 255, 0), 2)
    cv2.line(overlay, (int(width * 0.2), int(height * 0.6)), (int(width * 0.8), int(height * 0.6)), (0, 255, 0), 2)
    cv2.line(overlay, (int(width * 0.2), int(height * 0.4)), (int(width * 0.8), int(height * 0.4)), (0, 255, 0), 2)
    
    # Blend the overlay with the original frame using transparency
    alpha = 0.5  # Transparency factor
    cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0, frame)

    return frame

def open_camera():
    cap = cv2.VideoCapture(0)  # Open the default camera (FaceTime HD Camera)
    
    if not cap.isOpened():
        print("Cannot open camera")
        return
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break

        frame = draw_parking_lines(frame)  # Draw the parking lines on the frame

        cv2.imshow('CameraDisplay', frame)  # Display the frame with the lines
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    open_camera()
