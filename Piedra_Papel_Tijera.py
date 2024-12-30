import random

options = ('piedra','papel','tijera') #tuple

ia_wins = 0
usuario_wins = 0 
rondas = 1

while True:

  print('*' * 10)
  print('RONDA', rondas)
  print('*' * 10)

  print('VICTORIAS DE LA IA => ' ,ia_wins)
 
  print('VICTORIAS DE USUARIO  => ' ,usuario_wins)
  print('-' * 10)
  user_option = input('piedra, papel o tijera =>')
  user_option = user_option.lower() # pasar texto a minusculas
  
  rondas   +=1
  
  if not user_option in options:
     print('esa opción no es valida')
     continue
  
  computer_option = random.choice(options)
  
  print('usuario seleccionó  =>', user_option)
  print('IA seleccionó =>', computer_option)
  
  if user_option == computer_option:
    print ('EMPATE!')
    
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      print ('Piedra gana a tijera')
      print ('USUARIO GANO!')
      usuario_wins += 1
    else:
      print('papel gana a piedra')
      print('IA GANO!')
      ia_wins += 1
  
  
  elif user_option == 'papel':
    if computer_option == 'piedra': 
      print('papel gana a piedra')
      print('USUARIO GANO!')
      usuario_wins += 1
    else:
      print('tijera gana a papel')
      print('IA GANO!')
      ia_wins += 1
  
  
  elif user_option == 'tijera':
    if computer_option == 'papel':
      print('tijera gana a papel')
      print('USUARIO GANO!')
      usuario_wins += 1
    else:
      print('piedra gana a tijera')
      print('IA GANO!')
      ia_wins += 1
      
  if ia_wins == 2:
    print('*' * 10)
    print('EL GANADOR ES LA IA JUA JUA JUA!')
    print('*' * 10)
    break

  if usuario_wins ==2:
    print('*' * 10)
    print('EL GANADOR ERES TU BIEN HECHO!')
    print('*' * 10)
    break