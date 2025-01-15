# Tunaweza kutumia key argument bila
#katika function bila ya kuzingatia position
# kama ilivyokuwa hapo awali

def Argu():
    name1 = input('First name: ')
    name2 = input('Second name: ')
    show_names(second = name2,first = name1) #Ignore Position with key arguments

def show_names(first,second):
    print("full name is ",first," ",second,sep='')

Argu()