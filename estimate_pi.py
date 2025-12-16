import numpy as np

def estimate_pi(num_samples):
    darts = 0

    for i in range(num_samples):
        x = np.random.rand()
        y = np.random.rand()
        distance = (x*x + y*y)** 0.5

        if distance < 1:
            darts += 1

    pi_estimate = 4 * (darts / num_samples)

    return pi_estimate


print(estimate_pi(1000))