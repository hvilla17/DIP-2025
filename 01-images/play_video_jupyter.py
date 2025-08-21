# play_video_jupyter.py
import cv2 as cv
import matplotlib.pyplot as plt
from IPython.display import clear_output

video_path = 'vvideos/Megamind.avi4'
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    cap.release()
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream or cannot fetch frame.")
            break

        # Convert BGR (OpenCV) to RGB (Matplotlib)
        frame_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)

        # Clear previous output and display next frame
        clear_output(wait=True)
        plt.imshow(frame_rgb)
        plt.axis('off')
        plt.show()

cap.release()
