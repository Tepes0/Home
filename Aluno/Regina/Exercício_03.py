#Olá, a autora deste checkpoint é chama-se Regina Maria e ela está usando a versão 3.10 do Python.
#Dia 08/05

#Definindo funções que executem as operações pedidas
#a velocidade média é a variação da distância / pela variação do tempo
#Para calcular a velocidade média neste programa, digite as informações pedidas e digite 0 para as variaveis "primeiro número e segundo número"
#Para realizar outras operações é só fazer o processo normalmente digitando 0 para "variação de tempo" ou "variação distancia"

#Foram definidas as variáveis
variacao_distancia = int(input("Digite a variação do deslocamento, se houver:"))
variacao_tempo = int(input("Digite a variação do tempo, se houver:"))
number_01 = int(input("Digite o primeiro número:"))
operador = input("Digite o operador da conta:")
number_02 = int(input("Digite o segundo número:"))

#Foram definidas as condições para que as operações sejam feitas
if operador == "+":
    resposta = number_01 + number_02
elif operador == "vm":
    resposta = variacao_distancia / variacao_tempo
elif operador == "-":
    resposta = number_01 - number_02
elif operador == "/":
    resposta = number_01 / number_02
elif operador == "*":
    resposta = number_01 * number_02
else:
    resposta = "erro na operação"

print(str(number_01) + "" + str(operador) + "" +str(number_02) + " = " +str(resposta))