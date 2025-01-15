# Pass parameters within a function
def Bongo(num):
    row = 0
    for b in range(num):
        row += 1
        if row >= 200 + 1:
            print("we only end with 200")
            break
        print(f"{row}: Emmanueli as Python Expert")
num = int(input("Unataka kuchapisha mara ngapi? > "))

Bongo(num)