def diffDays():
    try:
        for dot in range(1,51):
            print(".",end="")
        print()
        print("A System of total count the days between two different dates")
        from datetime import datetime
        date1_input = input("Enter date1: eg 01-01-2021 > ")
        date2_input = input("Enter date2: eg 20-03-2021 > ")
        date1 = datetime.strptime(date1_input,"%d-%m-%Y")
        date2 = datetime.strptime(date2_input,"%d-%m-%Y")

        differences = abs((date1 - date2).days)
        print(f"The different of date {date1_input} and {date2_input} is total of {differences} days")
    except Exception as error:
        print("Some Errors occure: " + f"{error}")
diffDays()