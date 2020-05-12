def checkprime(num):
    if num == 2:
        return True
    i = 2
    while i < (round(num / 2)):
        if num % i == 0:
            return False
            break
        else:
            i += 1
    if num == 4:
        return False
    if num == 3:
        return True
    if i == (round(num / 2)):
        return True


factors=[]
a = 0
b = 0
def factorit(num):
    n = 2
    while n <= num:
        if num % n == 0:
            a = int(n)
            b = int(num / n)
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

for x in range(1, 21):
    factorit(x)

mydict = {}


def main(mlist):
    for x in range(len(mlist) - 2):
        n = 1
        while mlist[x+n] == mlist[x]:
            n+=1
            if mlist[x] in mydict:
                if mydict[mlist[x]] < n:
                    mydict[mlist[x]]=n
            else:
                mydict[mlist[x]] = n
        else:
            if mlist[x] in mydict:
                if mydict[mlist[x]] < n:
                    mydict[mlist[x]]=n
            else:
                mydict[mlist[x]] = n


value=1
def nextp():
    global value
    print(mydict)
    for x in mydict:
        value*= x**mydict[x]

main(factors)
nextp()
print(value)

