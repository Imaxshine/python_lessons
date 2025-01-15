# simple program for measure a pupipls average with the 4 tests

high_avg = 95
exam1 = int(input("Enter test one scores: "))
exam2 = int(input("Enter test two scores: "))
exam3 = int(input("Enter test three scores: "))
exam4 = int(input("Enter test four scores: "))

avg = (exam1 + exam2 + exam3 + exam4) // 4
print("Your total average is",avg)

# Compare current average with required which is (high_avg)
if avg >= high_avg :
    print("Excellent")
    print("The average that you scored is very high")