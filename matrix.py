import sys


def diagonalDifference(a):
    l = sum(matrix[i][i] for i in range(N))
    r = sum(matrix[i][N-i-1] for i in range(N))
    return abs(l - r)
if __name__ == "__main__":
    n = int(input().strip())
    a = []
    for a_i in range(n):
        a_t = [int(a_temp) for a_temp in input().strip().split(' ')]
        a.append(a_t)
    result = diagonalDifference(a)
    print(result)