import matplotlib.pyplot as plt
import math
import numpy as np
import copy as c


def task4(matrix):
    paretoIndexes = np.ndarray(0, dtype = int);
    noParetoIndexes = np.ndarray(0, dtype = int);

    for i, checkingVec in enumerate(matrix):
        isPareto = True;
        for j, vec in enumerate(matrix):
            if j != i and not np.any(checkingVec > vec):
                isPareto = False;
                break;
        if isPareto:
            paretoIndexes = np.append(paretoIndexes, i);
        else:
            noParetoIndexes = np.append(noParetoIndexes, j);
    
    fig, axes = plt.subplots(ncols=2, subplot_kw=dict(polar=True))

    angle = 2 * np.pi * np.arange(0, 1 + 1 / matrix.shape[1], 1 / matrix.shape[1]);

   # matrix = np.append(matrix, matrix[:, 0], axis = 0);

    for i in paretoIndexes:
        axes[0].plot(angle, np.append(matrix[i], matrix[i, 0]));

    for i in noParetoIndexes:
        axes[1].plot(angle, np.append(matrix[i], matrix[i, 0]));
    plt.show();

def main():
    count = 5;
    dim = 4;
    task4(np.trunc(np.random.rand(count, dim) * 10));

if __name__ == "__main__":
   main();