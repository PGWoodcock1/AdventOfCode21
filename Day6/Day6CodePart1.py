def main():
    file = list(open("AdvDay6Input", "r"))
    school = file[0].split(',')
    school = list(map(int, school))

    print(len(school))

    for x in range(256):
        for y in range(len(school)):
            school[y] -= 1
        for y in range(len(school)):
            if school[y] == -1:
                school[y] = 6
                school.append(8)

    print(len(school))

if __name__ == "__main__":
    main()

