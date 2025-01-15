# ============Return values more than one value========

def Names(jina1,jina2):
    return jina1,jina2

name1 = str(input("Enter the first name: "))
name2 = str(input("Enter the last name: "))
first,last = Names(name1,name2)
print("A full names is",first,last)
