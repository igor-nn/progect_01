# Задача 4
# Вывести по номеру месяца кол-во дней в нем (без указания названия месяца, в феврале 28 дней)
# Результат проверки вывести на консоль
# Если номер месяца некорректен - сообщить об этом

user_input = input("Введите номер месяца: ")
month = int(user_input)
# print('Вы ввели', month)

list_month_day = [['Январь',31],['Февраль',28],['Март',31],['Апрель',30],['Май',31],['Июнь',30],['Июль',31],['Август',31],['Сентябрь',30],['Октябрь',31],['Ноябрь',30],['Декабрь',31]]
list_month = ['Январь','Февраль','Март','Апрель','Май','Июнь','Июль','Август','Сентябрь','Октябрь','Ноябрь','Декабрь']
day = [31,28,31,30,31,30,31,31,30,31,30,30]
if month > 12 or month == 0:
  print("Не корректный номер месяца!")
else:
  month -= 1
  #print(list_month_day[month])
  print(f'В {month+1} месяце {day[month]} дней')