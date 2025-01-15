user_selector = 'yes'

# Repeate the task
user_selector = str(input("Would you like to process infomation? (yes/no) "))
while user_selector.lower() == 'yes':
    # Key variables
    min_boxes = 830
    max_boxes = 1010
    boxPereach = 40
    awarded = 36000

    userName = str(input('Enter your name: '))
    box_sales = int(input("Enter your total boxes sales: "))
    # Filter users Infomation:
    if box_sales < min_boxes:
        print("Helow dear ",userName," your total boxes of ",box_sales," is not satisfactory "+
              "to be given a commission because it is out of ",min_boxes,sep="")
        user_selector = str(input("Would you like to process another infomation? (yes/no) "))
    elif box_sales > max_boxes:
        diffeence = box_sales - max_boxes
        exactly_comm = box_sales - diffeence
        exactly_boxes = exactly_comm / boxPereach
        total_comm = awarded * exactly_boxes
        print("Gougious Mr.",userName," for reaching maxmum of your commission,"+
              " the total price is Tsh.",format(total_comm, ',.2f'),sep='')
        user_selector = str(input("Would you like to process another infomation? (yes/no) "))
    elif box_sales >= min_boxes or box_sales <= max_boxes:
        award_boxes = box_sales / boxPereach
        theAward = awarded * award_boxes
        print("Mr.",userName," your award is Tsh.",format(theAward, ',.2f'),sep="")
        user_selector = str(input("Would you like to process another infomation? (yes/no) "))


