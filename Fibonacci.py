def is_fibonacci(number):
    # Inicializa os primeiros valores da sequência de Fibonacci
    fib1, fib2 = 0, 1

    # Verifica se o número é 0 ou 1, que sempre pertencem à sequência
    if number == fib1 or number == fib2:
        return True

    # Gera a sequência até o valor desejado
    while fib2 < number:
        fib1, fib2 = fib2, fib1 + fib2

    # Se o último valor calculado é igual ao número, ele pertence à sequência
    return fib2 == number

# Número a ser verificado
number = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

# Verifica se o número pertence à sequência e imprime o resultado
if is_fibonacci(number):
    print(f"O número {number} pertence à sequência de Fibonacci.")
else:
    print(f"O número {number} NÃO pertence à sequência de Fibonacci.")