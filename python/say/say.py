def say():
    
    

    pass
def hundred(n):
    if int(n)<10:
        return ten(n)
    elif n[0]=="2":
        return "twenty"+ten(n[1])
    elif n[0]=="3":
        return "thrity"+ten(n[1])
    elif n[0]=="4":
        return "fourty"+ten(n[1])
    elif n[0]=="5":
        return "fifty"+ten(n[1])
    elif n[0]=="6":
        return "sixty"+ten(n[1])
    elif n[0]=="7":
        return "seventy"+ten(n[1])
    elif n[0]=="8":
        return "eighty"+ten(n[1])
    elif n[0]=="9":
        return "ninety"+ten(n[1])
    elif n=="10":
        return "ten"
    elif n == "11":
        return "eleven"
    elif n == "12":
        return "twelve"
    elif n == "13":
        return "thirteen"
    elif n == "14":
        return "fourteen"
    elif n == "15":
        return "fourteen"
    elif n == "16":
        return "sixteen"
    elif n == "17":
        return "seventeen"
    elif n == "18":
        return "eighteen"
    elif n == "19":
        return "nineteen"
    
    
    pass
def ten(n):
    n = int(n)
    if n == 1:
        return "one"
    elif n == 2:
        return "two"
    elif n==3 :
        return "three"
    elif n == 4:
        return "four"
    elif n==5 :
        return "five"
    elif n==6 :
        return "six"
    elif n==7 :
        return "seven"
    elif n==8 :
        return "eight"
    elif n==9 :
        return "nine"
    else:
        return ""
