lista = []

for i in [lista for lista in range(1, 1000)]: 
    if i%3 == 0 or i%5 == 0:
        lista.append(i) 

print(sum(lista))



