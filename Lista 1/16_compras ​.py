'''16) (LIVI & EDELWEISS, 2014) Construa um programa que receba os valores (em reais) que
cinco clientes pagaram por suas compras. O programa deverá informar o valor da compra
média efetuada. Salve o projeto com o nome “​ 16_compras ​ ”.'''

soma=0

for i in range(5):
    compra=float(input("Digite o valor da "+str(i+1)+" compra:"))
    soma+=compra

print("Media do valor:",soma/5)