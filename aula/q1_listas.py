#Declaracao da lista
list_elem = []

#Lendo o tamanho da lista
n = int(input())

#Lendo e adicionando elementos na lista
for i in range (0,n):
    var = int(input())
    list_elem.append(var)

#Descobrindo o elemento de maior valor
max_elem = max(list_elem)

#Multiplicando cada elemento da lista pelo elemnto de maior valor
for i in range (0,n):
    num = list_elem[i] * max_elem
    list_elem.append(num)

#Ordenando a lista
list_elem.sort()


#Retirando elementos da lista:

#Retirando elemento da posicao n
list_elem.pop(n)
#Retirando elemento da posicao 0
list_elem.pop(0)
#Retirando elemento da ultima posicao
list_elem.pop()


print(list_elem)
