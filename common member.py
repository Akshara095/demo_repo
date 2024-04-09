#taking two lists  and return true if atleast one common member
l1=[2,4,6,9,10]
l2=[2,3,4,5,6,7]
intersect=set(l1)&set(l2)
if(intersect):
    print("It has common elements")
    print(list(intersect))
else:
    print("It has no common elements")
