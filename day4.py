input = open("data/input4.txt", "r")
data = input.read().split('\n')
del data[198]


score = 0

for i in data:
    matches = []
    found = []
    index = i.index(':')
    line = i.index('|')
    first = i[index + 2:line - 1]
    second = i[line + 2:]
    myNums = first.split(' ')
    winNums = second.split(' ')
    myNums = list(filter(None, myNums))
    winNums = list(filter(None, winNums))
    for num in winNums:
        if num in myNums and num not in found:
            matches.append(num)
            found.append(num)
    if len(matches) != 0:
        score += (2 ** (len(matches) - 1))


print(score)