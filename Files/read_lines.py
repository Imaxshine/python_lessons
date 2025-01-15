def main():
    inputData = open("Files\\text.txt",'r')

    data_to_read1 = inputData.readline()
    data_to_read2 = inputData.readline()
    data_to_read3 = inputData.readline()

    inputData.close()
    print(data_to_read1,data_to_read3)
main()