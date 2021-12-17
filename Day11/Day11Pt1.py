def split(string):
    return list(string)


def integer(list):
    return [int(i) for i in list]


def addone(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            list[i][j] += 1


def checkflash(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] > 9: return True


def flash(list,count):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] > 9:
                list[i][j] = -500
                count += 1
                if i == 0:
                    if j == 0:
                        list[i][j + 1] += 1
                        list[i + 1][j] += 1
                        list[i + 1][j + 1] += 1
                    elif j == 9:
                        list[i - 1][j - 1] += 1
                        list[i - 1][j] += 1
                        list[i][j - 1] += 1
                    else:
                        list[i][j - 1] += 1
                        list[i][j + 1] += 1
                        list[i + 1][j - 1] += 1
                        list[i + 1][j] += 1
                        list[i + 1][j + 1] += 1

                elif i == 9:
                    if j == 0:
                        list[i - 1][j] += 1
                        list[i - 1][j + 1] += 1
                        list[i][j + 1] += 1
                    elif j == 9:
                        list[i - 1][j - 1] += 1
                        list[i - 1][j] += 1
                        list[i][j - 1] += 1
                    else:
                        list[i - 1][j - 1] += 1
                        list[i - 1][j] += 1
                        list[i - 1][j + 1] += 1
                        list[i][j - 1] += 1
                        list[i][j + 1] += 1

                elif j == 0:
                    if i == 0:
                        list[i][j + 1] += 1
                        list[i + 1][j] += 1
                        list[i + 1][j + 1] += 1
                    if i == 9:
                        list[i - 1][j] += 1
                        list[i - 1][j + 1] += 1
                        list[i][j + 1] += 1
                    else:
                        list[i - 1][j] += 1
                        list[i - 1][j + 1] += 1
                        list[i][j + 1] += 1
                        list[i + 1][j] += 1
                        list[i + 1][j + 1] += 1

                elif j == 9:
                    if i == 0:
                        list[i][j - 1] += 1
                        list[i + 1][j - 1] += 1
                        list[i + 1][j] += 1
                    if i == 9:
                        list[i - 1][j - 1] += 1
                        list[i - 1][j] += 1
                        list[i][j - 1] += 1
                    else:
                        list[i - 1][j - 1] += 1
                        list[i - 1][j] += 1
                        list[i][j - 1] += 1
                        list[i + 1][j - 1] += 1
                        list[i + 1][j] += 1

                else:
                    list[i-1][j-1] += 1
                    list[i-1][j] += 1
                    list[i-1][j+1] += 1
                    list[i][j-1] += 1
                    list[i][j+1] += 1
                    list[i+1][j-1] += 1
                    list[i+1][j] += 1
                    list[i+1][j+1] += 1
                break
    return count


def resetzero(list):
    for i in range(len(list)):
        for j in range(len(list[i])):
            if list[i][j] < 0:
                list[i][j] = 0


def main():
    #List of lists formatting
    file = list(open("Day11Input", "r"))
    energies = [i.split('\n') for i in file]
    [i.pop() for i in energies]
    energies = [split(i[0]) for i in energies]
    energies = [integer(i) for i in energies]

    flashes = 0

    for x in range(100):
        addone(energies)
        while checkflash(energies) == True:
            flashes += flash(energies,0)
        resetzero(energies)
        print(x, flashes)

if __name__ == "__main__":
    main()
