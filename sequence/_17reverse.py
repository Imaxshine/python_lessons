# reverced lists / iterms
def myFunct():
    myList = ['Emma','Bakari','Nondo','Abigaeli','Joeli','Shabani']
    print("Original Sequence", myList)
    print()
    myList.sort()
    # Ascend order
    print("Ascend Order: ",myList,sep="")
    # Descend order
    desend_order = myList
    desend_order.reverse()
    print("Descend order: ",desend_order,sep='')
myFunct()