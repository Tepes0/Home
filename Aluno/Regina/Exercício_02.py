#Olá, a autora deste checkpoint é chama-se Regina Maria e ela está usando a versão 3.10 do Python.
#Dia 08/05

print("Você tem 10 tentativas para o nível 1; 5 para o nível 2 e 3 tentativas para o nível 3")
int(input("Escolha seu nível:"))
chances_nivel1 = 10
chances_nivel2 = 5
chances_nivel3 = 2
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



