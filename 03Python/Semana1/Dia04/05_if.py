if True:
  print('deber­a ejecutarse')

if False:
  print('nunca se ejecuta')

#Caso uno
pet = input('cual es tu mascota favorita? ')

if pet == 'perro':
  print('genial tienes buen gusto')
elif pet == 'gato':
  print('espero tengas suerte')
elif pet == 'pez':
  print('eres lo maximo')
else:
  print('no tienes ninguna mascota interesante')

#Caso dos
stock = int(input('Digita el stock => '))

if stock >= 100 and stock <= 1000:
  print('el stock es correcto')
else:
  print('el stock es incorrecto')


#Caso tres
number = int(input('Ingrese un numero => '))
result = number % 2
if (result == 0):
	print('Es par')
else:
	print('Es impar')