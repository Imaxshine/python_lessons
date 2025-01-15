# Find the average from the list 
# Formula:  Average = Total / Number
numbers = [1,2,3,4,5,15,6890,6745,899,788]
total = 0
for value in numbers:
    total += value
num = len(numbers)
print('Average of ',numbers,'is: ',end='')
average = total / num
print(format(average, '.2f'))
