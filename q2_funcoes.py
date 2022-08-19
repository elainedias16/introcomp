l1 = int(input())
l2 = int(input())
l3 = int(input())

def eh_triangulo(l1, l2, l3):
    if(l1 < l2+l3 and l2 < l1+l3 and l3 <l1+l2 ):
        tipo_triangulo(l1, l2, l3)
    else:
        print("Não é um triângulo")
   

def tipo_triangulo(l1, l2, l3):
    if(l1 == l2 and l2 ==l3):
        print("É um triângulo equilátero")
    elif(l1 != l2 and l2!= l3 and l1!= l3):
        print("É um triângulo escaleno")
    else:
       print("É um triângulo isósceles") 


eh_triangulo(l1, l2, l3)