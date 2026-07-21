# Ввод размера массива
N = int(input("Введите количество элементов: "))
A = list(map(int, input("Введите элементы массива через пробел: ").split()))
max_index = A.index(max(A))
min_index = A.index(min(A))
left = min(max_index, min_index)
right = max(max_index, min_index)
sum_neg = 0
for i in range(left + 1, right):
    if A[i] < 0:
        sum_neg += A[i]
print("Сумма отрицательных элементов между максимальным и минимальным:", sum_neg)