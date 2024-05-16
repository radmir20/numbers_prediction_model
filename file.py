import numpy as np

import matplotlib.pyplot as plt 
import scipy as sp
from sklearn.linear_model import LinearRegression

from sklearn.linear_model import LinearRegression
from collections import Counter

# Подготовка данных
X_train = []
y_train = []

# Пользователь вводит числа
print("Введите числа от 1 до 5:")
for i in range(10):
    user_input = int(input(f"Число {i+1}: "))
    if user_input < 1 or user_input > 5:
        print("Ошибка: число должно быть от 1 до 5")
        continue
    X_train.append([user_input])
    y_train.append(user_input + 1)  # Предполагаем, что следующее число всегда на 1 больше

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание следующего числа
next_number = model.predict([[6]])  # Предсказываем для числа 6 (следующего после 5)
probabilities = Counter(y_train)

print("Предсказанное следующее число:", int(next_number[0]))
print("Вероятности выбора чисел:")
for number in range(1, 6):
    probability = probabilities[number] / len(y_train) * 100
    print(f"Число {number}: {probability:.2f}%")
