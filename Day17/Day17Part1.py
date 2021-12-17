def main():
    highesty = 0
    """for i in range(1000):
        y = 0
        yvelocity = i
        for j in range(1000):
            y += yvelocity
            yvelocity -= 1
            if y >= -124 and y <= -69:
                print(i,y)
                break
            if y < -124: break"""

    y = 0
    yvelocity = 123
    for j in range(1000):
        print(y)
        y += yvelocity
        yvelocity -= 1
        if y >= -124 and y <= -69:
            print(y)
            break
        if y < -124: break


if __name__ == "__main__":
    main()
