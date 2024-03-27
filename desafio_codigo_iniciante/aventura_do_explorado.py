"""
Desafio

Você é um intrépido explorador em uma jornada por uma terra desconhecida repleta de desafios emocionantes.
Ao se deparar com uma floresta misteriosa, você percebe que a única maneira de atravessá-la é 
desvendando seus caminhos por meio de um código em Python.
Prepare-se para a "Aventura do Explorador"!

Entrada
Seu programa deve solicitar ao usuário a entrada de um número inteiro positivo,
representando a quantidade de passos que o explorador deve dar na floresta.

Saída
O programa deve imprimir uma mensagem indicando o progresso do explorador na floresta.
Utilize um laço de repetição para simular os passos do explorador.
A cada passo, imprima uma mensagem informando a distância percorrida até o momento.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas.
Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

| ENTRADA |             SAIDA             |
|---------|-------------------------------|
|    2    | Explorador: 1 passo           |
|         | Explorador: 2 passos          |
|---------|-------------------------------|
|    3    | Explorador: 1 passo           |
|         | Explorador: 2 passos          |
|         | Explorador: 3 passos          |
|---------|-------------------------------|
|    0    | Nenhum passo dado na floresta.|

"""

# Desafio: A Aventura do Explorador

#TODO: Adicione uma condição para verificar se a quantidade de passos é positiva.
#Se a quantidade de passos for zero, imprima "Nenhum passo dado na floresta."
#Caso contrário, utilize um loop for para imprimir a mensagem do explorador, indicando o número do passo.

#Esta linha cria uma lista vazia chamada que será usada para armazenar os passos dados pelo explorador.
from  typing import List

list_of_steps: List[int] = []

def check_positive_number(number: int) -> bool:
    """Verifica se o número fornecido é positivo.

    Args:
        number (int): Número que vai ser verificado.

    Returns:
        bool: True se o número for positivo, False se for negativo.
    """
    if number < 0:
        print("Digite um número positivo")
        return False
    else:
        return True

def number_of_steps() -> None:
    """Recebe a quantidade de passos dados e imprime a quantidade para o usuário"""
    quantidade_passos = int(input())
    if quantidade_passos == 0:
        if not list_of_steps:
            print("Nenhum passo dado na floresta.")

    elif check_positive_number(quantidade_passos):
        list_of_steps.append(quantidade_passos)
        for i in range(1, quantidade_passos + 1):
            if i == 1:
                print(f"Explorador: {i} passo")
            else:
                print(f"Explorador: {i} passos")

number_of_steps()
