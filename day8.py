import re

def formatData(input):
    path = {}
    for i in input:
        temp = i.split(' ')
        path[temp[0]] = [re.sub(r'[\W_]+', '', temp[2]), re.sub(r'[\W_]+', '', temp[3])]
    return path

def partA(start, target):
    curr = start
    i=0
    count = 0
    while i < len(directions):
        if directions[i] == 'R':
            curr = data[curr][1]
        elif directions[i] == 'L':
            curr = data[curr][0]
        count+=1
        i+=1
        if curr == target:
            break
        if i == len(directions):
            i = 0
    return count

#Brute force method for part B
def partB():
    for i in data:
        if i[2] == 'A':
            startKeys.append(i)

    steps = 0
    i = 0
    curr = 0
    end = 0

    while i < len(directions):
        for curr in range(0, len(startKeys)):      
            if directions[i] == 'R':
                startKeys[curr] = data[startKeys[curr]][1]
            elif directions[i] == 'L':
                startKeys[curr] = data[startKeys[curr]][0]
        steps+=1
        end=0
        for j in range(0, len(startKeys)):
            if startKeys[j][2] == 'Z':
                end+=1
            else:
                break

        if end == len(startKeys):
            break
        else:
            i+=1 
        if i == len(directions):
            i = 0
    print(steps)

#Analysis the paths between start and end nodes, revealed that each start node had a unique end, and the
#cycle length at an end node was equal to the steps between its initial node and itself. This reduced the
#problem to finding the largest common multiple of all cycle lengths.  
def find_lcm(num1, num2):
    if(num1>num2):
        num = num1
        den = num2
    else:
        num = num2
        den = num1
    rem = num % den
    while(rem != 0):
        num = den
        den = rem
        rem = num % den
    gcd = den
    lcm = int(int(num1 * num2)/int(gcd))
    return lcm
     



input = open("data/input8.txt", "r")
data = input.read().split('\n')
directions = data[0]
del data[0]
del data[0]

data = formatData(data)

startKeys = []

l = []

l.append(partA('AAA', 'ZZZ'))
l.append(partA('GDA', 'SGZ'))
l.append(partA('QLA', 'VHZ'))
l.append(partA('RMA', 'FQZ'))
l.append(partA('NXA', 'BBZ'))
l.append(partA('PLA', 'MQZ'))

 
num1 = l[0]
num2 = l[1]
lcm = find_lcm(num1, num2)
 
for i in range(2, len(l)):
    lcm = find_lcm(lcm, l[i])

print(lcm)