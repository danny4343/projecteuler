

def fact(n):
    total = 1
    for i in range(1,n+1):
        total*=i
    return(total)


def digits(n):
    mst = str(n)
    total = 0
    for x in range(len(mst)):
        total+=int(mst[x])
    return(total)

print(digits(fact(100)))








