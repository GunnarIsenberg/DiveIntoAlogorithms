import math
import random


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


def rule1(x, n, upright):
    return((x + ((-1)**upright) * n) % n**2)


def rule2(x, n, upleft):
    return((x + ((-1)**upleft * (-n + 1))) % n**2)


def rule3(x, n, upleft):
    return((x + ((-1)**upleft * (-n + 1))) % n**2)


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

center_i = math.floor(n/2)
center_j = math.floor(n/2)

entry_i = center_i
entry_j = center_j
where_we_can_go = ['up_left', 'up_right', 'down_left', 'down_right']
where_to_go = random.choice(where_we_can_go)

if(where_to_go == 'up_right'):
    new_entry_i = entry_i - 1
    new_entry_j = entry_j + 1
    square[new_entry_i][new_entry_j] = rule1(square[entry_i][entry_j], n, True)

if(where_to_go == 'down_left'):
    new_entry_i = entry_i + 1
    new_entry_j = entry_j - 1
    square[new_entry_i][new_entry_j] = rule1(
        square[entry_i][entry_j], n, False)

if(where_to_go == 'up_left'):
    new_entry_i = entry_i - 1
    new_entry_j = entry_j - 1
    square[new_entry_i][new_entry_j] = rule2(square[entry_i][entry_j], n, True)

if(where_to_go == 'down_right'):
    new_entry_i = entry_i + 1
    new_entry_j = entry_j + 1
    square[new_entry_i][new_entry_j] = rule2(
        square[entry_i][entry_j], n, False)

if(where_to_go == 'up_left' and (entry_i + entry_j) == (n)):
    new_entry_i = entry_i - 1
    new_entry_j = entry_j - 1
    square[new_entry_i][new_entry_j] = rule3(square[entry_i][entry_j], n, True)
if(where_to_go == 'down_right' and (entry_i + entry_j) == (n-2)):
    new_entry_i = entry_i + 1
    new_entry_j = entry_j + 1
    square[new_entry_i][new_entry_j] = rule3(
        square[entry_i][entry_j], n, False)

where_we_can_go = []
if(entry_i < (n - 1) and entry_j < (n - 1)):
    where_we_can_go.append('down_right')
if(entry_i < (n - 1) and entry_j > 0):
    where_we_can_go.append('down_left')
if(entry_i > 0 and entry_j < (n - 1)):
    where_we_can_go.append('up_right')
if(entry_i > 0 and entry_j > 0):
    where_we_can_go.append('up_left')
