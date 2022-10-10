# RESULTADO DE OPERADORES LOGICOS #

############ A AND B ############              ############# A OR B #############                  
#A          B           RESULTADO              #A           B           RESULTADO
#V          V           V                      #V           V           V
#V          F           F                      #V           F           V
#F          V           F                      #F           V           V
#F          F           F                      #F           F           F

# DIGITE 3 NÚMEROS E IMPRIMA SE O RESULTADO É VERDADEIRO OU FALSO #

N1 = int(input("Digite um numero"))
N2 = int(input("Digite outro numero"))
N3 = int(input("Digite o ultimo numero"))

print( N1 > N2 or N1 > N3) #Nesse caso vai imprimir se é verdadeiro ou falto
