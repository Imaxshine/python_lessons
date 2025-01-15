
def main():
    number = [1,2,3,4,5,6]
    infile = open(r'C:\Users\DELL\Desktop\project\sequence\numbers.txt','w')
    for num in number:
        infile.write(str(num) + '\n')
    infile.close()
main()
