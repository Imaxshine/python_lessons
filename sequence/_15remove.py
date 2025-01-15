# my_list = [1,2,3,4,5,6]
# print('Original list',my_list)
# my_list.remove(4)
# my_list.remove(1)

# print('List after remove an element',my_list)
# names = ['Ally','Bakari','Nondo']
# print('An original list',names)
# names.remove('Nondo')
# names.append('Emmanueli')
# print('New names',names)

# Try now to make simple  CRUD
def userReg():
    print('Hellow, we need you to enroll new pupils in Chamazi Secondary school')
    names = []
    try:
        question = 'y'
        while question.lower() == 'y':
            name1 = str(input('Enter a pupils first name: '))
            names.append(name1)
            name2 = str(input("Enter a pupil second name: "))
            names.append(name2)
            name3 = str(input('Enter a pupil last name: '))
            names.append(name3)
            question = str(input('Would you like to add a new enrollment? press "y" to continue or "n" to stop enrollment: '))

        # yes = 'y'
        print("Would you want to Edit any of this names? ",names," press 'y' to edit or 'n' to stop ",sep='',end='')
        yes = str(input())
        while yes.lower() == 'y':
            item_remove = str(input('Write a name to remove: '))
            item_index = names.index(item_remove)
            new_name = str(input('Replace a new name: '))
            names[item_index] = new_name
            print('congratulation your enrollment is up to date ',end="")
            print("as",names)
            yes = str(input("Write 'y' to continue edit or 'n' to stop edit: "))
        print('Your enrolment pupils names are: ',end='')
        for name in names:
            print(name + " ",end='')
    except Exception as err:
        print(err)
userReg()
