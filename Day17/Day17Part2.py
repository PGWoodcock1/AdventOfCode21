def main():

    possiblecombinations = []

    for i in range(1000):
        j = -500
        while j <= 1000:
            j += 1
            xvelocity = i
            yvelocity = j
            x = 0
            y = 0
            for k in range(1000):
                x += xvelocity
                y += yvelocity
                if xvelocity != 0: xvelocity -= 1
                yvelocity -= 1
                if y >= -124 and y <= -69 and x >= 211 and x <= 232:
                    possiblecombinations.append([i,j])
                    break
                if y < -124 or x > 232: break

    print(len(possiblecombinations))

if __name__ == "__main__":
    main()
