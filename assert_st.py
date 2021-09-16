def divisors(num):   
    divisors = []
    for i in range(1,num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors
   
    

def run():
    num = input("ingresa un numero: ")
    assert num.isnumeric() and num > 0, "Ingresa un número positivo"
    print(divisors(int(num))) 
    print("terminó el programa")
    

if __name__ == '__main__':
    run()