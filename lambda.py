def run():
    my_list = [1, 2, 3, 4, 5]

    #filter
    odd = list(filter(lambda x: x%2 != 0, my_list))
    
    print(odd)

    #map
    square = list(map(lambda i : i**2, my_list))

    print(square)

    #reduce
    from functools import reduce

    multi = 1

    multi = reduce(lambda a,b : a * b, my_list)

    print(multi)

if __name__ == '__main__':
    run()