import numpy as np
from math import log2


def theta(arr, b):
    w = b // 25
    c = np.zeros((5, w))

    for x in range(5):
        for z in range(w):
            c[x, z] = (int(arr[x, 0, z]) + int(arr[x, 1, z]) + int(arr[x, 2, z]) +
                       int(arr[x, 3, z]) + int(arr[x, 4, z])) % 2

    d = np.array(np.zeros((5, w)), dtype=bool)

    for x in range(5):
        for z in range(w):
            d[x, z] = c[(x - 1) % 5, z] != c[(x + 1) % 5, (z - 1) % w]

    res = np.array(np.zeros((5, 5, w)), dtype=bool)

    for y in range(5):
        for x in range(5):
            for z in range(w):
                res[x, y, z] = arr[x, y, z] != d[x, z]

    return res


def rho(arr, b):
    w = b // 25
    res = arr.copy()
    x, y = 1, 0

    for t in range(24):
        for z in range(w):
            res[x, y, z] = arr[x, y, (z - int((t + 1) * (t + 2) * 0.5)) % w]
        x, y = y, (2 * x + 3 * y) % 5

    return res


def pi(arr, b):
    w = b // 25
    res = np.array(np.zeros((5, 5, w)), dtype=bool)

    for y in range(5):
        for x in range(5):
            for z in range(w):
                res[x, y, z] = arr[(x + (3 * y)) % 5, x, z]

    return res


def chi(arr, b):
    w = b // 25
    res = np.array(np.zeros((5, 5, w)), dtype=bool)

    for y in range(5):
        for x in range(5):
            for z in range(w):
                res[x, y, z] = (arr[x, y, z] != ((not (arr[(x + 1) % 5, y, z])) and arr[(x + 2) % 5, y, z]))

    return res


def iota(arr, b, ir):
    def rc(t):
        if t % 255 == 0:
            return 1

        r = [1, 0, 0, 0, 0, 0, 0, 0]
        for i in range(1, (t % 255) + 1):
            r = [0] + r
            r[0] = int(r[0] != r[8])
            r[4] = int(r[4] != r[8])
            r[5] = int(r[5] != r[8])
            r[6] = int(r[6] != r[8])
            r = r[:8]

        return r[0]

    w = b // 25
    l = int(log2(w))
    res = arr.copy()
    rc_array = [0] * w

    for j in range(l + 1):
        rc_array[2 ** j - 1] = rc(j + 7 * ir)
    for z in range(w):
        res[0, 0, z] = res[0, 0, z] != rc_array[z]

    return res
