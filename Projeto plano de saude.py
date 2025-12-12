print("Bem vindo ao meu trabalho,Filipi Buffalo")
valor_base = float(input("informe o valor do plano")) #Aqui foram feitos inputs refenre idade e valor usando booleanos
idade = int(input("informe sua idade"))
def calcular_valor_mensal(idade,valor_base,percentual) : #aqui criei uma funçao para calcular o valor mensal
    valor_mensal = valor_base * percentual
    return valor_mensal
if idade >= 0 and idade <= 19 :
   valor_mensal = valor_base * 1.00         #aqui montei o bloco de codigos 
elif idade >= 19 and idade <= 29 :
    valor_mensal = valor_base * 1.50
elif idade >= 29 and idade <= 39 :
    valor_mensal = valor_base * 2.25
elif idade >= 39 and idade <= 49 :
    valor_mensal = valor_base * 2.40
elif idade >= 49 and idade <= 59 :
    valor_mensal = valor_base * 3.50
else :
    idade >= 59 
    valor_mensal = valor_base *6.00

print(valor_mensal)      #aqui esta o print de resultado final


