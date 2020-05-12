total = 0
maxval = 1000
for x in range(maxval):
    if x % 3 == 0 or x%5==0 :
        total += x
print(total)