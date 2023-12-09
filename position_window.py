import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_liquid_front(frame, last_location=None, window_width=50, intensity_threshold=3):
    # Convert to grayscale and blur the image
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (3, 3), 0)

    # Define the search window
    if last_location is not None:
        start = max(0, last_location - window_width)
        end = min(frame.shape[1], last_location + window_width)
        search_frame = blurred_frame[:, start:end]
    else:
        search_frame = blurred_frame

    # Median of each column to represent the column
    compressed_frame = np.median(search_frame, axis=0)

    # Find the sharpest change in intensity
    intensity_change = np.diff(compressed_frame)
    local_front_location = np.argmin(intensity_change)
    change_at_front = np.min(intensity_change)

    # Check if the detected front is strong enough
    if change_at_front > -intensity_threshold:
        return frame, None

    # Adjust location based on search window
    if last_location is not None:
        liquid_front_location = start + local_front_location
    else:
        liquid_front_location = local_front_location

    # Mark the liquid front location on the frame
    marked_frame = cv2.line(frame.copy(), (liquid_front_location, 0),
                            (liquid_front_location, frame.shape[0]), (255, 0, 0), 2)

    return marked_frame, liquid_front_location

def main(video_path):
    # Stores the liquid front location for each frame
    liquid_front_locations = []
    
    # Video capture
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    last_location = None  # Initialize last known location

    # Frame by frame analysis
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        marked_frame, location = analyze_liquid_front(frame, last_location)
        last_location = location  # Update last known location
        liquid_front_locations.append(location)
        cv2.imshow('Video Playback', marked_frame)

        # Exit on 'q' keypress
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()

    # Plot results
    plt.plot(liquid_front_locations)
    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Liquid Front X Location vs. Frame Number')
    plt.show()

if __name__ == "__main__":
    video_path = "media/DSC_0036_cropped2.avi"
    main(video_path)
