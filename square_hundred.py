def run():
    square_list = []
    square_not_three = []

    for i in range (1, 101):
        square_list.append(i**2)

    for i in range (1, 101):
        if i % 3 == 0:
            continue
        square_not_three.append(i**2)   

    #for num in square_list:
    #    print(num)
    #print(square_list)
    print(square_not_three)


if __name__ == '__main__':
    run()