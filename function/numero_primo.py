def n_primo(a):
    if a ==1:
        return "Não é primo"
    if a ==2:
        return "primo"
    if a%a==1 and  a%1==a:
            return "primo"
    else:
        return "Não é primo Primo"

n=int(input("Digite um numero: "))
from funcoes import n_primo
print(n_primo(n))