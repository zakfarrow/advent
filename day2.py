import re
def getDict(rawData):
    dic = {}
    for item in rawData:
        gameNum = getGameId(item)
        dic[gameNum] = sortGames(item, len(gameNum) + 2)
    return dic

def getGameId(entry):
    gameId = str(entry.split(': ').pop(0)).strip("[]").strip("'")
    return gameId

def sortGames(gameData, index):
    gameData = gameData[index:].split("; ")
    for i in range(0, len(gameData)):
        x = gameData[i].split(", ")
        gameData[i] = x
    return gameData

def maxColors(data):
    cubes = []
    for i in range(1, 101):
        colorNums = {'r':0, 'g':0, 'b':0}
        id = "Game" + " " + str(i)
        for j in range(0, len(data[id])):
            for k in range(0, len(data[id][j])):
                x = data[id][j][k]
                num = int(re.sub('\D', '', x))
                color = re.sub('\d', '', x)[1]
                if num > colorNums[color]:
                    colorNums[color] = num
        gameRes = colorNums['r'] * colorNums['g'] * colorNums['b']
        cubes.append(gameRes)
    return cubes

def finalCount(data):
    total = 0
    for item in data:
        total += int(re.sub('\D', '', item))
    return total

def removeImpossible(cleanData):
    for i in range(1, 101):
        id = "Game" + " " + str(i)
        for j in range(0, len(cleanData[id])):
            if id in cleanData:
                for k in range(0, len(cleanData[id][j])):
                    if id in cleanData:
                        x = cleanData[id][j][k]
                        num = re.sub('\D', '', x)
                        color = re.sub('\d', '', x)[1]
                        if int(num) > colorLim[color]:
                            cleanData.pop(id)

input = open("data/input2.txt", "r")
data = input.read().split('\n')

# ------  Part A  ------
colorLim = {'r':12,'g':13,'b':14}
formatData = getDict(data)
possibleData = removeImpossible(formatData)
answer1 = finalCount(possibleData)


# ------  Part B  ------
answer2 = sum(maxColors(formatData))

input.close()