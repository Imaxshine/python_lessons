# Slicing ni kitendo cha kuondoa au kuchukua 
# sehemu fulani ya elements ndani ya list

list1=['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Sartaday']
# Slicing a list1
days=list1[1:6]
size = len(days)
id = 0
while id < size:
    # print(days[id])
    id = id + 1
for day in days:
    print(day)
