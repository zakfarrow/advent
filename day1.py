# Program to read the entire file using read() function
input = open("input.txt", "r")
data = input.read().split('\n')

nums = {
    'one':'1',
    'two':'2',
    'three':'3',
    'four':'4',
    'five':'5',
    'six':'6',
    'seven':'7',
    'eight':'8',
    'nine':'9'
}

count = 0
for j in data:
    x = len(j)
    currLow = len(j)
    y = 0
    currHigh = 0
    for i in nums:
        l1 = j.find(i)
        l2 = j.find(nums[i])
        h1 = j.rfind(i)
        h2 = j.rfind(nums[i])
        if l1 == -1 and l2 != -1:
            currLow = l2
        elif l2 == -1 and l1 != -1:
            currLow = l1
        elif l1 != -1 and l2 != -1:
            currLow = min(l1, l2)

        if currLow < x:
            x = currLow
            numLow = i

        currHigh = max(h1, h2)
        if currHigh > y:
            y = currHigh
            numHigh = i
            
    count += int(nums[numLow] + nums[numHigh])
print(count)

input.close()