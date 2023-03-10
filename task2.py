"""
Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
Помогите Кате отгадать задуманные Петей числа
"""

s = int(input("Введите сумму чисел: "))
p = int(input("Введите произведение чисел: "))

for x in range(1, 1001):
    if p % x != 0:  # если x не является делителем p, пропускаем
        continue
    y = p // x  # вычисляем y как частное от деления p на x
    if x + y == s:  # если найдены подходящие числа, выводим их и завершаем цикл
        print(f"X = {x}, Y = {y}")
        break
else:  
    print("Нет решения")