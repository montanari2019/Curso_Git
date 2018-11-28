'''15) (LIVI & EDELWEISS, 2014) Construa um programa que calcule e informe o consumo médio
de combustível de um automóvel. Considere que o tanque é totalmente cheio em cada
abastecimento. O programa deve receber, como entradas, a capacidade do tanque, a
quantidade de litros abastecidos e a quilometragem percorrida desde o último abastecimento.
Salve o projeto com o nome “​ 15_consumo_combustivel ” ​ .'''

capacidade = float(input("Digite a capacidade do Tanque:"))
km =float(input("Digite o km rodado:"))
litros = float(input("Digite a litragem do tanque:"))

print("Consumo medio:",km/(capacidade-litros))