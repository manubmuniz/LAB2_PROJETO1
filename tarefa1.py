import random

def cumprimento(texto):
    return f"Olá, {texto}"

# Chamar a função com seu nome completo
resultado = cumprimento("Manuela Belem Muniz")
print(resultado)

def calcular_media():
    numeros = [random.randint(1, 100) for _ in range(3)]  # Sorteia 3 números entre 1 e 100
    media = sum(numeros) / len(numeros)
    print(f"Números sorteados: {numeros}")
    return media

# Chamar a função para calcular a média e exibir o resultado
media = calcular_media()
print(f"A média dos 3 números sorteados é: {media}")