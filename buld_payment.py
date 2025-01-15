# John build company
saaZakazi = 45
nyongeza = 2

# Taarifa za mfanyakazi
saa  = float(input("Ingiza muda uliotumika kazini: "))
malipo_ya_kawaida = float(input("Ingiza malipo kwa saa: "))

if (saa > saaZakazi):
    mudaUliozidi = saa - saaZakazi
    ongezekoLaziada = mudaUliozidi * malipo_ya_kawaida * nyongeza
    jumla_ya_malipo = (malipo_ya_kawaida * saaZakazi) + ongezekoLaziada
else:
    jumla_ya_malipo = malipo_ya_kawaida * saa

print("Jumla ya malipo ya mfanyakazi ni Tsh:",format(jumla_ya_malipo, ',.2f'),sep="")
