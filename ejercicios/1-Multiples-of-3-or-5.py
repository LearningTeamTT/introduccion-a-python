# If we list all the natural numbers below 10 that are
# multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

def sum_of_numbers(limit = 10):
    # Inicializo mi variable para ir sumando los números
    result = 0

    # Recorro un ciclo desde el número 0 hasta el "limit - 1"
    for num in range(limit):
        # Compruebo que el número que estoy utilizando es
        # múltiplo de 3 o de 5.
        if num % 3 == 0 or num % 5 == 0:
            # Si el número es múltiplo de 3 o de 5 entonces
            # lo sumo al resultado
            result += num

    # Regreso todos los números sumados que almacené en la variable "result"
    return result

# Imprimo el resultado de ejecutar la función "sum_of_numbers" con el
# valor por default
default = 10
print("Valor default:", default)
print(sum_of_numbers())

# Imprimo el resultado de ejecutar la función "sum_of_numbers" con el
# valor "1000"
limit = 1000
print("Valor:", limit)
print(sum_of_numbers(limit))
