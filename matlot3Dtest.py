import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
# for surface plot
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter

def _3dplotLine():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    t = np.linspace(0, 10, 101)
    x = t
    y = t
    z = -t
    ax.plot(x, y, z)
    plt.show()
def _3dplotScatter():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    csvFile = np.loadtxt('exampledata.csv', delimiter=',', skiprows=1)
    NumberOfRow = csvFile.shape[0]
    rowRange = range (NumberOfRow)
    for indexRow in rowRange:
        [xs,ys,zs] = csvFile[indexRow]
        print([xs,ys,zs])
        ax.scatter(xs, ys, zs, c = 'y')
    plt.show()

def _3dplotSurface():
    fig = plt.figure()
    ax = fig.gca(projection='3d')

    X = np.arange(0, 2, 1)
    Y = np.arange(0, 2, 1)
    X, Y = np.meshgrid(X, Y)
    Z = -X -Y
    print(X)
    print(Y)
    print(Z)

    ax.plot_surface(X, Y, Z)
    plt.show()

def main():
    _3dplotLine()
    _3dplotScatter()
    _3dplotSurface()

if __name__ == "__main__":
    main()