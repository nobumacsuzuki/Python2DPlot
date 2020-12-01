import matplotlib.pyplot as plt
import numpy as np

def main():
    csvFile = np.loadtxt('exampledata.csv', delimiter=',', skiprows=1)
    print(csvFile)
    x1 = csvFile[:,0]
    y1 = csvFile[:,1]
    y2 = csvFile[:,2]
    print(x1)
    print(y1)
    print(y2)

    plt.scatter(x1, y1)
    plt.scatter(x1, y2)

    x = np.linspace(0, np.pi * 2, 8)
    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.show()

if __name__ == "__main__":
    main()