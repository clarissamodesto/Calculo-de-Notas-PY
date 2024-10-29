'''
Nome: Clarissa Cruz
Data: 29/10/2024
Versão 1
'''

#Faça um programa para a leitura de duas notas parciais de um aluno.  
#A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
#A mensagem “Aprovado com Distinção”, se a média for igual a dez;
#A mensagem “Reprovado” se a média for menor de do que sete;

nota1 = float (input('Digite a nota da Avaliação 1: '))
nota2 = float (input('Digite a nota da Avaliação 2: '))
notafinal = (nota1 + nota2) / 2

if notafinal == 10:
    print ('Aprovado com Distinção')
elif notafinal >= 7:
    print ('Aprovado')
else:
    print ('Reprovado')