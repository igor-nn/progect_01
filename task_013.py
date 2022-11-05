#
#  калькулятор

def operator(x,y,char): # непосредственно калькулятор
    if char == '+':
        z = x + y
    elif char == '-':
        z = x - y
    elif char == '*':
        z = x * y 
    elif char == '/':
        if y != 0:
          z = x / y
        else:
            print("Деление на ноль запрещено!")     
    elif char == '%':
        z = (x * y) /100
        #z = int(p)
    elif char == '**':
        z = x ** y 
    elif char == '//':
        z = x // y 
    
    string = str(z)           # если после запятой "0", то конвертируем переменную в "int"
    string = string.split('.')
    if string[1] == '0':
        z = int(string[0])   

    return z

def Inputs():  # -- преобразовываем введенные пользователем данные в числа и операнды
  inputs = input(': ')
  list = (inputs)
  if list[0].isalpha(): # -- проверяем первый символ, если не цифра, то выходим из калькулятора
     global exits
     exits = False
     return 0,0,''
  for oper in list:
    if oper == '+':
        break
    if oper == '-':
        break
    if oper == '*':
        id = list.index('*')
        if list[id+1] == '*':
            oper = '**'
            break    
        break
    if oper == '/':
        id = list.index('/')
        if list[id+1] == '/':
            oper = '//'
            break   
        break
    if oper == '%':
        break
  string = inputs.split(oper) #разделяем введеное значение на две подстроки знаком операции(+,-,*,/,...)
  string1 = string[0]
  string2 = string[1]
  
# if string1.isnumeric():
  number1 = float(string1)
# if string2.isnumeric():
  number2 = float(string2) 

  return number1, number2, oper 


try:
  n = True
  exits = True # для выхода из калькулятора
  while True: 
      if n:
        print('Вводите без пробелов: первое число, следом знак операции и второе число')
        print('для выхода - нажмите любую букву!')
      number1,number2,oper = Inputs()
      if not exits:
        print('Выход')
        break  
      print(f' Ответ: {operator(number1,number2,oper)}')
      n = False   
except:
      print("Не корректный ввод!")
      
