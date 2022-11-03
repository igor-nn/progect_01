
# ----------- накопления сотрудника за 12 месяцев

salary = input("Какая зарплата у сотрудника?")
savings = 0 # накопления
montch =11
try:
  salary = float(salary)
  expenses = salary
 
  while  montch > 0:  
    salary += (salary*5/100)
    remains = salary - expenses
    savings += remains
    montch -= 1
    #print(f'зарплата-{salary}, растраты - {expenses}, накопления - {savings}')
    
except:
  print("Не корректный ввод")    

print("За год сотрудник накопит:",round(savings,2), "рублей") 