# Verifica quantas vezes aparece uma letra em um texto e em que posição a primeira letra "A" aparece.
# A função "rfind()" procura a ultima letra "a", pois lê da direita para a esquerda.

frase = input("Digite uma frase:").lower()
print("A letra A aparece {} vezes na frase.".format(frase.count("a")))
print("A primeira letra A aparece na posição {}.".format(frase.find("a")))
print("A ultima letra A aparece na posição {}".format(frase.rfinf("a")))
