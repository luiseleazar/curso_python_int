def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "Eleazar", "lastname":"Nunez"}

    super_list = [
        {"firstname": "Eleazar", "lastname":"Nunez"},
        {"firstname": "Eduardo", "lastname":"Benitez"},
        {"firstname": "Carlos", "lastname":"Reyna"},
        {"firstname": "Jared", "lastname":"Barreto"}
    ]

    super_dict = {
        "natural_nums":[1, 2, 3, 4, 5],
        "int_nums":[-1, -2, 0, 1, 2],
        "float_nums":[1.1, 2.2, 3.3, 4.4]
    }

    for i in super_list:
        print(i)

if __name__ == '__main__':
    run()