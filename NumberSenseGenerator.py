import random

################### HERE ARE THE IMPORTANT CONSTANT DEFINITIONS #####################
numQuestions = 80
numTricks = 6

test = open('test.tex','w')
lst = []
ansblk = "\_\_\_\_\_\_\_\_\_\_"

#####################   Begin Trick Definitions     #####################
def foil ():
    a = random.randint(16, 99)
    b = random.randint(16, 99)
    str1 = "%d x %d = %s" % (a, b, ansblk)
    str2 = "%d" % (a*b)
    return [str1,str2]

def add ():
    a = random.randint(150, 9999)
    b = random.randint(150, 9999)
    c = random.randint(150, 99999)
    str1 = "%d + %d + %d = %s" % (a, b, c, ansblk)
    str2= "%d" % (a + b + c)
    return [str1, str2]

def polyNumber ():
    sel = random.randint(1,3)
    num = random.randint(4,12)
    ans = 0
    st = ""
    if (sel == 1):
        st = "triangular"
        ans = num*(num+1)/2
    elif (sel == 2):
        st = "pentagonal"
        ans = num*(3*num-1)/2
    else:
        st = "hexgonal"
        ans = num*(2*num-1)
    str1 = "Find the %dth %s number:  %s" % (int(num), st, ansblk)
    str2 = "%d" % (ans)
    return [str1, str2]

def fracWhole ():
    sel = random.randint(1,2)
    ans = 0
    a = 0
    b = 0
    c = 0
    d = 0
    whole = 0
    num = 0
    den = 0
    str1 = ""
    str2 = ""
    if (sel == 1):
        a = random.randint(11,25)
        b = a + random.randint(2,5)
        whole = (a*a)/b
        num = (a*a)%b
        den = b
        str1 = "$%d$ x $\\frac{%d}{%d}$ = %s" % (a, a, b, ansblk)
        str2 = "$%d\\frac{%d}{%d}$" % (whole, num, den)
    else:
        a = random.randint(11,25)
        d = random.randint(1,5)
        b = a + d
        c = b + d
        whole = (a*b)/c
        num = (a*b)%c
        den = c
        str1 = "$%d$ x $\\frac{%d}{%d}$ = %s" % (a, b, c, ansblk)
        str2 = "$%d\\frac{%d}{%d}$" % (whole, num, den)
    return [str1, str2]

def divisors ():
    sum = 1
    prop = ""
    num = random.randint(20,99)
    for i in range(2,num):
        if num % i == 0:
            sum = sum + 1
    j = random.randint(1,2)
    if (j == 1):
        prop = " proper"
    else:
        sum = sum + 1
    str1 = "No. of%s divisors of %d? %s" % (prop, num, ansblk)
    str2 = "%d" % (sum)
    return [str1, str2]

def mixedNumToImp ():
    a = random.randint(3,9)
    b = random.randint(2,11)
    c = random.randint(1,a-1)
    str1 = "Convert to improper $%d\\frac{%d}{%d}$%s" % (b, c, a, ansblk)
    str2 = "$\\frac{%d}{%d}$" % (b * c, a)
    return [str1, str2]
#####################   End of Trick Definitions    ##################### 


for i in range(0,numQuestions):
    lst.append(random.randint(0,numTricks-1))

test.write('\\documentclass{article}\n')
test.write('\\usepackage[margin=1in]{geometry}\n')
test.write('\\usepackage{multicol}\n')
test.write('\\begin{document}\n')
test.write('\\begin{center}{\\Large Number Sense Drills}\\end{center}\n')
test.write('\\begin{multicols}{2}\n')
test.write('\\begin{enumerate}\n')

st = ""

###### Question Iterator ######
for i in range(0,numQuestions):
    j = random.randint(0, len(lst))
    k = lst.pop()
    test.write("\\item ")
    if k == 0:
        arr = add()
        test.write(arr[0])
        temp = "\\item %s \\\\ \n" % (arr[1])
        st = st + temp
    elif k == 1:
        arr = foil()
        test.write(arr[0])
        temp = "\\item %s \\\\ \n" % (arr[1])
        st = st + temp
    elif k == 2:
        arr = polyNumber()
        test.write(arr[0])
        temp = "\\item %s \\\\ \n" % (arr[1])
        st = st + temp
    elif k == 3:
        arr = fracWhole()
        test.write(arr[0])
        temp = "\\item %s \\\\ \n" % (arr[1])
        st = st + temp
    elif k == 4:
        arr = divisors()
        test.write(arr[0])
        temp = "\\item %s \\\\ \n" % (arr[1])
        st = st + temp
    elif k == 5:
        arr = mixedNumToImp()
        test.write(arr[0])
        temp = "\\item %s \\\\ \n" % (arr[1])
        st = st + temp
    test.write(' \\\\ \n')
test.write('\\end{enumerate}\n')
test.write('\\end{multicols}\n')
test.write('\\pagebreak\n\\pagenumbering{gobble}\n')
test.write('\\begin{center}{\\Large Answer Key}\\end{center}\n')
test.write('\\begin{enumerate}\n')
test.write('\\begin{multicols}{4}\n')
test.write(st)
test.write('\\end{multicols}\n')
test.write('\\end{enumerate}\n')
test.write('\\end{document}\n')
