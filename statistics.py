import random

data = [random.randint(1, 30) for _ in range(10)]


# Нахождение мат ожидания.
expected_value = 0

for i in range(len(data)):
    # 1/30 - так как вероятность выпадения каждого значения одинакова (один из 30)
    # но может быть дан массив M, с вероятностями для каждого числа -> data[i] * M[i].
    expected_value += data[i] * 1/30

# Нахождение дисперсии.
despersion = 0
for i in range(len(data)):
    despersion += (data[i] ** 2) * 1/30
despersion -= expected_value ** 2

