import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt

def main():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    # theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    # z = np.linspace(-2, 2, 100)
    # r = z**2 + 1
    # x = r * np.sin(theta)
    # y = r * np.cos(theta)

    x = [1,2,3,4,5]
    y = [2,4,6,8,10]
    z = np.linspace(0,100,11)
    Y,Z = np.meshgrid(y,z)
    X = np.array([x]*Y.shape[0])

    ax.plot_surface(X, Y, Z)
    plt.show()

if __name__ == "__main__":
    main()