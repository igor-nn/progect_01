# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек


from turtle import end_fill


city = ('Moscow', 'Nizhny Novgorod', 'St. Petersburg', 'Volgograd')
print('Крупные города России:',end = ' ')
for i in city:
  print(i, end = ' ')
print()  
population = (12000,1300,5300,1000)
#population = [[city[0],12000],[city[1],1300],[city[2],5300],[city[3],1000] ]
# #print(population)
size = [
        [city[0]]+[population[0]],
        [city[1]]+[population[1]],
        [city[2]]+[population[2]],
        [city[3]]+[population[3]]
        ]

#result = f"{city}\n{population}\n{size}"
#print(result)
print("Численность населения ",city[1],"-",population[1],"человек.")
x = population[0]+population[1]+population[2]+population[3]
print("Итого численность населения всех городов:",x,"человек.")