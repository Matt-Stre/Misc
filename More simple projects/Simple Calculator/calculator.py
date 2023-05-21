def calculate(a,b,calculation):
    
    if type(a)==int and type(b)==int:
        if calculation=="+":
            return a+b
        elif calculation=='-':
            return a-b
        elif calculation=='/':
            return a/b
        elif calculation=='*':
            return a*b
        else:
            return "Error invalid operation."
    else:
        return "Error invalid numbers."