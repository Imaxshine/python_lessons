# Hifadhi jumla ya count iteration 
# atakazoingiza user
# ndani ya mizunguko maalum 
# utakayoipitisha katika loop

max_no = 5
accumulator = 0.0
print("Program hii itatoa jumla"+
      " ya namba ",max_no," utakazoingiza.",sep='')

for counter in range(max_no):
    number = int(input("Enter any number: "))
    accumulator = accumulator + number
print("Total of your numbers is: ",accumulator)