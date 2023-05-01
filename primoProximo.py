'''
    Checkpoint 2 - Python
    Nome: Leticia Cristina Gandarez Resina
    RM: 98069
'''

# Função que verifica se o número é primo ou não


def verificaPrimo(numero):
    for i in range(2, numero):
        if (numero % i == 0):
            # Pois, caso o número divida por qualquer um sem ser ele mesmo, retornará False.
            return False
    return True

# Função que vai verificar o número primo mais próximo caso não seja primo


def verificaPrimoProximo(numero):
    numeroMenor = numero - 1  # Vai achar o número menor que o número informado
    numeroMaior = numero + 1  # Vai achar o número maior que o número informado
    while True:
        if verificaPrimo(numeroMenor):
            # Se o menor número passar pela função de verificar se é primo, se sim, retorna ele!
            return numeroMenor
        # Caso o menor número não for primo...
        elif verificaPrimo(numeroMaior):
            # vai verificar se o número maior é primo, retornando ele caso seja primo
            return numeroMaior
        else:
            # Se nenhum dos casos acima for primo, ele vai tirar novamente para tentar encontrar o número primo mais próximo
            numeroMenor -= 1
            numeroMaior += 1


while True:
    num = int(input("Informe um número de 1 a 1000: "))
    if (num >= 1 and num <= 1000):
        verificaPrimo(num)
        if verificaPrimo(num) == True and num != 1:
            print(f"O número {num} é primo")
        elif verificaPrimo(num) == False:
            primoProximo = verificaPrimoProximo(num)
            print(f"O primo mais próximo de {num} é {primoProximo}")
        elif num == 1:
            print(f"O número {num} é um caso especial. Ele não é nem primo, nem composto.")
            print(f"Neste caso, o primo mais próximo dele é 2.")
    elif num == 0:
        print("Finalizando a execução...")
        break
    else:
        print("Valor inválido.")