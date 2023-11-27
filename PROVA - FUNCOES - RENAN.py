# Desenvolva um programa em Python que permita ao usuário digitar várias notas. 
# Em seguida, crie uma função chamada "calcular_media" que irá receber as notas 
# digitadas e calcular a média do aluno. Também crie uma função chamada "verificar_situacao" que, 
# com base na média calculada, irá exibir a situação do aluno: "Reprovado" se a média for menor que 7, 
# "Aprovado" se a média for maior ou igual a 7, e "Parabéns, sua média é 10" se a média for igual a 10.

def media():
    media_total = soma / contador
    return media_total
    
    
def verificar_situacao():
    
    if media() == 10:
        print(f"Média {media()} : PARABÉNS JOVEM, VOCÊ VENCEU!")
    elif media() < 7:
        print(f"Média {media()} : ALUNO REPROVADO!")
    elif media() >= 7:
        print(f"Média {media()} : ALUNO APROVADO!")
    

def inicio():
    print("------------------")
    print("-> INFINITY SCHOOL <-")
    print("* PROVA : FUNÇÕES *")
    print("ALUNO: RENAN SALES MONTENEGRO")
    print("------------------")

contador = 0
soma = 0

inicio()

while True:
    media_total = 0
    nota = float(input("Digite a nota do aluno: "))
    contador = contador + 1
    soma = soma + nota
    
    continuar = str(input("ADICIONAR MAIS UMA NOTA? (s/n) ").upper())
    if continuar == 'N':
        break

print(f"A média do aluno foi: {media()}")

verificar_situacao()
        


