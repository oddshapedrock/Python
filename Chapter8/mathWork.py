
while True:

    string = input("Problem: ")
    problem = string
    string = string.replace("-", "+").split("+")

    constant = ""
    leadTerm = ""

    for part in string[0]:
        if part.isnumeric():
            leadTerm += part
        else:
            if leadTerm == "":
                leadTerm = "1"
            break

    for part in string:
        if not "x" in part:
            constant = part
            
    def getFactors(number):
        lis = list(range(1, int(number)+1))
        return list(filter(lambda n : int(number) % n == 0, lis))

    cF = getFactors(constant)
    lF = getFactors(leadTerm)

    poss = set()
    possf = set()
    for x in cF:
        for y in lF:
            if x%y == 0:
                poss.add(str(int(x/y)))
                possf.add(str(int(x/y)))
            else:
                poss.add(str(x / y))
                possf.add(str(x)+"/"+str(y))
            
                
    print(cF, lF)
    print(poss)
    signs = []
    for char in problem:
        if char == "+" or char == "-":
            signs.append(char)
            
    print(signs)
    print(string)

    for index, part in enumerate(string):
        spl = part.split("x")
        string[index] = spl
        
    print(string)


    li = list(poss)
    t = []
    for pos in li:
        r = problem.replace("x", f"*{pos}")
        r = r.replace("^", "**")
        ans = eval(r)
        t.append(ans)
        r = problem.replace("x", f"*({-float(pos)})")
        r = r.replace("^", "**")
        ans = eval(r)
        t.append(ans)
        
    print(li)
    print(t)
    zeros = []
    for indx, stuff in enumerate(t):
        if stuff == 0:
            zero = (list(possf)[int(indx/2)])
            if not indx %2 == 0:
                zero = (f"-{zero}")
            zeros.append(zero)
            
    print(zeros)

