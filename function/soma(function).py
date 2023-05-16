def somar_(*numeros):
    soma=0
    for a in numeros:
        soma+=a
    return soma

from funcoes import somar_
print(somar_(30,10,3,4))