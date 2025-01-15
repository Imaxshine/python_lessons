def readNumbers():
    file_to_read = open(r"C:\Users\DELL\Desktop\project\Files\numbers.txt",'r')

    read_number = int(file_to_read.readline())
    read_number2 = int(file_to_read.readline())

    print(read_number + read_number2)
    # print(type(read_number2))

readNumbers()