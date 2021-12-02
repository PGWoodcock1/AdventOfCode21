def main():
    file = open("AdvDay2Input.txt","r")
    instructions = []
    for x in file:
        instructions.append(x.replace("\n",""))

    xcoord = 0
    ycoord = 0
    aim = 0

    for instruction in instructions:
        direction = instruction[0]
        magnitude = int(instruction[-1])
        if direction == 'u':
            aim -= magnitude
        elif direction == 'd':
            aim += magnitude
        else:
            xcoord += magnitude
            ycoord += magnitude * aim

    print(xcoord * ycoord)

if __name__ == "__main__":
    main()