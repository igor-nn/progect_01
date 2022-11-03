
# ----------- накопления сотрудника за 12 месяцев

salary = float(input("Какая зарплата у сотрудника?"))
expenses = salary
savings = 0
montch =11
while  montch > 0:  
   salary += (salary*5/100)
   remains = salary - expenses
   savings += remains
   montch -= 1
   print(f'зарплата-{salary}, растраты - {expenses}, накопления - {savings}')

print("За год сотрудник накопит:",round(savings,2), "рублей")  