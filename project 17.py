td={1:"one",
    2:"two",
    3:"three",
    4:"four",
    5:"five",
    6:"six",
    7:"seven",
    8:"eight",
    9:"nine",
    10:"ten",
    11:"eleven",
    12:"twelve",
    13:"thirteen",
    14:"fourteen",
    15:"fifteen",
    16:"sixteen",
    17:"seventeen",
    18:"eighteen",
    19:"nineteen",
    20:"twenty",
    30:"thirty",
    40:"forty",
    50:"fifty",
    60:"sixty",
    70:"seventy",
    80:"eighty",
    90:"ninety",
    100:"onehundred",
    200:"twohundred",
    300:"threehundred",
    400:"fourhundred",
    500:"fivehundred",
    600:"sixhundred",
    700:"sevenhundred",
    800:"eighthundred",
    900:"ninehundred",
    1000:"onethousand"
}
for x in range(21,30):
    td[x] = td[20]+td[x-20]

for x in range(31,40):
    td[x] = td[30]+td[x-30]

for x in range(41,50):
    td[x] = td[40]+td[x-40]

for x in range(51,60):
    td[x] = td[50]+td[x-50]

for x in range(61,70):
    td[x] = td[60]+td[x-60]

for x in range(71,80):
    td[x] = td[70]+td[x-70]

for x in range(81,90):
    td[x] = td[80]+td[x-80]

for x in range(91,100):
    td[x] = td[90]+td[x-90]

for x in range(101,200):
    td[x] = td[100]+"and"+td[x-100]

for x in range(201, 300):
        td[x] = td[200] + "and" + td[x - 200]

for x in range(301,400):
    td[x] = td[300]+"and"+td[x-300]

for x in range(401,500):
    td[x] = td[400]+"and"+td[x-400]

for x in range(501,600):
    td[x] = td[500]+"and"+td[x-500]

for x in range(601,700):
    td[x] = td[600]+"and"+td[x-600]

for x in range(701,800):
    td[x] = td[700]+"and"+td[x-700]

for x in range(801,900):
    td[x] = td[800]+"and"+td[x-800]

for x in range(901,1000):
    td[x] = td[900]+"and"+td[x-900]


all=""

for x in td:
    all+=td[x]

print(len(all))