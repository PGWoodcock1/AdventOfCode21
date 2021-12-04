def main():
    file = open("AdvDay3Input.txt","r")
    input = []
    for x in file:
        input.append(split(x.replace("\n","")))

    O2input = input
    CO2input = input

    #Oxygen Loop

    for x in range(12):
        count = 0
        if len(O2input) == 1:
            break
        for y in range(len(O2input)):
            count += int(O2input[y][x])
        if count < len(O2input)/2:
            O2input = list(filter(lambda z: (z[x] == '0'),O2input))
        else:
            O2input = list(filter(lambda z: (z[x] == '1'),O2input))

    O2Str = '0b'
    O2input = O2input[0]

    for x in range(len(O2input)):
        O2Str += str(O2input[x])

    #CO2 Loop

    for x in range(12):
        count = 0
        if len(CO2input) == 1:
            break
        for y in range(len(CO2input)):
            count += int(CO2input[y][x])
        if count < len(CO2input)/2:
            CO2input = list(filter(lambda z: (z[x] == '1'),CO2input))
        else:
            CO2input = list(filter(lambda z: (z[x] == '0'),CO2input))

    CO2Str = '0b'
    CO2input = CO2input[0]

    for x in range(len(CO2input)):
        CO2Str += str(CO2input[x])

    print(int(O2Str, 2) * int(CO2Str, 2))

def split(string):
    return [char for char in string]

def checkOne(x):
    if x == 1: return True
    else: return False

def checkZero(x):
    if x == 0: return True
    else: return False

if __name__ == "__main__":
    main()