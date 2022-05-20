import math


def verifysquare(square):
    sums = []

    rowsums = [sum(square[i]) for i in range(0, len(square))]
    sums.append(rowsums)
    colsums = [sum([row[i] for row in square]) for i in range(0, len(square))]
    sums.appen(colsums)
    maindiag = sum([square[i][i] for i in range(0, len(square))])
    sums.append([maindiag])
    antidiag = sum([square[i][len(square) - 1 - i] for i in
                    range(0, len(square))])
    sums.append([antidiag])
    flattened = [j for i in sums for j in i]
    return(len(list(set(flattened))) == 1)


def printsquare(square):
    labels = ['['+str(x)+']' for x in range(0, len(square))]
    format_row = "{:>6}" * (len(labels) + 1)
    print(format_row.format("", *labels))
    for label, row in zip(labels, square):
        print(format_row.format(label, *row))


def rule1(x, n):
    return(((x + n) % n**2))


# This piece defines the size of the sqare we want to make
# and then creates a matrix with the corresponding rows & cols
# filled with the float NAN
n = 7
square = [[float('nan') for i in range(0, n) for j in range(0, n)]]

center_i = math.floor(n/2)
center_j = math.floor(n/2)

square[center_i][center_j] = int((n**2 + 1)/2)
square[center_i + 1][center_j] = 1
square[center_i - 1][center_j] = n**2
square[center_i][center_j + 1] = n**2 + 1 - n
square[center_i][center_j - 1] = n
