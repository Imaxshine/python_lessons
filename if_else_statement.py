age = 22
if (age >= 18):
    # Collect a voters details
    name = "EmmaNuelI"
    age2 = age
    msg = "You are eligible to vote"
    print("Dear {} {} with your {} years \
old".format(name.upper(),msg,age2))
else:
    print("You are not eligible to vote with {} years old".format(age))