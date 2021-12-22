print ("Para Converter Celsius para Fahrenheit. Digite 1")
print ('Para Converter Fahrenheit para Celsius. Digite 2')
opcao= int(input('Digite aqui a opção desejada: '))
if opcao == 1:
    print('---------- Celsius Para Fahrenheit----------')
    temp1= int(input("Digite a temperatura em Celsius: "))
    celstemp= (temp1 *9/5)+32
    total= round(celstemp,2)
    print ('A temperatura é:',total, "ºF")
elif opcao ==2:
    print('---------- Fahrenheit Para Celsius----------')
    temp2= int(input("Digite a temperatura em Fahrenheit: "))
    celstemp2= (temp2-32)*5/9
    total1= round(celstemp2,2)
    print('A temperatura é: ', total1,'°C')

