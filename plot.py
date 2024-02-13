import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import csv
import os

import matplotlib.pyplot as plt
import csv

def read_csv_and_plot(csv_filename):
    liquid_front_locations = []
    
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            liquid_front_locations.append(int(row[0]))
    
    # Plot the data
    plt.plot(liquid_front_locations)
    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Liquid Front X Location vs. Frame Number')
    plt.show()

    # Plot the log-log data
    # Create range of frame numbers
    frame_numbers = np.arange(1, len(liquid_front_locations) + 1)

    # Plot the liquid front location vs. frame number in log-log scale
    plt.loglog(frame_numbers, liquid_front_locations, label='Liquid Front Location', marker='o', linestyle='-', markersize=2)

    # Plot y=x
    y_equals_x = frame_numbers * 80
    plt.loglog(frame_numbers, y_equals_x, label='y=x', linestyle='--')

    # Plot y=x^1/2
    y_sqrt_x = np.sqrt(frame_numbers) * 250
    plt.loglog(frame_numbers, y_sqrt_x, label='y=x^1/2', linestyle=':')

    # Add labels
    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Log-Log Plot of Liquid Front X Location vs. Frame Number')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    csv_filename = "media/021324-glycerol.csv"
    read_csv_and_plot(csv_filename)
