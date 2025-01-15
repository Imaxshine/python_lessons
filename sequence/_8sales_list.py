def main():
    # Takes some days of the week not exceed 7 days as usually
    print("Insert the total days of sales")
    try:
        days = int(input("Enter the total days: "))
        if(days > 7 or days <= 0):
            print("sorry, the days of the week is between 1 - 7 and not ",days,sep="")
        else:
            sales = [0] * days
            index = 0
            while index < len(sales):
                print("Sales of day#",index+1,": ",sep="",end="")
                sales[index] = float(input())
                index +=1
            print("You have entered this records.")
            for val in sales:
                print(format(val,",.2f"))
    except Exception as err:
        print(err)
main()
                
