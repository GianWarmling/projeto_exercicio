from controller.divisao import chamadivisao
from controller.multiplicacao import chamamultiplicacao
from controller.soma import chamasoma
from controller.subtracao import chamasubtracao

def menu():
    var = "sim"
    while var == "sim":
        
        operacao = input("Qual operação matemática você deseja: soma, sub, div, mult\n")  
        
        if operacao == "div":
            numero1 = int(input("Digite um número: "))
            numero2 = int(input("Digite um número: "))
            divisao = chamadivisao(numero1, numero2)

        elif operacao == "sub":
            numero1 = int(input("Digite um número: "))
            numero2 = int(input("Digite um número: "))
            subtracao = chamasubtracao(numero1, numero2)

        elif operacao == "mult":
            numero1 = int(input("Digite um número: "))
            numero2 = int(input("Digite um número: "))
            multiplicacao = chamamultiplicacao(numero1, numero2)

        elif operacao == "soma":
            numero1 = int(input("Digite um número: "))
            numero2 = int(input("Digite um número: "))
            soma = chamasoma(numero1, numero2)

        var = input("Deseja continuar? ")
