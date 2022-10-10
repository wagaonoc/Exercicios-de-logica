
# CRIE UM ALGORITMO ONDE O USUARIO VAI INFORMAR DOIS NUMEROS E O SISTEMA TEM DE DIZER QUAL O MAIOR

#N1 = int(input("Digite o primeiro numero: "))
#N2 = int(input("Digite o segundo numero: "))

#if N1 == N2:
#    print("Os números são iguais")
#elif N1 > N2:
#    print(f"O primeiro número: {N1} é maior que o segundo número: {N2}")
#else:
#    print(f"O segundo número: {N2} é maior que o primeiro número: {N1}")

#############################################################################

# CRIE UM ALGORITMO ONDE O USUARIO VAI INFORMAR 4 NUMEROS E O SISTEMA DEVERÁ CALCULARA MEDIA #
# INFORMAR SE ELE FOI APROVADO #
# SE TIRAR NOTA ACIMA DE 7, CASO CONTRÁRIO REPROVADO #

#N1 = int(input("Digite a primeira nota: "))
#N2 = int(input("Digite a segunda nota: "))
#N3 = int(input("Digite a terceira nota: "))
#N4 = int(input("Digite a quarta nota: "))

#Media = (N1+N2+N3+N4)/4

#if Media > 7:
#    print (f"{Media}: Aprovado")
#else:
#    print (f"{Media}: Reprovado")
    

#############################################################################

# CRIE UM ALGORITMO PARA UM CAIXA ELETRONICO. O ALGORITMO DEVE PEDIR PARA O USUÁRIO O VALOR QUE ELE QUER SACAR #
# EM SEGUIDA VERIFICAR SE O VALOR INFORMADO É MENOR QUE O VALOR DISPONIVEL #
# VAMOS ASSUMIR QUE O CLIENTE TEM UM SALDO DE 1000 REAIS PARA SAQUE #

#Saldo = 1000
#Saque = int(input("Digite o valor do saque: "))

#if Saldo < Saque:
#    print ("Saldo indisponível, valor informado maior que o saldo")
#else:
#    Saldo = Saldo - Saque
#    print (f"Saque realizado com sucesso, seu saldo atual é: {Saldo}")

#############################################################################

# CRIE UM ALGORITMO PARA LER 4 NOTAS, CALCULAR A MÉDIA, EM SEGUIDA MOSTRAR A MENSAGEM #
# REPROVADO: CASO ALUNO TENHA MEDIA MENOR QUE 4 #
# RECUPERAÇÃO: SE TIVER MÉDIA IGUAL A 4, 5 ou 6 #
# APROVADO: SE TIVER MEDIA MAIOR OU IGUAL A 7 #

N1 = int(input("Digite a primeira nota: "))
N2 = int(input("Digite a segunda nota: "))
N3 = int(input("Digite a terceira nota: "))
N4 = int(input("Digite a quarta nota: "))

Media = (N1+N2+N3+N4)/4

if Media >= 7:
    print (f"Você tirou: {Media}, está em aprovado")
elif Media <= 4:
    print (f"Você tirou: {Media}, está reprovado")
else:
    print (f"Você tirou: {Media}, está recuperação")
