import matplotlib.pyplot as plt
import numpy as np
import csv

import matplotlib.pyplot as plt
import numpy as np
import csv

def read_csv_and_plot(csv_filename):
    liquid_front_locations = []
    frame_numbers = []
    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for i, row in enumerate(reader):
            liquid_front_locations.append(int(row[0]))
            frame_numbers.append(i+1)

    # Regular Plot
    plt.plot(frame_numbers, liquid_front_locations, linestyle="None", marker='o', markersize=3)
    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Liquid Front X Location vs. Frame Number')
    plt.show()

    # Log-Log Plot
    plt.loglog(frame_numbers, liquid_front_locations, linestyle="None", marker='o', markersize=3, label='Data')

    y_equals_x = np.array(frame_numbers) * 80
    plt.loglog(frame_numbers, y_equals_x, label='y = x', linestyle='--', color='green')
    y_sqrt_x = np.sqrt(frame_numbers) * 120
    plt.loglog(frame_numbers, y_sqrt_x, label='y = sqrt(x)', linestyle='--', color='red', zorder=0)

    plt.xlabel('Frame Number')
    plt.ylabel('Liquid Front X Location')
    plt.title('Log-Log Plot with Overlays: Liquid Front X Location vs. Frame Number')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    csv_filename = "media/022024-suspension40um.csv"
    read_csv_and_plot(csv_filename)
