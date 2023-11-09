import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_liquid_front(frame):
    # Convert to grayscale and blur the image
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (3, 3), 0)

    # Median of each column to represent the column
    compressed_frame = np.median(blurred_frame, axis=0)

    # Find the sharpest change in intensity
    intensity_change = np.diff(compressed_frame)
    liquid_front_location = np.argmin(intensity_change)

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

    # Frame by frame analysis
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        marked_frame, location = analyze_liquid_front(frame)
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
