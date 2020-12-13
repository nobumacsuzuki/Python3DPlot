import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
# for surface plot
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def _3dplot1():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    x = [1,2,3,4,5]
    y = [2,4,6,8,10]
    z = np.linspace(0,100,11)
    Y,Z = np.meshgrid(y,z)
    X = np.array([x]*Y.shape[0])

    ax.plot_surface(X, Y, Z)
    plt.show()

def _3dplotLine():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
    z = np.linspace(-2, 2, 100)
    r = z**2 + 1
    x = r * np.sin(theta)
    y = r * np.cos(theta)
    ax.plot(x, y, z)
    ax.legend()

    plt.show()

def randrange(n, vmin, vmax):
    return (vmax - vmin)*np.random.rand(n) + vmin


def _3dplotScatter():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    n = 100
    for c, m, zlow, zhigh in [('r', 'o', -50, -25), ('b', '^', -30, -5)]:
        xs = randrange(n, 23, 32)
        ys = randrange(n, 0, 100)
        zs = randrange(n, zlow, zhigh)
        ax.scatter(xs, ys, zs, c=c, marker=m)
    plt.show()

def _3dplotSurface():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)

    surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                        linewidth=0, antialiased=False)

    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)

    plt.show()

def main():
    _3dplotSurface()

if __name__ == "__main__":
    main()