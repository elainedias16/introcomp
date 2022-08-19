n = int(input())


def line_x(x):
    for i in range(1, x+1):
        print(i , end=" ")

def triangulo_retangulo(n):
    for i in range(1 , n+1):
        line_x(i)
        print()


triangulo_retangulo(n)
# print()




