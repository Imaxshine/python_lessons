# Let say that a student wish to 
# learn three of subjects and he/she want to 
# eliminate one subject among those three

def mySubject():
    subjects = ['mathematics','physics','chemistry']
    print('These below are the subjects to learning.')
    print(subjects)
    try:
        option = str(input('Remove unfavorite subject if any by naming it. '))
        option_sub = subjects.index(option)
        favorite_sub = str(input('Write your new favorite subject. '))
        subjects[option_sub] = favorite_sub
        print('This is your course subjects.')
        print('-----------------------------')
        print(subjects)
    except:
        print("It seems as you write a wrong subject name as {}.".format(option))
mySubject()
