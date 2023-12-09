import cv2
import numpy as np
import matplotlib.pyplot as plt

def analyze_liquid_front(frame, last_position, window_size):
    # Define the window boundaries
    start_col = last_position
    end_col = min(frame.shape[1], last_position + window_size)

    # Crop the frame to the window
    cropped_frame = frame[:, start_col:end_col]

    # Existing processing steps
    gray_frame = cv2.cvtColor(cropped_frame, cv2.COLOR_BGR2GRAY)
    blurred_frame = cv2.GaussianBlur(gray_frame, (3, 3), 0)
    compressed_frame = np.median(blurred_frame, axis=0)
    intensity_change = np.diff(compressed_frame)
    local_liquid_front = np.argmin(intensity_change)

    # Calculate the global position of the liquid front
    global_liquid_front = start_col + local_liquid_front

    # Mark the liquid front location on the frame
    marked_frame = cv2.line(frame.copy(), (global_liquid_front, 0),
                            (global_liquid_front, frame.shape[0]), (255, 0, 0), 2)

    return marked_frame, global_liquid_front

def main(video_path):
    liquid_front_locations = []
    window_size = 50  # Adjust this based on your video
    last_position = 0  # Starting at the leftmost side

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        marked_frame, location = analyze_liquid_front(frame, last_position, window_size)
        last_position = location  # Update the last position
        liquid_front_locations.append(location)
        cv2.imshow('Video Playback', marked_frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    plt.plot(liquid_front_locations)
    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Liquid Front X Location vs. Frame Number')
    plt.show()

if __name__ == "__main__":
    video_path = "media/DSC_0036_cropped2.avi"
    main(video_path)
