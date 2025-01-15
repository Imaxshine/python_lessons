def main():
    number = get_value()
    print("The list items are {}".format(number))
    print('----------------\t---------------')
def get_value():
    List = []
    again = 'y'
    while again.lower() == 'y':
        value = int(input('Ingiza namba: '))
        List.append(value)
        print('Press "y" as Yes if anything else or "no": ')
        again = str(input("Would you like to add more? "))
    return List
main()