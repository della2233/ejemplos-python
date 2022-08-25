secret_number = 300
 
while True:
   number = input('adivinar el numero: ')
 
   try:
       number = int(number)
   except:
       print('Sorry that is not a number')
       continue
 
   if number != secret_number:
       if number > secret_number:
           print(number, 'es mayor que el número secreto')
 
       elif number < secret_number:
           print(number, 'es menor que el número secreto')
   else:
       print('Adivinaste el número te amo:', secret_number)
       break