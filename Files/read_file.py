# Kusoma data kutoka kwenye file husika

def readData():
    name = open(r"Files\customer.txt",'r')
    names = open(r"Files\friends.txt", 'r')

    get_name = name.read()
    get_msg = names.read()

    # print(get_name)
    print(get_msg)

    name.close()
    names.close()

readData()