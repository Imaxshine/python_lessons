# ===========================
# Chukulia Bank X inatoa mikopo 
# kwa wafanyakazi wa umma na sekta 
# binafsi ila kwa wenye vigezo 
# vikuu viwili

# 1: Awe amefanya kazi serikalini au sekta binafi ya sasa kuanzia 
#    miaka mitatu (3) na kuendelea

# 2: Jumla ya mshahara wake kwa mwaka mzima usiwe chini ya $2500
# ===========================

duration_years = 3
annual_salary = 2500.0

salary = float(input("Enter your monthly salary in current dolar currency: "))
work_experience = int(input("Enter numbers of years at job: "))
if salary >= annual_salary and work_experience >= duration_years :
    print("Dear custom, you qualified to a loan")
else:
    print("Your credentials are not satisfactory")