# play_video.py
import cv2 as cv

# Open video file or webcam (0 = default webcam)
video_path = "../videos/Megamind.avi"
cap = cv.VideoCapture(video_path)

frame_width = cap.get(cv.CAP_PROP_FRAME_WIDTH)
frame_height = cap.get(cv.CAP_PROP_FRAME_HEIGHT)
fps = cap.get(cv.CAP_PROP_FPS)
print('width: ', frame_width, ', height: ', frame_height, ', fps: ', fps)

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    ret, frame = cap.read()  # Read a frame
    if not ret:
        print("End of video stream or cannot fetch frame.")
        break

    cv.imshow("Video Playback", frame)  # Display frame

    # Exit when 'q' is pressed
    if cv.waitKey(int (1000 / fps)) & 0xFF == ord('q'):
        break

cap.release()           # Release the video capture object
cv.destroyAllWindows()  # Close all OpenCV windows
