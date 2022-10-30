# Задача 2
# Создайте список "города" с именами любых городов
# Количество элементов в списке "города" не меньше 3!

# Создайте список списков населения перечисленных городов

# Выведите на консоль население второго города в списке в формате
# Население Москвы - ХХ человек

# Выведите на консоль общий размер населения перечисленных городов как сумму населения всех городов
# Итого размер населения - ХХ человек


city = ['Moscow', 'Nizhny Novgorod', 'St. Petersburg', 'Volgograd']
#city = [['Moscow',12000], ['Nizhny Novgorod',2300], ['St. Petersburg',5300], ['Volgograd',1000]]
#print(city)
population = [12000,1300,5300,1000]
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
print("Население",city[1],"-",population[1],"человек.")
x = population[0]+population[1]+population[2]+population[3]
print("Итого размер населения:",x,"человек.")