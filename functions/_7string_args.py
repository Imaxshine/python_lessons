# Tumia function kufanya
# string reverse

def main():
    name1 = str(input("Enter first name: "))
    name2 = str(input("Enter second name: "))
    names_reverse(name1.capitalize(),name2.capitalize()) #new function declared

def names_reverse(firstName,secondName):
    print("Reversed names is {}-{}".format(secondName,firstName))

main()