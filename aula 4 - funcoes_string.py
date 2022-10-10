#FUNÇÕES UTILIZADAS EM STRING

minha_string = "qualquer texto"
print(f"concatenar {minha_string} em string")

print(minha_string.upper()) #deixando um texto maiusculo com upper;
print(minha_string.lower()) #deixando um texto minusculo com lower;
print(minha_string.capitalize()) #deixa a primeira letra da frase maiúscula;
print(minha_string.isupper()) #verificando se o texto é maiusculo ou não (resultado booleano);
print(minha_string.islower()) #verificando se o texto é minusculo ou não (resultado booleano);
print(minha_string.strip()) #remove espaço antes do texto ou final dos textos, não remove espaço no meio;
print(minha_string.replace("qualquer", "Meu")) #substitui uma palavra, textou ou até letra por outra;
print(minha_string.replace("u", "U",3)) #substitui a palavra u por U até a terceira palavra U;
print(len(minha_string)) #conta a quantidade de letras de uma palavra ou frase;
print(minha_string[2]) #busca a letra dentro de uma palavra, o 2 é o índice que começa de 0,1,2,3..., portanto palavra "a";
print(minha_string[2:5]) #busca as letras com inicio do indice em 2 até 5, portanto letras "alq";
print(minha_string[-12:-9]) #busca as letras de traz pra frente, começa o indice por -1;
print(minha_string.index("u")) #retorna em qual indice está a letra u no texto, no caso 1;
print(minha_string.index("texto")) #retorna o primeiro indice da palavra, no caso 9;

x = "texto" in minha_string
print(x) #de acordo com a variável acima, verifica se um texto existe ou não (resultado booleano);

outra_string = """
linha1
linha2
linha3
linha4"""
print(outra_string) #para quebra de linha utilizando as 3 (""") no inicio e fim;

outra_string = "o analista de TI é \"doido\"" #printa as aspas no texto através do \ - o analista de TI é "doido"
print(outra_string)

