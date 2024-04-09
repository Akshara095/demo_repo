#armstrong or not
n=int(input())
r=0
temp=n
s=0
while(n!=0):
    s=int(n%10)
    n=int(n/10)
    r+=int(s*s*s)
if(r==temp):
    print("the given number is armstrong")
else:
    print("the given number is not a armstrong")
