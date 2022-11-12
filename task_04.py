# Задача 4
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйсте модуль random
# import random 

#from random import random
from random import randint


my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

x = randint(0,8)
y = randint(0,8)
z = randint(0,8)


if y == x:
    while y==x:
        y = randint(0,8)

if z == x or z == y:
    while z == x or z == y:
       z = randint(0,8)

print("Треки:",x+1,'+',y+1,'+',z+1)
result_time = my_favorite_songs[x][1]+my_favorite_songs[y][1]+my_favorite_songs[z][1]
print("Три песни звучат:", round(result_time,2), "минут")

# Вот вариант покороче
# Решение 2
time = 0
for song in sample(my_favorite_songs, 3):
    print(song[0])
    time += song[1]

print(f'Три песни звучат {round(time, 2)}')
