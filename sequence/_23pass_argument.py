# pass a list as argument in a function
# fruits = ['Apple','Straubel','Mango','Orange']
# def items(f = fruits):
#     print('Fruits are most as ',end='')
#     for fruit in f:
#         print(fruit," ",sep='',end='')
# items()

def main():
    number = [3.5,5.0,7.06,1.3,5.5]
    print("The total is",get_sum(number))
def get_sum(value):
    # create accumulator
    total = 0.0
    for no in value:
        total = total + no
    return total
main()