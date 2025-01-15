# Square root 
import math
# Examples of functions found in math module
# pi & e
# cosin()
# sqrt() e.t.c==>

def square_root():
    number = float(input('Enter a number: '))
    square = math.sqrt(number)
    print("The square root of ",number," is ",format(square,'.2f'),sep="")

square_root()
