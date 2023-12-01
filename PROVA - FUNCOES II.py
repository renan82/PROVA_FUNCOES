def inicio():
    print("------------------")
    print("-> INFINITY SCHOOL <-")
    print("* PROVA II: FUNÇÕES *")
    print("ALUNO: RENAN SALES MONTENEGRO")
    print("------------------")

inicio()

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

quadrado = list(map(lambda y: y ** 2, lista_numeros))
print(f"A nova lista com os números elevados ao quadrado é {quadrado}")

numeros_pares = list(filter(lambda y: y % 2 == 0, lista_numeros))
print(f"A nova lista com os números pares é {numeros_pares}")

from functools import reduce

soma_dos_numeros = reduce(lambda x, y: x + y, lista_numeros)
print(f"A soma dos números contidos a lista é {soma_dos_numeros} !")





