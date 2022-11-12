# Задача 6
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

from random import randint


my_favorite_songs = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

t=[] 
for i,x in my_favorite_songs.items():
   t.append(x)
i = 3 
times = 0  
while i > 0:   
    rand = randint(1,8)
    print(rand)
    times += t[rand]
    i-=1
#   times = my_favorite_songs['A Sorta Fairytale']+ my_favorite_songs['In This World'] + my_favorite_songs['Waste a Moment']
print("Три песни звучат:", round(times,2),"минут")

# Хорошо!
