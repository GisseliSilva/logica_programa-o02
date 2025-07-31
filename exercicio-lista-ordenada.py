def ordenar_lista(*numeros):
    if not numeros:
        return []
    
    lista_ordenada = sorted(numeros)
    #lista_descrescente = sorted(lista, reverse=True) 
    print(f"Lista ordenada: {lista_ordenada}")

    