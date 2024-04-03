def missing_number(n, l):
        if 0 in l:
            raise ValueError("La lista no puede contener cero.")
        #utilizamos range para crear la lista completa y sumamos los valores de ambas listas, la diferencia entre estos es el numero faltante
        return sum(range(1, n+1)) - sum(l)

assert missing_number(5, [1, 2, 4, 5]) == 3, "Error en el caso de prueba"
assert missing_number((0),[1, 2, 4, 5]) ==0, "Error en el caso de prueba"
print("Caso de prueba pasado correctamente")
