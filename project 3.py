check = 600851475143

def checkprime(num):
    i = 2
    while i < (round(num / 2)):
        if num % i == 0:
            return False
            break
        else:
            i += 1
    if i == (round(num / 2)):
        return True


factors=[]
a = 0
b = 0
def factorit(num):
    n = 2
    while n < num:
        if num % n == 0:
            a = n
            b = num / n
            if checkprime(a):
                factors.append(a)
            else:
                factorit(a)
            if checkprime(b):
                factors.append(b)
            else:
                factorit(b)
            break
        else:
            n += 1

factorit(check)
factors.sort()
print(factors[len(factors)-1])
