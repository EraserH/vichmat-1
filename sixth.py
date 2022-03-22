import matplotlib.pyplot as plt
import numpy as np
import math

x1 = np.linspace(-10, 10, 80)
x2 = np.linspace(-10, 2, 48)
y = [1 - math.cos(i) for i in x1]
z = [math.sqrt(3 - i) for i in x2 if i <= 2]

plt.title("Грфики зависимостей y(x):\n1) y = 1 - cos(x)\n2) y = sqrt(3 - x)") # заголовок
plt.xlabel("x") # ось абсцисс
plt.ylabel("y") # ось ординат
plt.grid()      # включение отображение сетки
plt.plot(x1, y, x2, z)  # построение графика
plt.show()


