# Импортируем нужные библиотеки:
import numpy as np
from sklearn import datasets
from sklearn import linear_model
from pandas import DataFrame
import sys

# Загружаем набор данных Ирисы:
iris = datasets.load_iris()

# Получаем данные для обучения модели:
train_data = iris.data
train_labels = iris.target

# Обучаем модель логистической регрессии:
model = linear_model.LogisticRegression(max_iter=1000)
model.fit(train_data, train_labels)

# Принимаем входные данные из командной строки (например, [1, 1, 1, 1]):
input_data = np.array([float(x) for x in sys.argv[1:]]).reshape(1, -1)

# Делаем предсказание:
prediction = model.predict(input_data)

class_mapping = {
    0: "setosa",
    1: "versicolor",
    2: "virginica"
}
# Выводим предсказание в консоль:
print('Предсказание ирис: ',class_mapping[prediction[0]])
