# Incomplete solution

# Program to read the entire file using read() function
input = open("data/input1.txt", "r")
data = input.read().split('\n')

nums = {
    1:['one','1'],
    2:['two','2'],
    3:['three','3'],
    4:['four','4'],
    5:['five','5'],
    6:['six','6'],
    7:['seven','7'],
    8:['eight','8'],
    9:['nine','9']
}
count = 0
for i in data:
    lindex = len(data)
    hindex = len(data)
    for j in nums:
        for k in nums[j]:
            rev = i[::-1]
            temp = i.find(k)
            revk = k[::-1]
            revtemp = rev.find(revk)            
            if temp != -1:
                if temp < lindex: 
                    lindex = temp
                    l = j
            if revtemp != -1:
                if revtemp < hindex:
                    hindex = revtemp
                    h = j
    count += int(str(l) + str(h))

print(count)        

                
input.close()