# Making a nested loops
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for num in matrix:
    for list in num:
        print(list,end='')
    print()

print("----------------------------------")
list1 = [1,2,3,4]
list2 =['maembe','mbaazi','tembele','mchicha']
for number in list1:
    for list in list2:
        print(number,list)
    print()