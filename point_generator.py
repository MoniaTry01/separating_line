import numpy as np


def generate_points(n=50, seed=None, coord_range=10, margin=0.5):
    rng = np.random.default_rng(seed)
    true_a = rng.uniform(-2, 2)
    true_b = rng.uniform(-2, 2)

    points = []
    while len(points) < n:
        x = rng.uniform(-coord_range, coord_range)
        y = rng.uniform(-coord_range, coord_range)
        s = true_a * x + true_b * (1 + y)
        if abs(s) < margin:
            continue  # too close to the boundary, skip to keep classes cleanly separable
        label = 0 if s > 0 else 1
        points.append([x, y, label])

    return points


if __name__ == "__main__":
    for p in generate_points(n=10, seed=1):
        print(p)
