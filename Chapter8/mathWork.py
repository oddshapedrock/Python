from fractions import Fraction
import decimal
while True:
    try:
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
                    problem = "1" + problem
                break
        try:
            pwr = string[0].split("^")[1]
        except Exception:
            pwr = "1"
            
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
      
        print(f"P values: {cF}")
        print(f"Q values: {lF}")
        
        signs = []
        for char in problem:
            if char == "+" or char == "-":
                signs.append(char)

        for index, part in enumerate(string):
            spl = part.split("x")
            string[index] = spl

        possf = list(possf)
        li = list(poss)
        li = sorted(li, key=lambda x: float(x))
        possf.sort()
        
        def fractionize(s):
            if not "/" in s:
                return int(s)
            n, d = s.split('/')
            return Fraction(n) / Fraction(d)
        possf = list(sorted(possf, key=fractionize))
        print(f"p/q values: +- {possf}")
        
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
            
        zeros = []
        for indx, stuff in enumerate(t):
            if stuff == 0:
                zero = (li[int(indx/2)])
                if "." in zero:
                    indxs = li.index(zero)
                    zero = (possf[indxs])
                if not indx %2 == 0:
                    zero = (f"-{zero}")
                zeros.append(zero)
                
        print(f"Here are the zeros: {zeros}")
        
        if len(zeros) < int(pwr):
            print(f"Warning! Not all zeros were found!\nA possible {int(pwr) - len(zeros)} others exist")
        
        
    except SyntaxError:
        print("Error could not evaluate -> Please use a 1 before a x values with a coef of 1.")
    except ValueError:
        print("Error could not find necessary values -> ensuer a coef exists even if it is just +0!")