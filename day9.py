def findNext(currSeq):
    nextSeq = []
    for i in range(len(currSeq)-1):
        nextSeq.append(currSeq[i+1] - currSeq[i])
    if any(currSeq):
        return currSeq[-1] + findNext(nextSeq)
    else:
        return currSeq[-1]
    

def findDiff(x, y):
    return x - y

def formatData(input, opt):
    ans = 0
    input = input
    for i in input:
        arr = i.split(' ')
        if opt == 'partB':
            arr.reverse()
        ans+=findNext(list(map(int, arr)))

    print(ans)



input = open("data/input9.txt", "r")
data = input.read().split('\n')
formatData(data, 'partA')
