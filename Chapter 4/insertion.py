
def insert_cabinet(cabinet, toInsert):
    checkLocation = len(cabinet) - 1
    insertLocation = 0
    while(checkLocation >= 0):
        if toInsert > cabinet[checkLocation]:
            insertLocation = checkLocation + 1
            checkLocation = - 1
        checkLocation = checkLocation - 1
    cabinet.insert(insertLocation, toInsert)
    return(cabinet)


cabinet = [1, 2, 3, 3, 4, 6, 8, 12]
newcabinet = insert_cabinet(cabinet, 5)
print(newcabinet)
