myNums = [83, 86,  6, 31, 17,  9, 48, 53]
winNums = [41, 48, 83, 86, 17]

score = 0
matches = []
for num in winNums:
    if num in myNums:
        matches.append(num)
score = score + 2 ** (len(matches) - 1)
print(score)
