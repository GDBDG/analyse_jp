import matplotlib.pyplot as plt
import numpy as np


def generate_circles(nb_circles, cancerous_rate, r1, r2):
    fig, ax = plt.subplots()
    circles = np.random.choice([r1, r2], size=nb_circles, p=[cancerous_rate, 1 - cancerous_rate])

    for r in circles:
        x, y = np.random.uniform(-10, 10), np.random.uniform(-10, 10)
        circle = plt.Circle((x, y), radius=r, fc='blue' if r == r1 else 'red', alpha=0.5)
        ax.add_patch(circle)
    ax.axis('off')
    ax.set_aspect('equal')
    ax.set_xlim([-10, 10])
    ax.set_ylim([-10, 10])
    ax.set_title(f"Nb circles : {nb_circles}, nb cancerous : {nb_circles * cancerous_rate}")
    plt.savefig('circles.png')
    plt.show()


# Example usage
if __name__ == '__main__':

    generate_circles(nb_circles=2000, cancerous_rate=0.3, r1=0.3, r2=0.1)
