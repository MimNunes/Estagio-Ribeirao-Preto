def verificar_letra_a(texto):
    # Conta o número de ocorrências de 'a' e 'A'
    quantidade_a = texto.count('a') + texto.count('A')

    # Verifica a existência da letra 'a' e exibe o resultado
    if quantidade_a > 0:
        print(f"A letra 'a' aparece {quantidade_a} vezes na string.")
    else:
        print("A letra 'a' não está presente na string.")

# String a ser verificada
texto = input("Informe uma string para verificar a existência da letra 'a': ")

# Chama a função para verificar e contar a letra 'a'
verificar_letra_a(texto)