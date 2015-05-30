#Insertion Sort
stringToBeSorted = "INSERTIONSORT"
strList = list(stringToBeSorted)
strLength = len(strList)
print ''.join(strList)

def swap( a , b ):
    t = strList[a]
    strList[a] = strList[b]
    strList[b] = t
    return

for i in range(1,strLength):
    j = i
    while ((j > 0) and (strList[j] < strList[j-1])):
        swap(a = j,b = j-1)
        j = j-1

    print ''.join(strList)


    
