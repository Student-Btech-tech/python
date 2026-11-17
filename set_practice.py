ar1=[1,5,10,34,20,80]
ar2=[6,7,20,30,80]
ar3=[3,4,15,20,80,60]


s1=set(ar1)
s2=set(ar2)
s3=set(ar3)

p=s1&s2
q=p&s3

r=list(q)
print(r)