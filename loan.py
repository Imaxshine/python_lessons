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
work_experience = int(input("Enter the year which you start to work: "))
years_at_work = 2024 - work_experience #Find the years differences (cuurent year - work_experience)
totat_salary = salary * 12 #Number of months in a year (12)

if totat_salary >= annual_salary :
     if years_at_work >= duration_years:
          print("Hellow custom, you have reached all criteria to take a loan")
     else:
          print("Your work experience of {} year is not required. Only at least 3 years.".format(years_at_work) +
                  "Welcome back next year")
else:
     print('Your salary $',format(totat_salary, '.2f'),' has no criteria',sep='')
                