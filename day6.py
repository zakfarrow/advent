import math

input = open("data/input6.txt", "r")
data = input.read().split('\n')



times = ' '.join(data[0].split(' ')).split()
distances =' '.join(data[1].split(' ')).split()
del times[0], distances[0]
x=[]
for i in range(0, len(times)):
    t = int(times[i])
    d = int(distances[i]) 
    lb = math.ceil((t-math.sqrt(t**2-4*d))/2)
    ub = math.floor((t+math.sqrt(t**2-4*d))/2)
    x.append(ub - lb + 1)
ans = 1
for i in x:
    ans *= i
print(ans)
input.close()