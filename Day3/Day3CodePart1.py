def main():
    file = open("AdvDay3Input.txt","r")
    input = []
    for x in file:
        input.append(x.replace("\n",""))

    sumList = [0,0,0,0,0,0,0,0,0,0,0,0]
    gamma = [0,0,0,0,0,0,0,0,0,0,0,0]
    epsilon = [0,0,0,0,0,0,0,0,0,0,0,0]

    for x in range(len(input)):
      input[x] = split(input[x])
      for y in range(len(input[x])):
          sumList[y] += int(input[x][y])

    for x in range(len(sumList)):
        if sumList[x] < len(input)/2:
            epsilon[x] = 1
        else:
            gamma[x] = 1

    gammaStr = '0b'
    epsilonStr = '0b'

    for x in range(len(gamma)):
        gammaStr += str(gamma[x])

    for x in range(len(epsilon)):
        epsilonStr += str(epsilon[x])

    print(int(gammaStr,2)*int(epsilonStr,2))

def split(string):
    return [char for char in string]

if __name__ == "__main__":
    main()