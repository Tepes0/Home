#Olá, a autora deste checkpoint é chama-se Regina Maria e ela está usando a versão 3.10 do Python.
#Dia 08/05

tentativa = int(input("Digite sua tentativa de número secreto aqui:"))
number_secret = 1822

if tentativa == (1822):
    print("Parabéns! Você acertou o número secreto que é:", int(number_secret))
else:
    print("ERRO - tente novamente, o número secreto não é:", int(tentativa))
#Dica para aproximar o jogador do número correto
if tentativa <1822:
    print("A sua tentativa foi menor que o número secreto")
else:
    print("A sua tentativa foi maior que o número secreto")





























