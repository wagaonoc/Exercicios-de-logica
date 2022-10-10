# CRIE UM ALGORITMO PRA EXIBIR OS NUMEROS DE 1 A 10

#Cont = 1
#while (Cont <= 10):
#    print (Cont)
#    Cont = Cont + 1

#########################################################################
    
# CRIE UM ALGORITMO PARA EXIBIR OS NUMEROS E 1 A 10 EM ORDEM DECRESCENTE

#Cont = 10
#while (Cont >=1):
#    print (Cont)
#    Cont = Cont - 1

#########################################################################

# CRIE UM EXERCICIO PARA EXIBIR A TABUADA DE 7

#Resultado = 0
#Cont = 0
#N = int(input("Digite um numero para exibir a tabuada: "))

#########################################################################

#while (Cont <=10):
#    Resultado = N * Cont
#    print (f"{N} x {Cont} = {Resultado}")
#    Cont = Cont + 1
           
#########################################################################
           
# CRIE UM ALGORITMO ONDE O USUARIO VAI INFORMAR UM NUMERO ENTRE 1 E 100, E O SISTEMA DEVE MOSTRAR 
# TODOS OS NUMEROS SEQUENCIAIS DE 0 ATÉ O NUMERO INFORMADO

#N = int(input("Digite um numero: "))
#Cont = 0

#while (Cont <= N):
#    print (Cont)
#    Cont = Cont + 1

#########################################################################

# CRIE UM ALGORITMO ONDE O USUARIO VAI INFORMAR O NUMERO FINAL E O MULTIPLICADOR
# O SISTEMA DEVE MOSTRAR DE 0 ATÉ O NUMERO FINAL, SOMANDO O MULTIPLICADOR

#N = int(input("Informe um numero: "))
#MULT = int(input("Digite o multiplicador: "))
#Cont = 0
           
#while (Cont <= N):
#    print (Cont)
#    Cont = Cont + MULT
    
#########################################################################

# CRIE UM ALGORITMO PARA SOMAR E EXIBIR OS VALORES QUE O USUARIO DIGITAR
# O LOOP DEVERÁ TERMINAR QUANDO O USUÁRIO INFORMAR O NUMERO 0
# QUANDO DIGITAR 0 DEVERÁ EXIBIR O RESULTADO DA SOMA

#N1 = int(input("Digite o valor: "))
#Soma = 0

#while (N1 != 0): #Enquanto N1 diferente de 0
#    Soma = Soma + N1 #Vai somar o valor da soma 0 + o valor N1 informado pelo cliente
#    print (f"Resultado Parcial: {Soma}") #Informara o resultado parcial
#    N1 = int(input("Digite o valor: ")) #No loop deve informar um novo valor

#else:
#    print (f"voce digitou o número 0, resultado final: {Soma}")
    
#######################################################################################

# CRIE UM ALGORITMO QUE NÃO PERMITA QUE O USUARIO INFORME UM VALOR MENOR QUE 100
# SE ELE INFORMAR UM VALOR MENOR, DEVE MOSTRAR UMA NENSAGEM PARA SOLICITAR QUE DIGITE O NUMERO NOVAMENTE
# SE ELE INFORMAR UM VALOR MAIOR, DEVE MOSTRAR UMA MENSAGEM DE SUCESSO

#N1 = int(input("Digite um numero: "))

#while (N1 < 100):
#    N1= int(input("Numero incorreto, digite outro numero: "))
#else:
#    print (f"O número digitado {N1} é maior ou igual a 100, registrado com sucesso")

#######################################################################################

# CONSTRUA UM ALGORITMO PARA UM PEQUENO GAME, NO QUAL UM JOGADOR ENTRA COM UM NUMERO E O OUTRO DEVE ADIVINHAR O NUMERO INFORMADO
# O ALGORITMO DEVE PEDIR PARA O JOGADOR DESAFIANTE INFORMAR UM VALOR NUMERO
# O ALGORITMO DEVE PEDIR PARA O JOGADOR DESAFIADO INFORMAR UM VALOR NUMERO
# SE O VALOR INFORMADO FOR IGUAL AO VALOR DO DESAFIANTE, O ALGORITMO DEVE EXIBIR A MENSAGEM DE SUCESSO
# SE O VALOR INFORMADO FOR DIFERENTE, O SISTEMA DEVE INFORMAR QUE ESTA INCORRETO E PEDIR UM NOVO VALOR
# SE O DESAFIANTE OU DESAFIADO INFORMAREM NUMERO DIFERENTE DE 0 A 9, APRESENTAR MENSAGEM  DE ERRO

#import os # Para limpar o numero que o desafiante colocou, esta biblioteca habilita (os.system('cls'))

#print ("JOGADOR DESAFIANTE")
#N1 = int(input("Digite umdafadsf valor de 0 a 9: "))

#while(N1 < 0 or N1 > 9):
#    N1 = int(input("Valor inválido, digite novamente: "))
#print ("sucesso")
#os.system('cls')

#print ("JOGADOR DESAFIADO")
#N2 = int(input("Tente adivinhar o numero de 0 a 9: "))
#while (N2 < 0 or N2 > 9):
#    N2 = int(input("Numero invalido, digite os valores entre 0 e 9: "))

#while (N2 != N1):
#    N2 = int(input("Você não acertou, digite novamente um número: "))
#    while (N2 < 0 or N2 > 9):
#        N2 = int(input("Numero invalido, digite os valores entre 0 e 9: "))
    
#print ("Parabéns, você acertou o número")

#######################################################################################

# CONSTRUA UM ALGORITMO PARA UM PEQUENO GAME, NO QUAL UM JOGADOR ENTRA COM UM NUMERO E O OUTRO DEVE ADIVINHAR O NUMERO INFORMADO
# O ALGORITMO DEVE PEDIR PARA O JOGADOR DESAFIANTE INFORMAR UM VALOR NUMERO
# O ALGORITMO DEVE PEDIR PARA O JOGADOR DESAFIADO INFORMAR UM VALOR NUMERO
# SE O VALOR INFORMADO FOR IGUAL AO VALOR DO DESAFIANTE, O ALGORITMO DEVE EXIBIR A MENSAGEM DE SUCESSO
# SE O VALOR INFORMADO FOR DIFERENTE, O SISTEMA DEVE INFORMAR QUE ESTA INCORRETO E PEDIR UM NOVO VALOR
# SE O DESAFIANTE OU DESAFIADO INFORMAREM NUMERO DIFERENTE DE 0 A 9, APRESENTAR MENSAGEM  DE ERRO
# INCREMENTAR SE O USUÁRIO ERRAR POR 3 VEZES INFORMAR FINALIZAR O SCRIPT
    
import os # Para limpar o numero que o desafiante colocou, esta biblioteca habilita (os.system('cls'))

Cont = 0

print ("JOGADOR DESAFIANTE")
N1 = int(input("Digite um valor de 0 a 9: "))

while(N1 < 0 or N1 > 9):
    N1 = int(input("Valor inválido, digite novamente: "))
os.system('cls')

print ("JOGADOR DESAFIADO")
N2 = int(input("Tente adivinhar o numero de 0 a 9: "))
while (N2 < 0 or N2 > 9):
    N2 = int(input("Numero invalido, digite os valores entre 0 e 9: "))
    while (Cont < 4):
        Cont = Cont + 1

while (N2 != N1):
    N2 = int(input("Você não acertou, digite novamente um número: "))
    while (N2 < 0 or N2 > 9):
        N2 = int(input("Numero invalido, digite os valores entre 0 e 9: "))
    
print ("Parabéns, você acertou o número")