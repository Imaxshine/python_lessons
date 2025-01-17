# Detect if user apply capital or small leter while introduced  names
import sys
# print(sys.version)
Name = str(input("Ingiza majina yako matatu >"))
space1 = Name.find(" ")
# Find a next white space
space2 = Name.find(" ",space1 + 1)
string0 = Name[0]
stringA = space1 + 1
stringB = space2 + 1
if Name[0] == Name[0].lower():
    print("Inaonekana Jina la kwanza unatumia herufi ndogo badala ya {}".format(Name[0].upper())," umeandika {}".format(Name[0]),sep="")
    sys.exit()
if Name[stringA] == Name[stringA].lower():
    print("Inaonekana Jina la pili unatumia herufi ndogo badala ya {}".format(Name[stringA].upper())," umeandika {}".format(Name[stringA]),sep="")
    sys.exit()
if Name[stringB] == Name[stringB].lower():
    print("Inaonekana Jina la tatu unatumia herufi ndogo badala ya {}".format(Name[stringB].upper())," umeandika {}".format(Name[stringB]),sep="")
    sys.exit()
else:
    print("EXECELLENT YOU HAVE SUCCESS TO WRITE YOUR NAME")
    print(f"Your real name is {Name}")
    