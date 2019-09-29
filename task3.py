import numpy as np
import math

def get_indices(length, n_batches, split_ratio): #split_ratio = (0, 1)
    lenSector = length / (split_ratio * n_batches + 1 - split_ratio);

    train = np.zeros((n_batches, 2));
    check = np.zeros((n_batches, 2));
    trainLen = math.floor(lenSector * split_ratio);
    checkLen = round(lenSector * (1 - split_ratio));

    for i in range(0, n_batches):
        train[i][0] = i * trainLen;
        train[i][1] = (i + 1) * trainLen - 1;
        check[i][0] = train[i][1] + 1;
        check[i][1] = train[i][1] + checkLen;
    return [trainLen, checkLen];

def main():
    for inds in get_indices(100, 5, 0.25):
        print(inds)
    # expected result:
    # [0, 44, 55]
    # [11, 55, 66]
    # [22, 66, 77]
    # [33, 77, 88]
    # [44, 88, 99]

if __name__ == "__main__":
    main()