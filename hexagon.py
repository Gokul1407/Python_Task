import numpy as np
import matplotlib.pyplot as plt


def hexagon(radius, center):
    
    angle = np.linspace(0, 2 * np.pi, 7)
    x = center[0] + radius * np.cos(angle)
    y = center[1] + radius * np.sin(angle)
    return x, y


def plot_hexagonal_grid(rows, cols, hex_size=1.0):

    fig, ax = plt.subplots()
    for j in range(cols):
        if j % 2 == 0:
            num_hexagons = rows
        else:
            num_hexagons = rows - 1

        for i in range(num_hexagons):
            x_offset = 3 / 2 * hex_size * j
            y_offset = np.sqrt(3) * hex_size * (i + 0.5 * (j % 2))
            hex_x, hex_y = hexagon(hex_size, (x_offset, y_offset))
            ax.fill(hex_x, hex_y, edgecolor='k', linewidth=1, facecolor='none')

    ax.set_aspect('equal', 'box')
    ax.axis('off')
    plt.show()



rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))


plot_hexagonal_grid(rows, cols)
