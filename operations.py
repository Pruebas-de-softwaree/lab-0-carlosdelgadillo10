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
    #print(power(2,2))#Error en la potencia
    #print(square_root(-50)) # Error en la raiz, no hay raices negativas, deberia de impedir la operacion
    #print(average([])) #Error al poner lista vacias, estaria mejor mostrar nulo
    print(maximum([1,2,3,3,4,6])) #Error en el valor esperado, el valor maximo deberia ser 6



    print("end test")

