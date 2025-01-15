# if elif else statement
grade_a = 90
grade_b = 80
grade_c = 70
grade_d = 60

scores = int(input("Enter your Exam score: "))
if scores >= grade_a:
    print("You have scored grade A")
elif scores >= grade_b:
    print("You have scored grade B")
elif scores >= grade_c:
    print("You have scored grade C")
elif (scores >= grade_d):
    print("You have scored grade D")
else:
    print("You have scored grade F")