# video_frames.py
import cv2 as cv


# Video source
video_path = '../videos/Liverpool.mp4'
cap = cv.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

fps = cap.get(cv.CAP_PROP_FPS)
print('FPS: ', fps)

output_folder = "frames"   # Output folder to store frames
filename_prefix = "frame"  # Base name for saved images

frame_counter = 0

while True:
    ret, frame = cap.read()
    if not ret:
        print("End of video stream or cannot fetch frame.")
        break

    # Display the current frame
    cv.imshow("Video Playback", frame)

    # Save the frame to a file with consecutive numbering
    frame_filename = f"{output_folder}/{filename_prefix}-{frame_counter:04d}.png"
    cv.imwrite(frame_filename, frame)
    frame_counter += 1

    # Press 'q' to stop early
    if cv.waitKey(int(1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

print(f"Saved {frame_counter} frames in '{output_folder}' folder.")
