# Remove Error report by 
# using if else statement

def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))

    if num2 != 0:
        result = num1 // num2
        print(num1,"divide by",num2,"is",result)
    else:
        print("cannot divide by zero")
main()
