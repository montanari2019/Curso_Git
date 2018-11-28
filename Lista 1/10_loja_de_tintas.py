'''10) (Python.org.br) Faça um Programa para uma loja de tintas. O programa deverá pedir o
tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de
1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam
R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00. Informe ao usuário as quantidades
de tinta a serem compradas e os respectivos preços em 3 situações:
● comprar apenas latas de 18 litros;
● comprar apenas galões de 3,6 litros;
● misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
Salve o projeto com o nome “​ 10_loja_de_tintas ​ ”.'''

tamanho = float(input("Digite o tamanho da area a ser pintada em m²"))

tinta =1/6*tamanho
tinta_compra = tinta

lata18=0
lata3=0

while tinta_compra > 0:
    tinta_compra-=18
    lata18+=1
    print("Quantidade de latas de 18l:%d \tPreço: R$%.2f" % (lata18,lata18*80.00))

tinta_compra = tinta

while tinta_compra > 0:
    tinta_compra-=3.6
    lata3+1
    print("Quantidade de latas de 3.6l:%d\tPreço: R$.2f" % (lata3,lata3*25))

tinta_compra = tinta
lata3=0
lata18=0

while tinta_compra>17.9:
    tinta_compra-=18
    lata18+=1
while tinta_compra>0:
    tinta_compra-=3.6
    lata3+=1
print("Quantidade de latas de 18l:%d \nQuantidade de latas de 3.6l:%d\nPreço Total:R$%2f" % (lata18,lata3,(lata18*80+lata3*25)))
