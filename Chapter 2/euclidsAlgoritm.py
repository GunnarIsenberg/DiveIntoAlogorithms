def gcd(x, y):
    # This line of code always setsup our variables and sorts them so the
    # algoritm can begin.
    larger = max(x, y)
    smaller = min(x, y)

    remainder = larger % smaller

    # if we get to zero we refrain from replacing whatever smaller happens to be
    if(remainder == 0):
        return smaller

    # If we have not yet achieved 0 we must continue to ensure we find the gcd
    # this means implimenting a recusive function in order to continue the same
    # operations all the way down.
    if(remainder != 0):
        return(gcd(smaller, remainder))
