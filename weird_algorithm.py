def weird_algorithm (n):
    #se crea una lista con el valor inicial "n"
    ans = [n]
    while n != 1: 
        #evaluamos que n sea par.
        if n % 2 == 0:
            n //= 2
        else:
        #en caso contrario
            n = n * 3 + 1
        ans.append(n)
    return ans
assert weird_algorithm(3) == [3, 10, 5, 16, 8, 4, 2, 1], "Error en el caso de prueba"
print("Caso de prueba esta todo chill :D")