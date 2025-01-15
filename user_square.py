# Muwezeshe user kudhibiti 
# loop yake yeye mwenyewe
print("""
      program hii itadisplay list ya 
      nambari na square ya kila nambari:
      -------------------------------------
      """)
start = int(input("Ingiza namba ya kianzio: "))
end = int(input("Ingiza namba ya ukomo: "))
print("Numbers | squareroot")
print('------------------')

for no in range(start,end+1):
    squareRoot = no**2
    print(no,'\t',squareRoot)