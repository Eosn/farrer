def ex_1_12_1():
    idade = int(input("Idade: "))
    i = 0
    media = 0
    while (idade != 0):
        i += 1
        media += idade
        idade = int(input("Idade: "))
    media = media/i
    print("Média: %.2f" % (media))
