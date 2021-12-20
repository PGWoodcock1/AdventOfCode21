def split(string):
    return list(string)

def capture(i,x,y,max_x,max_y,list):
    if i % 2 == 0:
        outer_pixels = '.'
    else:
        outer_pixels = '#'

    if y == 0 and x == 0:
        TL = outer_pixels
        TM = outer_pixels
        TR = outer_pixels
        ML = outer_pixels
        MR = list[y][x+1]
        BL = outer_pixels
        BM = list[y+1][x]
        BR = list[y+1][x+1]
    elif y == max_y and x == 0:
        TL = outer_pixels
        TM = list[y-1][x]
        TR = list[y-1][x+1]
        ML = outer_pixels
        MR = list[y][x + 1]
        BL = outer_pixels
        BM = outer_pixels
        BR = outer_pixels
    elif y == 0 and x == max_x:
        TL = outer_pixels
        TM = outer_pixels
        TR = outer_pixels
        ML = list[y][x-1]
        MR = outer_pixels
        BL = list[y+1][x-1]
        BM = list[y + 1][x]
        BR = outer_pixels
    elif y == max_y and x == max_x:
        TL = list[y-1][x-1]
        TM = list[y - 1][x]
        TR = outer_pixels
        ML = list[y][x-1]
        MR = outer_pixels
        BL = outer_pixels
        BM = outer_pixels
        BR = outer_pixels
    elif y == 0:
        TL = outer_pixels
        TM = outer_pixels
        TR = outer_pixels
        ML = list[y][x - 1]
        MR = list[y][x + 1]
        BL = list[y+1][x-1]
        BM = list[y + 1][x]
        BR = list[y+1][x+1]
    elif y == max_y:
        TL = list[y-1][x-1]
        TM = list[y - 1][x]
        TR = list[y-1][x+1]
        ML = list[y][x - 1]
        MR = list[y][x + 1]
        BL = outer_pixels
        BM = outer_pixels
        BR = outer_pixels
    elif x == 0:
        TL = outer_pixels
        TM = list[y - 1][x]
        TR = list[y - 1][x + 1]
        ML = outer_pixels
        MR = list[y][x + 1]
        BL = outer_pixels
        BM = list[y + 1][x]
        BR = list[y+1][x+1]
    elif x == max_x:
        TL = list[y - 1][x - 1]
        TM = list[y - 1][x]
        TR = outer_pixels
        ML = list[y][x - 1]
        MR = outer_pixels
        BL = list[y+1][x-1]
        BM = list[y + 1][x]
        BR = outer_pixels
    else:
        TL = list[y - 1][x - 1]
        TM = list[y - 1][x]
        TR = list[y - 1][x + 1]
        ML = list[y][x - 1]
        MR = list[y][x + 1]
        BL = list[y + 1][x - 1]
        BM = list[y + 1][x]
        BR = list[y+1][x+1]

    MM = list[y][x]


    output = [TL,TM,TR,ML,MM,MR,BL,BM,BR]
    return output

def convert_to_bin(capture_output):
    output_string = '0b'
    for i in range(len(capture_output)):
        if capture_output[i] == '.':
            output_string += '0'
        else:
            output_string += '1'
    return output_string

def use_algorithm(output_string, algorithm):
    return algorithm[int(output_string,2)]

def main():
    file = list(open("Day20Image", "r"))
    pixels = [i.split('\n') for i in file]
    [i.pop() for i in pixels]
    pixels = [split(i[0]) for i in pixels]

    file = list(open("Day20Algorithm", "r"))
    algorithm = [split(i) for i in file]
    algorithm = algorithm[0]

    input = pixels

    for i in range(50):
        if i % 2 == 0:
            outer_pixels = '.'
        else:
            outer_pixels = '#'

        for j in range(len(input)):
            input[j].insert(0, outer_pixels)
            input[j].insert(0, outer_pixels)
            input[j].append(outer_pixels)
            input[j].append(outer_pixels)

        new_row = []
        for j in range(len(input[0])):
            new_row.append(outer_pixels)
        input.insert(0,new_row)
        input.insert(0, new_row)
        input.append(new_row)
        input.append(new_row)

        output = []
        [output.append([]) for i in range(len(input))]
        for y in range(len(input)):
            for x in range(len(input[0])):
                capture_output = capture(i,x,y,len(input[0])-1,len(input)-1,input)
                output[y].append(use_algorithm(convert_to_bin(capture_output),algorithm))
        input = output

    total = 0
    for i in range(len(input)):
        total += output[i].count('#')

    print(total)

if __name__ == "__main__":
    main()