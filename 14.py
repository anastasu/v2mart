x = 36**7+6**19-18
k=0
while x>0:
    if x%6==5: k = k+1
    x = x//6
print (k)