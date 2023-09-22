"""
programa que contabiliza vogais e encerra com enter 2x
versao python: 3.11.4
"""

#Cria um texto vazio
texto = ""
linha = input("Digite uma linha (ou ENTER para encerrar):\n")

while linha != "":
# adiciona linha ao texto
    texto = texto + linha + "\n"
# input para que o se deixar a linha vazia possa quebra o loop
    linha = input("")

#Loop para contar as vogais
contadorVogais = 0
for letra in texto:
    if letra.lower() in "aeiouáâéêíîóôúû":
        contadorVogais += 1

print(f"O texto digitado contém {contadorVogais} vogais!")
print("")
print(texto)