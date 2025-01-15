# Chukua user input kisha ziifadhi kwenye file husika
def main():
    print("Enter three names of your friends.")
    name1 = input("Enter first name: ")
    name2 = input("Enter second name: ")
    name3 = input("Enter third name: ")
    keepNames = open(r"C:\Users\DELL\Desktop\project\Files\friends.txt",'w')

    keepNames.write(name1 + '\n')
    keepNames.write(name2 + '\n')
    keepNames.write(name3 + '\n')
    

    keepNames.close()

    print("All names are stored in friends.txt")
main()
