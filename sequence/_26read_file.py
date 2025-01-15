def myFnct():
    cities = main()
    print('The Cities of Tanzania is: {}'.format(cities))
    
def main():
    infile = open(r'C:\Users\DELL\Desktop\project\sequence\cities.txt','r')
    readFile = infile.readlines()
    index = 0
    while index < len(readFile):
        readFile[index] = readFile[index].rstrip()
        index = index + 1
    infile.close()
    return readFile
myFnct()