NumeroInserido = str(input("Insira um Numero em Romano:"))

NRomanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
}

total = 0

for Indice in range(len(NumeroInserido)):
    valor = NRomanos[NumeroInserido[Indice]]

    if Indice < len(NumeroInserido) - 1:
        proximo_valor = NRomanos[NumeroInserido[Indice + 1]]

        if valor < proximo_valor:
            total -= valor
        else:
            total += valor
    else:
        total += valor

print("Resultado:", total)