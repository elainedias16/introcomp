import math

n = float(input("Digite um número:\n"))

#raiz = math.sqrt(n)
raiz = n ** (1/2) 
raiz_aux = int(math.sqrt(n))


if( raiz == raiz_aux):
    print('É um quadrado perfeito.\n' )
else:
    print('Não é um quadrado perfeito\n')