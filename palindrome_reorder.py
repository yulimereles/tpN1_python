def palindrome_reorder(string):
    #  Cuenta la cantidad de cada carácter en la cadena
    conteo_caracteres = {}
    for char in string:
        conteo_caracteres[char] = conteo_caracteres.get(char, 0) + 1

    conteo_impares = 0
    caracter_impar = ''
    palindrome = []
    
    # Construye  la mitad del palíndromo
    for char, count in conteo_caracteres.items():
        if count % 2 != 0:
            conteo_impares += 1
            caracter_impar = char
        palindrome.extend([char] * (count // 2))
    
    # Se verifica si hay más de un carácter impar
    if conteo_impares > 1:
        return "NO SOLUTION"
    
    # Para unir la mitad del palíndromo en una cadena
    palindrome = ''.join(palindrome)
    
    # Se construye el palíndromo reordenado
    return palindrome + caracter_impar + palindrome[::-1]

assert palindrome_reorder("aabbc") == "abcba", "Error en el caso de prueba"
print("En caso de prueba salio todo de chill :)")
