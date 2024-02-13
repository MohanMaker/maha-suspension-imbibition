import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import csv
import os

def analyze_liquid_front(frame, last_location):
    # Convert to grayscale and blur the image
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.GaussianBlur(frame, (3, 3), 0)

    # Define the search window
    frame = frame[:, last_location:last_location+100]

    # Median of each column to represent the column
    frame = np.median(frame, axis=0)

    # Apply Savitzky-Golay filter to smooth the intensity profile
    if len(frame) >= 5:
        frame = savgol_filter(frame, 5, 2) # window length 5, polynomial order 2

    # Find the sharpest change in intensity
    intensity_change = np.diff(frame)
    location = np.argmin(intensity_change)

    return last_location + location

def main(video_path):
    liquid_front_locations = []
    last_location = 0

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Analyze the frame, update the last location, and save the data
        last_location = analyze_liquid_front(frame, last_location)
        liquid_front_locations.append(last_location)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Write data to CSV
    csv_filename = f"{os.path.splitext(os.path.basename(video_path))[0]}.csv"
    with open(csv_filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Liquid Front X Location'])
        for location in liquid_front_locations:
            writer.writerow([location])

        # Assuming liquid_front_locations is already defined
    # For demonstration, let's create a hypothetical range of frame numbers
    frame_numbers = np.arange(1, len(liquid_front_locations) + 1)

    # Plot the liquid front location vs. frame number in log-log scale
    plt.loglog(frame_numbers, liquid_front_locations, label='Liquid Front Location', marker='o', linestyle='-', markersize=4)

    # Plot y=x by using the same values for x and y
    plt.loglog(frame_numbers, frame_numbers, label='y=x', linestyle='--')

    # Correctly plot y=x^1/2
    # Calculate y=x^1/2 for the range of frame numbers
    y_sqrt_x = np.sqrt(frame_numbers)
    plt.loglog(frame_numbers, y_sqrt_x, label='y=x^1/2', linestyle=':')

    # Adjusting the plot
    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Log-Log Plot of Liquid Front X Location vs. Frame Number')
    plt.legend()

    plt.show()

if __name__ == "__main__":
    video_path = "media/020624_cropped.avi"
    main(video_path)
