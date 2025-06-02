def potencia (valor,exponente):
    return valor ** exponente

r = potencia(2,4)
print(r)


def sumatoria(*numeros):
    sum_total = 0
    for n in numeros:
        sum_total+=n
    return sum_total

print(sumatoria(1,2,3,4,5,6,7,8,9,10))


def area (base,altura):
    return (base*altura)/2
print(area(5,3))


sumatoria = lambda x,y: x+y
print(sumatoria(2,2))
cuadrado = lambda base,exponente : base **exponente
print(cuadrado(2,3))
filtrado = lambda lista:list(filter(lambda x:x%2==0, [1, 2, 3, 4, 5]))
print(filtrado([1,2,3,4,5,6,7,8,9,10]))

mayuscula =lambda lista:list(map(lambda x: x.upper(),lista))
nombre =["hola", "mundo", "python"]
print(mayuscula(nombre))
tuplas =[('a', 3), ('b', 1), ('c', 2)]
orden = sorted(tuplas ,key=lambda x:x[0])
print(orden)

nombre =["hola", "mundo", "python"]
mayusculas =list(map(lambda x: x.upper(),nombre))
print(mayusculas)