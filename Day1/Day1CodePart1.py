def main():
    file = open("AdvDay1Input.txt","r")
    depths = []
    for x in file:
        depths.append(int(x.replace("\n","")))

    count = 0

    for d in range(len(depths)-1):
        if compare(depths[d],depths[d+1]) == True:
            count += 1

    print(count)

    def compare(d1,d2):
        if d1 < d2:
            return True

if __name__ == "__main__":
    main()