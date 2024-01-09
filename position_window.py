import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import csv
import os

def analyze_liquid_front(frame, last_location=0, intensity_threshold=3):
    # Convert to grayscale and blur the image
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (3, 3), 0)

    # Define the search window starting from the last found liquid front location
    search_frame = blurred_frame[:, last_location:]

    # Median of each column to represent the column
    compressed_frame = np.median(search_frame, axis=0)

    # Apply Savitzky-Golay filter to smooth the intensity profile
    smoothed_frame = savgol_filter(compressed_frame, 3, 2) # window size 3, polynomial order 2

    # Find the sharpest change in intensity
    intensity_change = np.diff(smoothed_frame)
    local_front_location = np.argmin(intensity_change)
    change_at_front = np.min(intensity_change)

    # Check if the detected front is strong enough
    if change_at_front > -intensity_threshold:
        return frame, None

    # Adjust location based on search window
    liquid_front_location = last_location + local_front_location

    # Mark the liquid front location on the frame
    marked_frame = cv2.line(frame.copy(), (liquid_front_location, 0),
                            (liquid_front_location, frame.shape[0]), (255, 0, 0), 2)

    return marked_frame, liquid_front_location

def main(video_path):
    liquid_front_locations = []
    frame_count = 0
    last_location = 0

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Analyze the frame
        marked_frame, location = analyze_liquid_front(frame, last_location)

        # Update last location if a new location was found
        if location is not None:
            last_location = location

        liquid_front_locations.append((frame_count, location))
        
        frame_count += 1

        # Display the marked frame
        cv2.imshow('Video Playback', marked_frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Write data to CSV
    csv_filename = f"{os.path.splitext(os.path.basename(video_path))[0]}_data.csv"
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Frame Number', 'Liquid Front X Location'])
        for frame_number, location in liquid_front_locations:
            writer.writerow([frame_number, location])

    # Plot the data
    frame_numbers, locations = zip(*liquid_front_locations)
    plt.plot(frame_numbers, locations)
    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Liquid Front X Location vs. Frame Number')
    plt.show()

if __name__ == "__main__":
    video_path = "media/DSC_0036_cropped3.avi"
    main(video_path)
