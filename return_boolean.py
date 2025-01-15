# Rudisha boolean value
def is_odd(value):
    if value % 2 != 0:
        status = True
    else:
        status = False
    return status
val = int(input("Enter any number: "))
if is_odd(val):
    print("The number id real Odd:")
else:
    print("The number is not Odd but is real Even")