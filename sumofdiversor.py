counter=1
import math
n=5

for i in range(1,n+1):
    temp=0
    sqrtN = int(math.sqrt(i)) 
    for j in range(1,sqrtN):
        if i%j==0:
            #print(i,j)
            counter+=j+i
            print(i,j)
            print(counter)
        
print(counter)

