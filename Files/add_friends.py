def main():
    print("Add another Three friends.")
    name1 = str(input("Enter #1: "))
    name2 = str(input("Enter #2: "))
    name3 = str(input("Enter #3: "))

    file_name = open("C:\\Users\\DELL\\Desktop\\project\\Files\\friends.txt",'a')

    file_name.write(name1 + '\n')
    file_name.write(name2 + '\n')
    file_name.write(name3 + '\n')

    print("Your aditional friends names" +
          " are all stored in friends.txt file")
main()
