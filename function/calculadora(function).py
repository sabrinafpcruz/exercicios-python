def dividir(A, B):
    divi = A / B
    return divi
def multiplicar(A, B):
    multi = A * B
    return multi
def subtracao(A, B):
    subtra = A - B
    return subtra
def somar(A, B):
    soma = A + B
    return soma

resp=1
while resp> 0 and resp <5:
    print("1-SOMA\n"
          "2-Subtração\n"
          "3-Multiplicação\n"
          "4-Divisão\n"
          "5-Sair")
    resp = int(input("O que deseja fazer: "))
    if resp ==5 :
        break
    else:
        n1 = float(input("Digite um número: "))
        n2 = float(input("Digite outro número: "))

    if resp == 1:
        print(somar(n1, n2))
    elif resp == 2:
        print(subtracao(n1, n2))
    elif resp == 3:
        print(multiplicar(n1, n2))
    elif resp == 4:
        print(dividir(n1, n2))
