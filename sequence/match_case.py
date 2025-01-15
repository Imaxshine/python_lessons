umri = int(input("Ingiza umri > "))
# Apply match case
# match umri:
#     case 18:
#         print(f"Umri wa {umri} ni umri wa utu uzima")
#     case 45:
#         print(f"Umri wako wa {umri} ni mkubwa sana")
#     case _:
#         print('Hatutambui umri huu wa miaka {} '.format(umri),sep="") 
match umri:
    case _ if umri >= 15 and umri <= 18:
        print(f'umri wa miaka {umri} ni umri mzuri wa kujiunga na Academ zetu za mpira wa miguu!')
    case _ if umri < 15:
        left_age = 15 - umri
        print(f"Hongera bado umri wa mwaka/miaka {left_age} ili kujiunga rasmi na Academy zetu za mpira wa miguu")

    case _:
        added_age = umri - 18
        print(f"Umri wako wa miaka {umri} ni mkubwa sana, Tafadhali subiri awamu yako kwani umezidi miaka {added_age} zaidi")