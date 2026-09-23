import matplotlib.pyplot as plt
import numpy as np

def plot_points(points, x0, y0, a):
    n = len(points)
    xp = np.zeros(n)
    yp = np.zeros(n)
    cp = np.zeros(n)

    for i in range(0, n):
        xp[i] = points[i][0]
        yp[i] = points[i][1]
        cp[i] = points[i][2]

    colors = ['red' if p[2] == 0 else 'blue' for p in points]
    plt.scatter([p[0] for p in points], [p[1] for p in points], c=colors)
    plt.axline((x0, y0), slope=a)
    plt.grid()
    #plt.plot(xp, yp, 'o')
    plt.show()