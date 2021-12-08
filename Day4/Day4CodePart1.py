#Function to test called number against numbers on board and mark the number

def markOff(Board,CalledNumber):
    for x in range(len(Board)):
        for y in range(len(Board[x])):
            if Board[x][y] == CalledNumber: Board[x][y] = 'X'

#Function to map 'rows' board to 'columns' board

def createColumnsBoard(Board):
    ColumnsBoard = []
    for x in range(len(Board)):
        newArray = []
        for y in range(len(Board[x])):
            newArray += [Board[y][x]]
        ColumnsBoard += [newArray]
    return ColumnsBoard

#Function to test if board has won

def testWin(Board):
    createColumnsBoard(Board)
    if ['X','X','X','X','X'] in Board or ColumnsBoard: print('Win')
    else: print('No')

#Function to calculate the winning score


def main():

    #Format input

    file = list(open("AdvDay4CalledNumbers", "r"))
    CalledNumbers = file[0].split(',')

    file = open("AdvDay4Boards", "r")
    Boards = [i.split('\n') for i in file]
    [i.pop() for i in Boards]
    for x in range(len(Boards)):
        Boards[x] = Boards[x][0].split()

    BoardsEdited = []

    for x in range(0,len(Boards),6):
        BoardsEdited += [[Boards[x]] + [Boards[x+1]] + [Boards[x+2]] + [Boards[x+3]] + [Boards[x+4]]]

    #print(CalledNumbers)
    #print(Boards)
    #print(BoardsEdited[0])

    #print(BoardsEdited[0])
    #createColumnsBoard(BoardsEdited[0])
    #print(ColumnsBoard)

    #Run through boards, marking off numbers as they're called until the board wins
    #(or passes numbers called for current winner)
    #calculate the winning score and store


    for x in range(len(BoardsEdited)):
        WinningCall = ''
        for y in range(len(CalledNumbers)):
            if CalledNumbers[y] == WinningCall: break
            else:
                markOff(BoardsEdited[x],CalledNumbers[y])
                testWin(BoardsEdited[x])
        print(WinningCall)

if __name__ == "__main__":
    main()