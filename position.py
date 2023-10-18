import cv2
import numpy as np
import matplotlib.pyplot as plt 

# define an array of integers to hold the min x location of the vertical bar in every frame
min_x_locations = []
def analysis(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (5, 5), 0)

    # Find the vertical bar with the minimum gray value in the frame
    avg_intensities = np.mean(frame, axis=0)
    min_x_loc = np.argmin(avg_intensities)
    marked_frame = cv2.line(frame.copy(), (min_x_loc, 0), (min_x_loc, frame.shape[0]), (0, 0, 255), 2)
    
    min_x_locations.append(min_x_loc)

    return marked_frame

# Open the video file.
video_path = "output_cropped.avi"
cap = cv2.VideoCapture(video_path)

# Check if the video file was opened successfully.
if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

while True:
    # Read a frame from the video.
    ret, frame = cap.read()

    # If 'ret' is False, it means the video has ended.
    if not ret:
        print(min_x_locations)
    
        # plot the min x locations over time
        x = np.arange(len(min_x_locations))
        min_x = np.array(min_x_locations)
        plt.plot(x, min_x)
        plt.xlabel('Frame Number')
        plt.ylabel('Min Grayscale X Location')
        plt.title('Min Grayscale X Location vs. Frame Number')
        plt.show()

        break

    marked_frame = analysis(frame)

    # Display the frame.
    cv2.imshow('Video Playback', marked_frame)

    # Wait for 25ms and check if the user pressed 'q' to exit.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows.
cap.release()
cv2.destroyAllWindows()