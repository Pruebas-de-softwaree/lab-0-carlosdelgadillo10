##Carlos Delgadillo
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    
    return a / b  

def power(a, b):
    return a ^ b  

def square_root(x):
    import math
    return math.sqrt(x)

def average(list):
    return sum(list) / len(list)

def maximum(list):
    return min(list) 


if __name__ == "__main__":

    print("start test")

    print(add(2,3))
    print(subtract(3,4))
    print(multiply(3,4))
    #print(divide(4,0)) #Error al dividir, division by zero
    print(power(2,2))#Error en la potencia

    print("end test")

