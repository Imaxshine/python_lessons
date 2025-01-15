def main():
    infile = open(r"C:\Users\DELL\Desktop\project\Files\text.txt",'r')
    
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()

    line1 = line1.rstrip()
    line2 = line2.rstrip()
    line3 = line3.rstrip()

    print(line1)
    print(line2)
    print(line3)

    infile.close

main()  