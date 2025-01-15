def main():
    try:
        cities = ['Shinyanga','Dar es Salaam','Arusha','Mbeya','Singida']
        outfile = open(r'C:\Users\DELL\Desktop\project\sequence\cities.txt','w')
        for city in cities:
            outfile.write(city + '\n')
        outfile.close()
    except Exception as error:
        print(error)
main()