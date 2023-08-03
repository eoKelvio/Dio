def contar_vogais(texto):
    vogais= "aeiouAEIOU"
    contador = 0
    for letra in texto:
        if letra in vogais:
            contador += 1
    return contador

frase = "Ola, tudo bem?"
print (contar_vogais(frase))
