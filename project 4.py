def checkpalindrome(num):
    if len(num) < 4:
        if num[0] == num[len(num) - 1]:
            return True
        else:
            return False
    else:
        if num[0] == num[len(num) - 1]:
            return(checkpalindrome(num[1:len(num)-1]))
        else:
            return False

big = 0

def main(start, sec):
    global big
    a = start
    b = sec
    while a > round(start/2):
        if checkpalindrome([int(x) for x in str(a * b)]):
            if (a * b) > big:
                print(a)
                print(b)
                print(a*b)
                big = (a * b)
                a -= 1
            else:
                a -= 1
        else:
            a -= 1
    else:
        if b > round(start/2):
            main(start, b - 1)
        else:
            print(big)

main(1000, 1000)

