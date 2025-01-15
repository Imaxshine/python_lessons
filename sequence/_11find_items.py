names = ['Emma','john','ibra','juma','ally','yasinta','Yeze']
# Find the item from the given list
search_name = "mwajuma"
for val in names:
    if search_name in val:
        print("{}".format(val)," is available",sep="")
        break
else:
    print("{}".format(search_name)," Is not available",sep="")
