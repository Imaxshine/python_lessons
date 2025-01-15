numbers = [1,2,3,4,5,6]
# iterate data from the list
# for no in numbers:
#     print(no)
# ==========================

# for no in numbers:
#     init = 1
#     no = init + no
#     print(no)
# ================================
total = 0
for no in numbers:
    total = no + total
print(total)