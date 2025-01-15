# Simple program for gross payments
usual_hours = 40
bonus = 1.5

# Get employees infomation
employee = str(input("What is Employee name? "))
respons_hours = float(input("Enter responsible hours per week: "))
paymentPerweek = float(input("Enter the payment rate per week: "))

if (respons_hours > usual_hours):
    extra_hours = respons_hours - usual_hours
    added_amount = paymentPerweek * extra_hours * bonus
    total_payment = usual_hours * paymentPerweek + added_amount
else:
    # Only for employees reached 40 hrs or < (less) than 40 hrs per week
    total_payment = respons_hours * paymentPerweek

# Print out results 
print("The total payment of {} is \
$".format(employee.capitalize()),format(total_payment, ',.2f')," Per week",sep='')
