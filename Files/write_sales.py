# Weka taarifa za mauzo 
# katika file kwa kutumia loop

def Sales():
    # muulize mtumiaji aingize jumla ya siku za mauzo
    sales = int(input('How long do you have a sales? '))
    sales_file = open(r"C:\Users\DELL\Desktop\project\Files\sales.txt", 'w')
    for Round in range(1, sales + 1):
        daily_balance = float(input("Enter a balance of day #" + str(Round) + ": "))
        sales_file.write(str(daily_balance) + '\n')
    sales_file.close()
    print("All sales are recorded successfully.")
Sales()
