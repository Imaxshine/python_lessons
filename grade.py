# ===============================
# Mkuu wa shule ya upili anaomba 
# umuundie mfumo utakaochuja 
# wanafunzi na kuwaweka kwenye 
# madaraja yao (Grade)

#  GRADES
# A = 90+
# B = 80+
# C = 70+
# D = 60+
# ===============================

grade_a = 90
grade_b = 80
grade_c = 70
grade_d = 60

# Take the pupils scores
pupil_scores = int(input("Enter your Exam score: "))
# check if scores does not exceed 100 marks
if pupil_scores > 100 :
    print("{} is exceeded 100 as the total marks".format(pupil_scores))
else:
    if pupil_scores >= grade_a:
        print("You scored Grade A")
    else:
        if pupil_scores >= grade_b:
            print("You scored Grade B")
        else:
            if pupil_scores >= grade_c:
                print("You scored Grade C")
            else:
                if pupil_scores >= grade_d:
                    print("You scored Grade D")
                else:
                    print("You scored Grade F")