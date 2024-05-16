from sklearn.linear_model import LinearRegression
from collections import Counter

# Подготовка данных
X_train = []
y_train = []

# Пользователь вводит числа
print("Введите числа от 1 до 5:")
for i in range(10):
    while True:  # Цикл будет повторяться, пока пользователь не введет корректное число
        user_input = int(input(f"Число {i+1}: "))
        if user_input < 1 or user_input > 5:
            print("Ошибка: число должно быть от 1 до 5")
        else:
            X_train.append([user_input])
            y_train.append(user_input)  # Предполагаем, что следующее число всегда на 1 больше
            break  # Выход из цикла, если число введено корректно

# Обучение модели линейной регрессии
model = LinearRegression()
model.fit(X_train, y_train)

# Предсказание следующего числа
probabilities = Counter(y_train)
most_common_number = probabilities.most_common(1)[0][0]
next_number = most_common_number

print("Предсказанное следующее число:", next_number)
print("Вероятности выбора чисел:")
for number, count in probabilities.items():
    probability = count / len(y_train) * 100
    print(f"Число {number}: {probability:.2f}%")
