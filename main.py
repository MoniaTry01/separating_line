import numpy as np
from point_generator import generate_points
from plot import plot_points

in_a = 1.0
in_b = 1.0
lr = 0.01


def update_parameters(a, b, p, point):
    target = 0
    if point[2] == 0: target = 1
    a = a - lr * (p - target) * point[0]
    b = b - lr * (p - target) * (1 + point[1])
    return a, b


def adjust_parameters(a, b, points):
    p_arr = []
    for i in range(0, len(points)):
        s = a * points[i][0] + b + b * points[i][1]
        p = sigmoid(s)
        p_arr.append(p)
        #L = -[points[i][2] * np.log(p) + (1-points[i][2]) * np.log(1-p)]
        a, b = update_parameters(a, b, p, points[i])
    return a, b, p_arr
    

def calculate_line(a, b, points):
    while(True):
        a, b, p_arr = adjust_parameters(a, b, points)
        if accuracy_check(p_arr, points) > 0.99:
            break
    return a, b


def sigmoid(s):
    return 1 / (1 + np.exp(-s))


def accuracy_check(p_arr, points):
    score = 0
    for i in range(0, len(points)):
        if (points[i][2] == 0 and p_arr[i] >= 0.5) or (points[i][2] == 1 and p_arr[i] < 0.5):
            score = score + 1
    return score / len(points)


def main():
    points = generate_points(n=300)
    final_a, final_b = calculate_line(in_a, in_b, points)
    plot_points(points, 0, -1, -final_a/final_b)


if __name__ == '__main__':
    main()