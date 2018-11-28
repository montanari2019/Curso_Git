'''19) (Python.org.br) Faça um Programa que peça 2 números inteiros e um número real. Calcule
e mostre:
● o produto do dobro do primeiro com metade do segundo .
● a soma do triplo do primeiro com o terceiro.
● o terceiro elevado ao cubo.
Salve o projeto com o nome “​ 19_calculo_numeros ​ ”.'''

n1=int(input("Digite o primeiro valor inteiro:"))
n2=int(input("Digite o segundo valor inteiro:"))
n3=float(input("Digite o primeiro valor real:"))

print("A =",n1*2*(n2/2))
print("B =",n1*3+n3)
print("C = ",n3**3)