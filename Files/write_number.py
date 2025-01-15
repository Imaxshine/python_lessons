def main():
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    num3 = int(input("Enter another number: "))

    myfile = open(r"C:\Users\DELL\Desktop\project\Files\numbers.txt","a")

    myfile.write(str(num1) + '\n')
    myfile.write(str(num2) + '\n')
    myfile.write(str(num3) + '\n')

    myfile.close()
    print("Numbers are written to numbers.txt file.")

main()
