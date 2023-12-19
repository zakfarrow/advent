def quickSort(data, start, end): 
    if end <= start: return

    pivot = partition(data, start, end)
    quickSort(data, start, pivot - 1)
    quickSort(data, pivot + 1, end)

def partition(data, start, end):

    pivot = data[end]
    i = start - 1

    for j in range(start, end):
        if compare(data[j], pivot):
            i+=1
            temp = data[i]
            data[i] = data[j]
            data[j] = temp
    i+=1
    temp = data[i]
    data[i] = data[end]
    data[end] = temp

    return i

def rankOrder(hands):
    handScore = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    for i in hands:
        temp = cardScore[i[0]]
        handScore[temp].append(i)
    return handScore

def compare(x, y):
    test = False
    for i in range(0, len(x)):
        if cardScore[x[i]] < cardScore[y[i]]:
            test = True
            break
        if cardScore[x[i]] > cardScore[y[i]]:
            test = False
            break
    return test

def getScore(ordered, raw):
    total = 0
    for i in range(0, len(ordered)):
        index = next((j for j in enumerate(raw) if ordered[i] in j[1]),[-1,-1])[0]
        bet = int(raw[index].split(' ')[1])
        total += (i+1)*bet
    return total

def partA(data):
    g5= []
    g4= []
    gfh=[]
    g3= []
    g2p=[]
    gp= []
    gh= []



    for i in data:
        hand = i.split(' ')[0]
        x=0
        for card in cards:
            if hand.count(card) > x:
                x = hand.count(card)
                hcard = card
        if x==1:
            gh.append(hand)
        elif x==2:
            temp = hand
            temp = temp.replace(hcard, '')
            if temp.count(temp[0]) != 3:
                test1 = temp.count(temp[0])
                test2 = temp.count(temp[1])
                if test1 == 2 or test2 == 2:
                    g2p.append(hand)
                else:
                    gp.append(hand)
        elif x==3:
            temp = hand
            temp = temp.replace(hcard, '')
            if temp[0] == temp[1]:
                gfh.append(hand)
            else:
                g3.append(hand)
        elif x==4:
            g4.append(hand)
        elif x==5:
            g5.append(hand)


    fiveOfKind = ['JJJJJ']
    fourOfKind = rankOrder(g4)
    fullHouse = rankOrder(gfh)
    threeOfKind = rankOrder(g3)
    twoPair = rankOrder(g2p)
    onePair = rankOrder(gp)
    highCard = rankOrder(gh)


    for k in fourOfKind:
        quickSort(fourOfKind[k], 0, len(fourOfKind[k]) - 1)
    for k in fullHouse:
        quickSort(fullHouse[k], 0, len(fullHouse[k]) - 1)
    for k in threeOfKind:
        quickSort(threeOfKind[k], 0, len(threeOfKind[k]) - 1)
    for k in twoPair:
        quickSort(twoPair[k], 0, len(twoPair[k]) - 1)
    for k in onePair:
        quickSort(onePair[k], 0, len(onePair[k]) - 1)
    for k in highCard:
        quickSort(highCard[k], 0, len(highCard[k]) - 1)

def finalOrder(fiveOfKind, fourOfKind, fullHouse, threeOfKind, twoPair, onePair, highCard):
    finalArray = []

    for item in highCard:
        for index in highCard[item]:
            finalArray.append(index)
    for item in onePair:
        for index in onePair[item]:
            finalArray.append(index)
    for item in twoPair:
        for index in twoPair[item]:
            finalArray.append(index)
    for item in threeOfKind:
        for index in threeOfKind[item]:
            finalArray.append(index)
    for item in fullHouse:
        for index in fullHouse[item]:
            finalArray.append(index)
    for item in fourOfKind:
        for index in fourOfKind[item]:
            finalArray.append(index)
    for item in fiveOfKind:
        for index in fiveOfKind[item]:
            finalArray.append(index)

    return finalArray

def convertJacks(array):

    fiveofkind = []
    fourofkind = []
    fullhouse = []
    threeofkind = []
    twopair = []
    onepair = []
    highcard = []

    for i in array:
        jokerNum = i.count('J')
        x, cardName = maxCardQty(i)
        total = x + jokerNum
        if total == 5:
            fiveofkind.append(i)
        if total == 4:
            fourofkind.append(i)
        elif total == 3:
            temp = i
            temp = temp.replace(cardName, '')
            temp = temp.replace('J', '')
            if temp[0] == temp[1]:
                fullhouse.append(i)
            else:
                threeofkind.append(i)
        elif total == 2:
            temp = i
            temp = temp.replace(cardName, '')
            if temp.count(temp[0]) != 3:
                test1 = temp.count(temp[0])
                test2 = temp.count(temp[1])
                if test1 == 2 or test2 == 2:
                    twopair.append(i)
                else:
                    onepair.append(i)
        elif total == 1:
            highcard.append(i)

    return fiveofkind, fourofkind, fullhouse, threeofkind, twopair, onepair, highcard

def maxCardQty(hand):
    x=0
    if hand == 'JJJJJ':
        x=0
        hcard = 'J'
    for card in cards:
        if hand.count(card) > x:
            x = hand.count(card)
            hcard = card
    return x, hcard      


def formatData(input):
    hands = []
    bets = []
    for i in input:
        hands.append(i.split(' ')[0])
        bets.append(i.split(' ')[1])
    l0,l1,l2,l3,l4,l5,l6 = convertJacks(hands)
    
    fiveOfKind = rankOrder(l0)
    fourOfKind = rankOrder(l1)
    fullHouse = rankOrder(l2)
    threeOfKind = rankOrder(l3)
    twoPair = rankOrder(l4)
    onePair = rankOrder(l5)
    highCard = rankOrder(l6)

    for j in fiveOfKind:
        quickSort(fiveOfKind[j], 0, len(fiveOfKind[j])-1)
    for j in fourOfKind:
        quickSort(fourOfKind[j], 0, len(fourOfKind[j])-1)
    for j in fullHouse:
        quickSort(fullHouse[j], 0, len(fullHouse[j])-1)
    for j in threeOfKind:
        quickSort(threeOfKind[j], 0, len(threeOfKind[j])-1)
    for j in twoPair:
        quickSort(twoPair[j], 0, len(twoPair[j])-1)
    for j in onePair:
        quickSort(onePair[j], 0, len(onePair[j])-1)
    for j in highCard:
        quickSort(highCard[j], 0, len(highCard[j])-1)

    return fiveOfKind, fourOfKind, fullHouse, threeOfKind, twoPair, onePair, highCard

cardScore = {'J':0,'2':1,'3':2,'4':3,'5':4,'6':5,'7':6,'8':7,'9':8,'T':9,'Q':10,'K':11,'A':12}
handScore = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[],13:[]}
cards = ['2','3','4','5','6','7','8','9','T','Q','K','A']

input = open("data/input7.txt", "r")
data = input.read().split('\n')

arr0, arr1, arr2, arr3, arr4, arr5, arr6 = formatData(data)

finalList = finalOrder(arr0, arr1, arr2, arr3, arr4, arr5, arr6)
count = getScore(finalList, data)

print(count)

input.close()