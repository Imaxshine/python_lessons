# Tuchukulie mfdano unaunda programu ya wanafunzi 
# ambayo itawasaidia katika kuonesha jumla ya matokeo yao.

# Sasa kwa hali ya kawaida aipaswi mwanafunzi kuingiza matokeo
# chini ya (<) 0 yaani negative numbers na matokeo yasizidi 100.

print('Program hii inachakata matokeo yasiyozidi 100 na yasiyopungua 0')
scores = int(input("Ingiza matokeo yako au -1 kuhitimisha: "))
while scores != -1:
    if scores < 0 or scores > 100:
        print("Hairuhusiwi kuingiza namba zaidi ya 100 au chini ya 0 kama ilivyo ",scores,sep='')
        scores = int(input("Ingiza matokeo yako au -1 kuhitimisha: "))
    else:
        print("The marks is ",scores)
        scores = int(input("Ingiza matokeo yako au -1 kuhitimisha: "))