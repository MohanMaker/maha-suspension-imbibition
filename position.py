import cv2
import numpy as np
import matplotlib.pyplot as plt 

# define an array of integers to hold the min x location of the vertical bar in every frame
min_x_locations = []
def analysis_darkest(frame):
    # Convert to grayscale
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Compress each column of pixels into one pixel by taking the median, which excludes outliers
    compressed_frame = np.median(frame_gray, axis=0)

    # Calculate the derivative of the compressed frame
    derivative = np.diff(compressed_frame)

    # Find the location of the largest spike in the derivative
    # We use np.argmin here because a spike (large negative change) indicates the presence of the front
    spike_locs = np.where(derivative == np.amin(derivative))[0]
    if spike_locs.size > 0:
        min_x_loc = spike_locs[0]  # Taking the first spike location
        min_x_locations.append(min_x_loc)
        # Draw a line at the position of the detected front
        frame_marked = cv2.line(frame.copy(), (min_x_loc, 0), (min_x_loc, frame.shape[0]), (255, 0, 0), 2)
    else:
        frame_marked = frame.copy()
        min_x_locations.append(np.nan)  # Append NaN to indicate no spike was found

    return frame_marked

# Open the video file.
video_path = "media/DSC_0038_cropped2.avi"
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

    # Use the analysis function that works with the darkest point
    # and extract only the image from the returned tuple for displaying
    marked_frame = analysis_darkest(frame)

    # Display the frame.
    cv2.imshow('Video Playback', marked_frame)

    # Wait for 25ms and check if the user pressed 'q' to exit.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows.
cap.release()
cv2.destroyAllWindows()