# CONSTRUA UM ALGORITMO QUE LEIA UM NUMERO E EXIBA INFORMAÇÃO SE ESSE NUMERO É OU NÃO DIVISÍVEL POR 5 #

#N1 = 5
#N2 = int(input("Digite um numero: "))

#Soma = N2 % N1

#if Soma == 0:
#    print (f"O número: {N2} é divisível por {N1}")
#else:
#    print (f"O número: {N2} não é divisível por {N1}")

###############################################################

# CONSTRUA UM ALGORITMO QUE LEIA 3 NUMEROS INTEIROS DISTINtOS E EXIBA O MENOR DELES #

#N1 = int(input("Digite o primeiro numero: "))
#N2 = int(input("Digite o segundo numero: "))
#N3 = int(input("Digite o terceiro numero: "))

#if N1 < N2 and N1 < N3: # Primeiro ele procura saber se o N1 é o menor, se for imprime o N1
#    print (N1)
#elif N2 < N3: # Se o N1 não for o menor entre os 3 numeros, portanto só pode ser o N2 ou N3
#    print (N2)
#else:
#    print (N3)

###############################################################

# FAÇA UM ALGORITMO QUE LEIA O VALOR DE SALÁRIO BRUTO DE UM FUNCIONARIO #
# SE O SALÁRIO FOR MENOR OU IGUAL A 500, O ALGORITMO DEVE ATRIBUIR AUMENTO DE 10% #

Salario = int(input("Informe o salário: "))

if Salario <= 500:
    Salario = Salario * 1.10 # O valor 1.10 é o fator de multiplicação de 10%, se fosse 20% seria 1.20.
    print (f"Seu salário atual é: {Salario}")
else: 
    print ("Voce não obteve aumento")
    
    