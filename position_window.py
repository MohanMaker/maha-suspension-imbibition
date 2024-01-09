import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import csv
import os

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

    # Apply Savitzky-Golay filter to smooth the intensity profile
    smoothed_frame = savgol_filter(compressed_frame, 3, 2)  # window size 5, polynomial order 2

    # Find the sharpest change in intensity
    intensity_change = np.diff(smoothed_frame)
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
    liquid_front_locations = []
    frame_count = 0

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    last_location = None

    csv_filename = f"{os.path.splitext(os.path.basename(video_path))[0]}_data.csv"

    # Open CSV file to save data
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Frame Number', 'Liquid Front X Location'])

        while True:
            ret, frame = cap.read()
            if not ret:
                break

            # Analyze each frame
            marked_frame, location = analyze_liquid_front(frame, last_location)
            last_location = location
            liquid_front_locations.append(location)

            # Save data to CSV file
            writer.writerow([frame_count, location])
            frame_count += 1

            # Display the marked frame
            cv2.imshow('Video Playback', marked_frame)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                break

    cap.release()
    cv2.destroyAllWindows()

    # Plot the data
    plt.plot(liquid_front_locations)
    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Liquid Front X Location vs. Frame Number')
    plt.show()

if __name__ == "__main__":
    video_path = "media/DSC_0038_cropped3.avi"
    main(video_path)
