# Haishauriwi sana kutumia gloabal variable
# katika long sequence of code mfano kuepuka 
# Error ambazo zinaweza kubebwa na global variables 
# na kuwa ngumu kugundua kwanini variable fulani 
# imebeba value tofauti na output inayotarajiwa.

# =============================

# name = input("Enter your name: ")
# def Name():
#     print("Your name is: ",name,sep="")
# Name()

number = 0
def main():
    # global number
    number = int(input("Enter number: "))
    print(number)
main()