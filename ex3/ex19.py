# ex19 (✿◠ᴗ◠)

primeiro_numero = 1
segundo_numero = 1
contador = 0

while contador < 60:

    print(primeiro_numero)  # mostra numero atual

    proximo_numero = primeiro_numero + segundo_numero  # soma dos dois anteriores
    primeiro_numero = segundo_numero  # atualiza primeiro
    segundo_numero = proximo_numero   # atualiza segundo

    contador = contador + 1