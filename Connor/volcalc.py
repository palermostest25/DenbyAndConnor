import math

def circle():
   while True:
      try:
         r = float(input('Radius (In CM): '))
         break
      except ValueError:
         print('Please Enter A Number.')
   r = r * r
   a = r * math.pi
   while True:
      try:
         h = float(input('Hight (In CM): '))
         break
      except ValueError:
         print('Please Enter A Number.')
   vol = h * a
   vol = vol / 1000
   while True:
      rnd = input('Round? [Y,N] ')
      rnd = rnd.lower()
      if rnd == 'y':
         vol = round(vol)
         break
      elif rnd == 'n':
         break
      else:
         print('Please Enter Y or N.')
   print(str(vol) + 'L')
   input('Press Enter To Exit.')
   exit() 

def square():
   while True: 
      try:
         w = float(input('Width (In CM): '))
         break
      except ValueError:
         print("Please Enter A Number.")
   while True: 
      try:
         h = float(input('Hight (In CM): '))
         break
      except ValueError:
         print("Please Enter A Number.") 
   vol = w * w * h
   vol = vol / 1000
   while True:
      rnd = input('Round? [Y,N] ')
      rnd = rnd.lower()
      if rnd == 'y':
         vol = round(vol)
         break
      elif rnd == 'n':
         break
      else:
         print('Please Enter Y or N.')
   print(str(vol) + 'L')
   input('Press Enter To Exit.')
   exit()   

print('1. Circle\n2. Square')
while True:
   choice = input('Choice: ')
   if choice == '1':
      circle()
      break
   elif choice == '2':
      square()
      break
   else:
      print('Please Choose 1 Or 2.')


     
 


   
