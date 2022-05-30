from insertion import insert_cabinet


cabinet = [8, 4, 6, 1, 2, 5, 3, 7]


def insertionSort(cabinet):
    newCabinet = []

    while len(cabinet) > 0:
        toInsert = cabinet.pop(0)
        newCabinet = insert_cabinet(newCabinet, toInsert)
    return(newCabinet)

# 12 appears in the first cabinet when the script is run
# This is beacuse the first cabinet item is from insertion.py - not this script
# and it can be ignored.


sortedCabinet = insertionSort(cabinet)
print(sortedCabinet)
print(cabinet)
