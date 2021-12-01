def main():
    file = open("AdvDay1Input.txt","r")
    depths = []
    for x in file:
        depths.append(int(x.replace("\n","")))

    count = 0

    def window(d1,d2,d3):
        return d1 + d2 + d3

    windows = []

    for d in range(len(depths)-2):
        windows.append(window(depths[d],depths[d+1],depths[d+2]))

    def compare(d1,d2):
        if d1 < d2:
            return True

    for w in range(len(windows)-1):
        if compare(windows[w],windows[w+1]) == True:
            count += 1

    print(count)

if __name__ == "__main__":
    main()