
def run():
    #squares = [i**2 for i in range(1, 101) if i % 3 != 0]

    #print(squares)

    squares = [i for i in range(1, 9999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    #Minimum common multiple (36)
    #squares = [i for i in range(1, 9999) if i % 36 == 0]

    print(squares)


if __name__ == '__main__':
    run()