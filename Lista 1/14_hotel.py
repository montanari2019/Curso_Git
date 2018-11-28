'''14) (LIVI & EDELWEISS, 2014) Um hotel com 75 apartamentos deseja fazer uma promoção
especial de final de semana, concedendo um desconto de 25& na diária. Com isso, espera
aumentar sua taxa de ocupação de 50 para 80%. Sendo dado o valor normal da diária, calcule
e imprima:
a) O valor da diária promocional;
b) O valor total arrecadado com 80% de ocupação e diária promocional;
c) O valor total arrecadado com 50% de ocupação e diária normal;
d) A diferença entre esses dois valores;
Salve o projeto com o nome “​ 14_hotel . ​'''

diaria=float(input("Digite o valor da diaria:"))
valor_promocao = int(75*0.8)*(diaria-(diaria*0.25))
valor_normal=int(75*0.5)*diaria

print("Valor da diaria: R$",diaria)
print("valor total arrecadado com diaria promocional: R$",valor_promocao)
print("valor total arrecadado com diaria normal: R$",valor_normal)
print("A diferença da promocial para a normal:",valor_promocao-valor_normal)
