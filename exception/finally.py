# Finally maranyingi hutumika kama kufunga mafile ambayo hayakufungwa 
# kwani yenyewe inakuwa excuted bila ya kujali 
# kama try imefanikiwa au imepata errors

def Gross():
    print("Enter the hours and payments per hour")
    try:
        hours = int(input("Enter the worked hours: "))
        payment = float(input("Enter your hour payment: "))
        gross_payment = hours * payment

        # print gross pay
        print("The gross pay is Tsh.",format(gross_payment,",.2f"),sep="")
    # print a default Exception Error:
    except Exception as error:
        print(error)
    finally:
        print("It's a finally.")

Gross()