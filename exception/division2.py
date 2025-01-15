# Catch Error by Error type

def division():
    try:
        num1 = int(input("Enter a number: "))
        num2 = int(input("Enter another number: "))

        result = num1 / num2
        print("Division of",num1,"and",num2,"is",result)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    

division()