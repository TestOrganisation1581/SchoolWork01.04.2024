f=open("17_13088.txt")
A=[int(n) for n in (f)]
k=0
ma=0
mas=0
for i in range(len(A)):
    if(ma<A[i] and A[i]%17==0):
        ma=A[i]
for i in range(len(A)-2):
    if(((9999>=A[i]>=1000 and 9999>=A[i+1]>=1000) or (9999>=A[i]>=1000 and 9999>=A[i+2]>=1000) or (9999>=A[i+2]>=1000 and 9999>=A[i+1]>=1000))
            and (A[i]%5==0 or A[i+1]%5==0 or A[i+2]%5==0)
            and A[i]+A[i+1]+A[i+2]>ma):
        k+=1
        if(mas<A[i]+A[i+1]+A[i+2]):
            mas=A[i]+A[i+1]+A[i+2]
print(k,mas)