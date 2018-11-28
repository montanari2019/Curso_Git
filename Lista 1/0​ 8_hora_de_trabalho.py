'''8) (BACKES, 2012) Faça um programa que leia o valor da hora de trabalho (em reais) e
número de horas trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando
10% sobre o valor calculado. Salve o projeto com o nome “0​ 8_hora_de_trabalho ​ ”.'''

preco_hora=float(input("Digite o Valor da hora trabalhada:"))
horas=float(input("Digite a Quantidade de horas trabalhadas:"))
salario = (preco_hora*horas)
salario = salario+(salario*0.1)
print("Salário: R$",salario)