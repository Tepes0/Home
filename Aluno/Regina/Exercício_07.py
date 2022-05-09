#Olá, a autora deste checkpoint é chama-se Regina Maria e ela está usando a versão 3.10 do Python.
#Dia 08/05

#Exercício 07
print("Dada a lista a seguir, encontre o que se pede:")
#deixando a lista visível:
print([10, -2, 4, 8, 100, 44, -19, 2, 3, 2, -90, 11, -33, 10, 67, 15])

lista_00 = [10, -2, 4, 8, 100, 44, -19, 2, 3, 2, -90, 11, -33, 10, 67, 15]

#separando os itens positivos e negativos manualmente em diferentes listas para fazer a soma posteriormente
lista_neg = [-2, -19, -90, -33]
lista_pos = [10, 4, 8, 100, 44, 2, 3, 2, 11, 10, 67, 15]

#Usando uma condição para comprovar os números pares (aqueles que possuem a visão com o resto 0)
print("os números pares da lista são:")
for number in lista_00:
    if(number % 2 == 0):
        print(number)
print("o valor máximo é:",max(lista_00))
print("o valor mínimo é:",min(lista_00))
print("vezes em que o primeiro número da lista aparece:",)
print("a média dos números da lista é:",)
print("a soma dos números negativos da lista é:",sum(lista_neg))
print("a soma dos números positivos da lista é:",sum(lista_pos))
print("os elementos repetidos são:", )

