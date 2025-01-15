# Soma data zote kutoka 
# kwenye file husika

# def Sales():
#     sales_files = open(r"C:\Users\DELL\Desktop\project\Files\sales.txt","r")

#     lines = sales_files.readline()
#     endFile = ""
#     while lines != endFile:
#         amount = float(lines)
#         print(amount)
#         lines = sales_files.readline()
#     sales_files.close()
#     print("All data were included")

# Sales()

# Read files data with for loop
def main():
    sales_files = open(r"C:\Users\DELL\Desktop\project\Files\sales.txt","r")
    # lines = sales_files.readline()
    for line in sales_files:
        amount = float(line)
        print("Tsh.",format(amount, ",.2f"),sep="")
        # print(type(amount))
    print("End of data")
    sales_files.close()
main()