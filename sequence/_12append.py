# Method au function hii ya append inaturahisishia 
# kuongeza data/element ndani ya list yetu
def main():
    student_names = []
    excution = 'y'
    times = 1
    while excution.lower() == 'y' and times >= 1:
        # times = 1
        name = input("Weka jina kwa mara ya #:"+str(times)+": ")
        student_names.append(name)
        print("Ungependa kuongeza majina zaid?")
        excution = input("Bofya 'y' kuongeza au 'n' kuitimisha: ")
        times = times + 1
        print('-----------------------------------------')
    # print("Haya ndio majina uliyoyaingiza:")
    if len(student_names) > 1:
        print("Haya ndio majina uliyoyaingiza:")
    elif len(student_names) < 2:
        print("Hili ndilo jina uliloingiza")
    for name in student_names:
        print(name)
main()