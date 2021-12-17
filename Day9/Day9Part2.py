def measureRL(list,startingX):
    i = startingX
    while i < len(list) and list[i] != 9:
        list[i] = 'X'
        i += 1
    j = startingX
    while j > 0 and list[j] != 9:
        list[j] = 'X'
        j -= 1
        i += 1
    return i

def measureBasin(listofLists,startingX,startingY)
    k = startingY
    while k < len(listofLists) and listofLists[startingY][startingX]:
        measureRL(listofLists[k],startingX)
        k += 1


def split(string):
    return list(string)

def integer(list):
    return [int(i) for i in list]

def main():
    #List of lists formatting
    file = list(open("Day9Input", "r"))
    heights = [i.split('\n') for i in file]
    [i.pop() for i in heights]
    heights = [split(i[0]) for i in heights]
    h = [integer(i) for i in heights]

    dontMeasure = ['X',9]
    basinSizes = []

    for y in range(len(h)):
        for x in range(len(h[y])):
            if h[y][x] in dontMeasure: continue
            else:
                meausureRL(h(y),x)

if __name__ == "__main__":
    main()