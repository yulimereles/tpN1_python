def number_spiral(Y, X):
    # tenemos que identificar cual de las dos es mayor para saber el limite de la matriz
    if Y > X:
        # al sacar el cuadrado del numero anterior, obtenemos el ultimo valor del area interior.
        ans = (Y - 1) * (Y - 1)
        #verificamos que Y sea par o impar para saber si esta creciendo o decreciendo.
        if Y % 2 != 0:
            add = X
        else:
            add = 2 * Y - X
        return (ans + add)
    else:
        # en caso de que X sea mayor que Y se realizan los mismos calculos pero al contrario. 
        ans = (X - 1) * (X - 1)
        if X % 2 == 0:
            add = Y
        else:
            add = 2 * X - Y
        return (ans + add)

assert number_spiral(2, 2) == 3, "Error en el caso de prueba"
print("En caso de prueba salio todo bien")
