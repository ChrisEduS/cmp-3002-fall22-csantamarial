def quick_sort(lista):
    '''Sort an array by quick sort method'''
    if len(lista) < 2:
        return lista

    contador = 0 
    for i in range(1, len(lista)): 
        if lista[i] >= lista[0]: ## cambiar a menor que
            contador+= 1
            temp = lista[i]
            lista[i] = lista[contador]
            lista[contador] = temp
              
    temp = lista[0]
    lista[0] = lista[contador] 
    lista[contador] = temp 
    
    izq = quick_sort(lista[0:contador]) 
    der = quick_sort(lista[contador+1:len(lista)])
    
    lista = izq + [lista[contador]] + der 
    
    return lista