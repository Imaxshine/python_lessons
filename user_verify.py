# Tuseme unataka kuhakiki user name, 
# na password kutuka kwenye database yetu
# na kama information za user zitakuwa sawa 
# basi atakaribishwa katika programu yetu rasmi

# Taarifa za user kwenye database yetu
#user_name
userName = "Emmanueli"

# user password
password = "ema@12"

name = str(input("Enter user name: "))
user_pass = str(input("Enter your password: "))
if name == userName and user_pass == password :
    print("Helow! ",userName," you are very welcome to our program.",sep='')
elif name != userName:
    print("User name is invalid!")
elif user_pass != password:
    print("Password is Invalid!")

# =====copy 'py .\user_verify.py' to run in a Terminal====