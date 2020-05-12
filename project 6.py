def sumofsqaures(maxx):
    a=0
    for i in range(maxx + 1):
        a+=i**2
    return(a)

def squareofsum(maxx):
    a=0
    for i in range(maxx + 1):
        a+=i
    return(a**2)



print(squareofsum(100) - sumofsqaures(100))