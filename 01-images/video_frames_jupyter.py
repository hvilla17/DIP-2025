# video_frames_jupyter.py
import cv2 as cv
import matplotlib.pyplot as plt
from IPython.display import clear_output

video_path = 'videos/Megamind.avi'
cap = cv.VideoCapture(video_path)

# Output folder for frames
output_folder = "frames"

frame_counter = 0  # Start frame numbering
filename_prefix = "frame"

if not cap.isOpened():
    print("Error: Could not open video.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("End of video stream or cannot fetch frame.")
            break

        # Convert to RGB for Matplotlib
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Display inline in Jupyter
        clear_output(wait=True)
        plt.imshow(frame_rgb)
        plt.axis('off')
        plt.show()

        # Save frame to file
        frame_filename = f"{output_folder}/{filename_prefix}-{frame_counter:04d}.png"
        cv.imwrite(frame_filename, frame)
        frame_counter += 1

cap.release()
print(f"Saved {frame_counter} frames in '{output_folder}' folder.")
