# Tunaweza pia ku loop na kudesplay random numbers zaidi ya moja
import random
no = 5
def myRand():
    for count in range(no):
        number = random.randint(1,20)
        print(number)
myRand()