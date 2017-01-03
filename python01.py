a = 42
b = 26
print (a = 42 and b = 26)
print (a = 43 and b = 26)
print (a = 42 or b = 252)

--- marcadores

print ('O numero é %d ' %a)
#% = marcador
#%d = marcador dentro da string(d = inteiros)
#%a = variavel do marcador

dc = 'qualquer'
print('Esta é a palavra %s ' %dc)
#% = marcador
#%s = marcador para strings

dc = 3.1512
print('Esta é a palavra %f ' %dc)
#ou
print ('Esta é a palavra %.2f' %dc)
#%f = marcador de decimais
#%.2f = marcador com limite de casas

# linguagens dinamica = n precisa definir um tipo
# fortemente tipada = tem diferenças entre os tipos
# pode ser feitas varias atribuições multiplas

a = 34
b = 37
a,b = b,a
# valor de a vai para b e vice-versa, sem perder ou adicionar variavel
#pythontutor.com




