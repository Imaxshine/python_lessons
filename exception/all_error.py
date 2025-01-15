# Catch Errors by a single msg
def Payment():
    try:
        print("Gros payment calculations")
        hour = int(input("Enter the hours that you work's: "))
        payment = float(input("Gros pay per hour: "))

        gros_pay = hour * payment
        print("Gros pay is Tsh.",format(gros_pay,',.2f'),sep="")
    except:
        print("ERROR: hours and gros pay must be valid!")
Payment()