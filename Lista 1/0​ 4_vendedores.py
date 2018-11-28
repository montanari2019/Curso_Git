#4) (BACKES, 2012) Escreva um programa de ajuda para vendedores. A partir de um valor total
#lido, mostre:
#● o total a pagar com desconto de 10%;
# o valor de cada parcela, no parcelamento de 3× sem juros;
#● a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com
#desconto);
#● a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total) ;
#Salve o projeto com o nome “0​ 4_vendedores ” ​ .

valor=float(input("Digite o valor total da venda:"))
desconto= valor-(valor*0.1)
print("Valor Total R$",valor,"\n-----------------------\n")
print("Se for a vista fica R$",desconto,"Com 10% de desconto")
print("Valor da Parcela R$",round((valor/3),2))
print("Comissao do vendedor a vista R$",desconto*0.05)
print("Comissao do vendedor a prazo R$",valor*0.05)