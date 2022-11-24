#Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.
n = int(input('Напишите число: ')) 

sum = 0
i = 1
for i in range (1, n+1):
    result = (1+1/i)**i
    sum = sum + result
    i += 1
print(sum)