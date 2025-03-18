n1 = float(input('numero 1 ') )
n2 = float(input('numero 2 ') )
opa = input('qual operação +, -, /, *, %, //, **?')

if opa == '+':
    rst = (n1)+(n2) 

elif opa == '-':
    rst = (n1)-(n2)

elif opa == '/':
    rst = (n1)/(n2)

elif opa == '*':
    rst = (n1*n2)
    
elif opa == '%':
    rst = (n1%n2)

elif opa == '**':
    rst = (n1**n2)

elif opa == '//':
    rst = (n1//n2)

else :
    rst = 'operação invalida'

print ('{:.2f}' .format(rst))