import numpy as np
import matplotlib.pyplot as plt

def test(abc):
    print(abc)
    
def Target(azimuth, elevation):
    # Define radii for the concentric circles
    radii = [1, 2, 3, 4]

    # Define the labels for each circle
    labels = ['67.5°', '45°', '22.5°', '0°']

    # Create a figure and axis
    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')  # Set figure background color to black
    ax.set_facecolor('black')  # Set axis background color to black

    # Get x at each selected time
    if azimuth >= 0:
        x = 4 - (4/90) * azimuth
    elif azimuth < 0:
        x = -4 - (4/90) * azimuth
    else:
        print("Error: Azimuth Out of Bounds")

    # Get y at each selected time
    if elevation >= 0:
        y = 4 - (4/90) * elevation
    elif elevation < 0:
        y = -4 - (4/90) * elevation
    else:
        print("Error: Elevation Out of Bounds")

    # Adding Indicator dot
    indicator = plt.Circle((x,y), 0.15, color='green', zorder=10)
    ax.add_patch(indicator)

    # Draw concentric circles
    for radius in radii:
        circle = plt.Circle((0, 0), radius, fill=False, edgecolor='red')
        ax.add_patch(circle)

    # Draw red lines to split the circles into eight equal parts
    for angle in range(0, 360, 45):  # 0, 45, 90, ..., 315 degrees
        x = np.cos(np.radians(angle)) * radii[-1]
        y = np.sin(np.radians(angle)) * radii[-1]
        ax.plot([0, x], [0, y], color='red', alpha=0.5, linestyle=":")

    # Set the aspect of the plot to be equal, so circles are not distorted
    ax.set_aspect('equal', 'box')

    # Set the limits of the plot
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    # Remove the axis labels and ticks
    ax.axis('off')

    # Adding labels just below the rings
    for radius, label in zip(radii, labels):
        ax.text(0, -radius - 0.1, label, horizontalalignment='center', verticalalignment='top', color='white')
    plt.show()