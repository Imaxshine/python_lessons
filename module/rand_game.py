import random
max_no = 6
min_no = 1
print('----------------------------------')
print("This GLD game needs you to win within an interval from 1 - 6")
golden_number = int(input("Enter your Golden number: "))
while golden_number != 0:
        if golden_number > max_no or golden_number < min_no:
            print("Your Golden number must begging from 1 and not exceed 6")
            golden_number = int(input("Enter your Golden number: "))
        def myRand():
            rand_num = random.randint(1,6)
            if golden_number == rand_num:
                print("Congratulations you win a game with equal of {} and {}".format(golden_number,rand_num))
            elif golden_number != rand_num:
                print("Sorry try again, your gold number {}".format(golden_number)," has no any gift, "+
                      "please Re-try more again. The GLD was {}".format(rand_num))
                
        myRand()
        golden_number = int(input("Enter your Golden number or 0 to over this GLD Game: "))