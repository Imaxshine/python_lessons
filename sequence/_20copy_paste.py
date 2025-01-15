# copy and paste list 
# -----------------------------
# list1 = [1,2,3,4,5]
# list2 = list1 #assign a list in a new variable
# print(list2)

# -----------------------------
# Use loop to paste a contents
# list1 = [1,2,3,4,5]
# list2 = []
# for newlist in list1:
#     list2.append(newlist)
# print('List 2 {}'.format(list2))

# -------------------------------------
# paste list in a new list 
list1 = [1,2,3,4,5]
list2 = [] + list1
print('list 2',list2)
