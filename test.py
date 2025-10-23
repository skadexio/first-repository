#практическая 4

#3

a = int(input())
b = int(input())

if a < b:
    for i in range(a, b+1):
        print(i)
else:
    for j in range(a, b-1, -1):
        print(j)

#8

n = int(input("Число <= 9: "))

for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end="")
    print()

#практическая 5

#8

line = input("Строка: ")

line = line.rstrip(".")
words = line.split()

print("Кол-во слов: ", len(wrds))

#13

line = input("Строка: ")

start = line.find("(")
end = line.find(")")

signs = line[start+1:end]

print("Символы внутри строки: ", signs)

#практическая 6

#8.1

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

summ = 0
product = 1

for x in numbers:
    summ += x
    product *= x

print("Сумма: ", summ)
print("Произведение: ", product)

#8.2

num = [1.0, 9.0, 3.0, 0.0, 5.0, 0.0]

value = sum(num) / len(num)

for i in range(len(num)):
    if num[i] == 0:
        num[i] = value

print(num)

#13.1

num = [1, 2, 3, 4, 2, 3, 5]

ind = []

for i in range(len(num)):
    for j in range(i+1, len(num)):
            if num[i] == num[j] not in ind:
                print("Элемент", num[i], "встречается на индексах", i, "и", j)
                ind.append(num[i])

#13.2

num = [12, 15, 7, 21, 13, 15, 2, 29]

for i in range(len(num)):
    if num[i] < 15:
        num[i] = num[i] * 2

print(num)



