def main():
    #List of lists formatting
    file = list(open("Day9Input", "r"))
    heights = [i.split('\n') for i in file]
    [i.pop() for i in heights]
    heights = [split(i[0]) for i in heights]
    heights = [integer(i) for i in heights]

    TotalRisk = 0

    for x in range(len(heights)):
        for y in range(len(heights[x])):
            if testLR(heights[x],y) != True: continue
            if testUD(heights,y,x) == True:
                TotalRisk += (heights[x][y] + 1)

    print(TotalRisk)

def testLR(list,indexInList):
    if indexInList == 0:
        return list[indexInList] < list[indexInList+1]
    elif indexInList == len(list)-1:
        return list[indexInList] < list[indexInList-1]
    else:
        return list[indexInList] < list[indexInList-1] and list[indexInList] < list[indexInList+1]

def testUD(list,indexInList,indexOfList):
    if indexOfList == 0:
        return list[indexOfList][indexInList] < list[indexOfList+1][indexInList]
    elif indexOfList == len(list)-1:
        return list[indexOfList][indexInList] < list[indexOfList-1][indexInList]
    else:
        return list[indexOfList][indexInList] < list[indexOfList+1][indexInList] and list[indexOfList][indexInList] < list[indexOfList-1][indexInList]

def split(string):
    return list(string)

def integer(list):
    return [int(i) for i in list]

if __name__ == "__main__":
    main()