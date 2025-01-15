# Chukulia unatakiwa kuunda program 
# ambayo hautambui itatakiwa ku run 
# mara ngapi endapo user atahitaji ku run 
# zaidi na zaidi
# ====================================================
# Hapa tutatengeneza accumulator 
# ambayo itashikilia jumla ya namba zoote atakazoingiza.
# ------------------------------------------------

# Mfano tuunde program ambayo Doctor ataingiza uzito wa kila mgonjwa 
# katika hospitali X sasa kwa kawaida hatujui doctor ataingiza uzito wa 
# wagonjwa wangapi
default_kg = 0.0
kilogram = int(input('Ingiza uzito (au 0 kuitimisha): '))
while kilogram != 0:
    default_kg = default_kg + kilogram
    kilogram = int(input('Ingiza uzito (au 0 kuitimisha): '))
print("Total weight is ",default_kg," Kg",sep="")
# ========copy 'py .\sentinel_loop.py' and paste to your Terminal