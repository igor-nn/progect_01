# Задача 5
# Зарплата сотрудника составляет salary руб., 
# Расходы на проживание превышают зараплату и составляют expenses руб. в месяц. 
# Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Напишите скрипт расчета суммы денег, которую необходимо взять в долг, 
# чтобы можно было прожить ближайший год (12 месяцев).
# Формат вывода:
# Необходимо взять в долг ХХХ.ХХ рублей

salary, expenses = 10000, 12000

#for expenses in 11:
x = 1
dept = expenses - salary
while x <= 11:

    expenses += (expenses*3/100)
    dept += expenses - salary
    x += 1
    #print(int(expenses))

print("Необходимо взять в дог:",round(dept,2), "рублей")
