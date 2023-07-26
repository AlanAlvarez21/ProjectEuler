F = [1,1]
F_even = []

f = 0
n = 4000000

i = 0

while f < n:

    f = F[i]+F[i+1]
    F.append(f)
    
    if f%2==0:
        F_even.append(f)

    i+=1
print(F)
print(F_even)
print(sum(F_even))