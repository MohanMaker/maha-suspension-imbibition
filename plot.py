import matplotlib.pyplot as plt
import numpy as np
import csv

import matplotlib.pyplot as plt
import numpy as np
import csv

def read_csv_and_plot(csv_filename):
    # Read the CSV file
    liquid_front_locations = []
    frame_numbers = []
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader):
            liquid_front_locations.append(int(row[0]))
            frame_numbers.append(i)

    # Log-Log Plot
    plt.loglog(frame_numbers, liquid_front_locations, linestyle="None", marker='o', markersize=3, label='Data')
    
    y_equals_x = np.array(frame_numbers) * 5
    plt.loglog(frame_numbers, y_equals_x, label='y = x', linestyle='--', color='green')
    y_sqrt_x = np.sqrt(frame_numbers) * 40
    plt.loglog(frame_numbers, y_sqrt_x, label='y = sqrt(x)', linestyle='--', color='red', zorder=0)

    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Liquid Front X Location vs. Frame Number')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    csv_filename = "media/030724-glycerolsuspension-400umthintube2.csv"
    read_csv_and_plot(csv_filename)
