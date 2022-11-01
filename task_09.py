#--------------генерация паролей
import random

string = "+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = []
length = input("Задайте длину пароля:")
try:
  length = int(length)  
  while length > 0:
    password.append(random.choice(string))
    length-=1 
  print('Сгенерированный пароль',''.join(password))
except: 
    print('Введено не корректное чило')