
# ESCREVA UM ALGORITMO PARA LER DOIS NUMEROS E MOSTRAR SE ELES SÃO IGUAIS #

#N1 = int(input("Digite um numero: "))
#N2 = int(input("Digite outro numero: "))

#if N1 == N2:
#    print("Os numeros são iguais")
#else:
#    print("Os numeros são diferentes")
    
# ESCREVA UM ALGORITMO PARA LER DOIS NUMEROS E MOSTRAR QUAL É O MAIOR, O MENOR OU SE SÃO IGUAIS #

#N1 = int(input("Digite um numero: "))
#N2 = int(input("Digite outro numero: "))

#if N1 > N2:
    #print(f"{N1} é maior que: {N2}")
#elif N1 < N2:
    #print(f"{N2} é maior que {N1}")
#else:
    #print(f"{N1} e {N2} são iguais")
    
# ESCREVA UM ALGORITMO PARA LER 4 NOTAS, CALCULAR A MEDIA, EM SEGUIDA DEVE MOSTRAR SE O ALUNO ESTÁ DE RECUPERAÇAO #
# RECUPERAÇÃO: SE A MÉDIA FOR MAIOR QUE 3 E MENOR QUE 6

N1 = float(input("Digite a primeira nota: "))
N2 = float(input("Digite a segunda nota: "))
N3 = float(input("Digite a terceira nota: "))
N4 = float(input("Digite a quarta nota: "))

Media = (N1+N2+N3+N4) / 4

if Media > 3 and Media < 6:
    print(f"Você tirou {Media}, está de recuperação")
else:
    print(f"Voce tirou {Media}, está aprovado")
