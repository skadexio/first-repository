# практическая 7

# вариант 8

# 1

# def is_good_num(numb):
#     for numb_char in str(numb):
#         num = int(numb_char)
#         if num == 0:
#             return False
#         if numb % num != 0:
#             return False
#     return True

# def main():
#     n = int(input("Введите натуральное число n: "))

#     for i in range(1, n + 1):
#         if is_good_num(i):
#             print(i)

# main()

# 2

# def change_first_and_last(array):
#     temp = array[0]

#     array[0] = array[-1]

#     array[-1] = temp

# def main():
#     m = int(input("Введите длину массива: "))

#     array = []

#     for i in range(m):
#         element = int(input(f"Введите элемент {i + 1}: "))
#         array.append(element)

#     print("Изначальный массив: ", array)

#     change_first_and_last(array)

#     print("Массив после замены: ", array)

# main()

# вариант 13

# 1

# def is_armstrong(number):
#     str_numb = str(number)

#     n = len(str_numb)

#     total = 0

#     for num_char in str_numb:
#         num = int(num_char)
#         total += num ** n

#     return total == number

# def main():
#     k = int(input("Введите верхнюю границу k: "))

#     print("Числа Армстронга от 1 до", k, ":")

#     for i in range(1, k + 1):
#         if is_armstrong(i):
#             print(i)

# main()

# 2

# import math

# def find_min_angle_point(x1, y1, x2, y2, x3, y3):

#     angle1 = math.atan2(y1, x1) 
#     angle2 = math.atan2(y2, x2) 
#     angle3 = math.atan2(y3, x3) 

#     min_angle = angle1 
#     min_point = (x1, y1)

#     if angle2 < min_angle:
#         min_angle = angle2
#         min_point = (x2, y2)

#     if angle3 < min_angle:
#         min_angle = angle3
#         min_point = (x3, y3)

#     print("Точка с минимальным углом: ", min_point)

# def main():
#     x1 = float(input("Введите x1: "))
#     y1 = float(input("Введите y1: "))

#     x2 = float(input("Введите x2: "))
#     y2 = float(input("Введите y2: "))

#     x3 = float(input("Введите x3: "))
#     y3 = float(input("Введите y3: "))

#     find_min_angle_point(x1, y1, x2, y2, x3, y3)

# main()

# практическая 8

# вариант 8

# 1

# n = int(input("Введите размер матрицы n: "))

# A = []
# for i in range(n):
#     row = input(f"Введите элементы {i + 1}-й строки через пробел: ").split()

#     for j in range(len(row)):
#         row[j] = float(row[j])

#     A.append(row)

# k = int(input("Введите номер строки k: "))

# diagonal = A[k-1][k-1]

# for j in range(n):
#     A[k-1][j] = A[k-1][j] / diagonal

# for row in A:
#     for element in row:
#         print(element, end=' ')
#     print()

# 2

# n = int(input("Введите размер квадратной матрицы n: "))

# A = []
# for i in range(n):
#     row = input(f"Введите элементы {i+1}-й строки через пробел: ").split()
#     for j in range(len(row)):
#         row[j] = float(row[j])
#     A.append(row)

# T = []
# for i in range(n):
#     new_row = [0] * n
#     for j in range(n):
#         new_row[j] = A[j][i]
#     T.append(new_row)

# for row in T:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# варинат 13

# 1

# M = int(input("Введите количество строк M: "))
# N = int(input("Введите количество столбцов N: "))

# A = []
# for i in range(M):
#     row = input(f"Введите элементы {i+1}-й строки через пробел: ").split()
#     for j in range(N):
#         row[j] = float(row[j])
#     A.append(row)

# for i in range(1, M, 2):  
#     min_elem = A[i][0] 
#     for j in range(1, N):
#         if A[i][j] < min_elem:
#             min_elem = A[i][j]

#     print(f"Наименьший элемент {i+1}-й строки: {min_elem}")

# 2 

# M = int(input("Введите количество строк M: "))
# N = int(input("Введите количество столбцов N: "))

# A = []
# for i in range(M):
#     row = input(f"Введите элементы {i+1}-й строки через пробел: ").split()
#     for j in range(N):
#         row[j] = float(row[j])
#     A.append(row)

# min_val = A[0][0]
# max_val = A[0][0]
# min_pos = (0, 0)
# max_pos = (0, 0)

# for i in range(M):
#     for j in range(N):
#         if A[i][j] < min_val:
#             min_val = A[i][j]
#             min_pos = (i, j)
#         if A[i][j] > max_val:
#             max_val = A[i][j]
#             max_pos = (i, j)

# A[min_pos[0]][min_pos[1]], A[max_pos[0]][max_pos[1]] = A[max_pos[0]][max_pos[1]], A[min_pos[0]][min_pos[1]]

# print("Матрица после замены наименьшего и наибольшего элементов:")
# for row in A:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# практическая 9

# 1 (блок А)

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n - 1)
    
# def power(x, n):
#     if n == 0:
#         return 1
#     else:
#         return x * power(x, n - 1)
    
# x = int(input("Введите X: "))
# n = int(input("Введите N: "))

# result = power(x, n) / factorial(n)

# print(result)

# 1 (блок Б)

# def find_max():
#     num = int(input())

#     if num == 0:  
#         return float('-inf') 
#     else:
#         max_rest = find_max() 
#         return max(num, max_rest) 

# print("Максимальное число в последовательности:", find_max())