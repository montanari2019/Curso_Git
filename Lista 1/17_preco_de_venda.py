'''17) (LIVI & EDELWEISS, 2014) Um produto comprado por um consumidor tem um preço
composto pelo seu preço de custo (preço que a loja paga para a fábrica) adicionado de um
percentual de lucro para a loja, além de um percentual de impostos que a loja deve pagar.
Supondo que o percentual de lucro seja de 28% do preço de custo e que os impostos sejam de
25% sobre o preço de custo, escreva um algoritmo que calcule o preço que um consumidor
deve pagar. O algoritmo deve receber somente o preço de custo de um produto. Salve o
projeto com o nome “​ 17_preco_de_venda ” ​ .'''

preco_custo=float(input("Digite o preço de custo:"))

lucro=preco_custo*0.28
impostos=preco_custo*0.25

print("Valor Total do produto:",preco_custo+lucro+impostos)