def main():
    try:
        fileName = input("Enter a file name: ")
        infile = open("project\\"+fileName+"r")
        toReadfile = infile.read()
        print(toReadfile)
    except FileNotFoundError:
        print("The file {} is not available".format(fileName))
    except FileExistsError:
        print("This file "+fileName +" is not exists")
    except:
        print("Sorry file "+fileName +" may not found currently")
main()
