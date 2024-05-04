from step_mappings import *


def keccak_p(s, b, nr):
    w = b // 25
    l = int(log2(w))
    arr = np.array(np.zeros((5, 5, w)), dtype=bool)
    res = ""

    for y in range(5):
        for x in range(5):
            for z in range(w):
                arr[x, y, z] = bool(int(s[w * (5 * y + x) + z]))

    for ir in range(12 + 2 * l - nr, 12 + 2 * l):
        arr = iota(chi(pi(rho(theta(arr, b), b), b), b), b, ir)

    for y in range(5):
        for x in range(5):
            for z in range(w):
                res += str(int(arr[x, y, z]))

    return res


def xor_string(s1, s2):
    return "".join([str(int(s1[i] != s2[i])) for i in range(len(s1))])


def pad10_1(x, m):
    return "1" + "0" * ((-m - 2) % x) + "1"


def keccak_c(c, n_str, d):
    b = 1600
    r = b - c
    nr = 24

    p_str = n_str + pad10_1(r, len(n_str))
    n = len(p_str) // r

    s = '0' * b
    for i in range(n):
        s = keccak_p(xor_string(s, p_str[i * r:(i + 1) * r] + ('0' * c)), b, nr)

    z = s[:r]
    while len(z) < d:
        z += s[:r]
        s = keccak_p(s, b, nr)

    z = z[:d]
    res = ''
    for i in range(0, len(z), 8):
        bit_s2 = z[i:i+4]
        bit_s1 = z[i+4:i+8]
        s1 = hex(int(bit_s1[::-1], 2))[2:]
        s2 = hex(int(bit_s2[::-1], 2))[2:]
        res += s1 + s2

    return res


def sha3(bit_string, sha_type):
    if sha_type not in [224, 256, 384, 512]:
        return "wrong sha_type"
    return keccak_c(sha_type * 2, bit_string + '01', sha_type)


