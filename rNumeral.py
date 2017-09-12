#! /bin/python3
import sys


def romanNumeralWrite(arabicNumeral):
    try:
        number = int(arabicNumeral)
    except:
        return None
    M, x = divmod(number, 1000)
    D, x = divmod(x, 500)
    C, x = divmod(x, 100)
    L, x = divmod(x, 50)
    X, x = divmod(x, 10)
    V, x = divmod(x, 5)
    returnstring = ('M' * M) + ('D' * D) + ('C' * C) + ('L' * L) + ('X' * X) + \
                   ('V' * V) + ('I' * x)
    specials = [("DCCCC", "CM"), ("CCCC", "CD"), ("LXXXX", "XC"), ("XXXX", "XL"),
                ("VIIII", "IX"), ("IIII", "IV")]

    def cornercase(instring, value):
        outstring = instring
        if value[0] in outstring:
            while True:
                if outstring.find(value[0]) != -1:
                    outstring = outstring[:outstring.find(value[0])] + \
                                          value[1] + \
                                          outstring[outstring.find(value[0]) + 
                                          len(value[0]):]
                else:
                    break
        return outstring

    for case in specials:
        returnstring = cornercase(returnstring, case)
    return returnstring


if __name__ == "__main__":
    print(romanNumeralWrite(sys.argv[1]))
