#Teste de cálculo

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

Resultado = ('Soma: {soma}. \nSubtracao: {subtracao}. '
    ' \nMultiplicacao {multiplicacao}. \nDivisao {divisao}. \nResto {resto}'.format(soma=soma,
                                                                    subtracao=subtracao,
                                                                    multiplicacao=multiplicacao,
                                                                    divisao=divisao,
                                                                    resto=resto))
print(Resultado)



# print ('subtração: {}'.format(subtração))
# print ('multiplicação: {}'.format(multiplicação))
# print ('divisão: {}'.format(divisão))
# print ('resto: {}'.format(resto))
