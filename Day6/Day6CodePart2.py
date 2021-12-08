def main():
    #Open file and format as list
    file = list(open("AdvDay6Input", "r"))
    school = file[0].split(',')
    school = list(map(int, school))

# Convert school to dictionary

    SchoolDict = {
        "Zeroes": 0,
        "Ones": 0,
        "Twos": 0,
        "Threes": 0,
        "Fours": 0,
        "Fives": 0,
        "Sixes": 0,
        "Sevens": 0,
        "Eights": 0
    }

    keys = list(SchoolDict)

    for x in range(len(school)):
        for y in range(8):
            if school[x] == y: SchoolDict[keys[y+1]] +=1

    for x in range(257):
        NewFish = SchoolDict[keys[0]]
        for y in range(len(keys)-1):
            SchoolDict[keys[y]] = SchoolDict[keys[y+1]]
        SchoolDict[keys[6]] += NewFish
        SchoolDict[keys[8]] = NewFish
        #print('Day {}: {}'.format(x,SchoolDict))

    print(sum(SchoolDict.values()))

if __name__ == "__main__":
    main()

