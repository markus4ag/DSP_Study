import numpy as np
import matplotlib.pyplot as plt

# параметры нашего радиоэфира
f_signal = 5 #частота сигнала (например, 5 Гц)
fs = 100     # частота дискретизации (100 Гц - берем с запасом)
duraction = 1 # длительность в секундах

# Создаем массив времени
t = np.linspace(0 , 1, fs, endpoint=False)

# Генерирем сигнал
signal = np.sin(2 * np.pi * f_signal * t)

# Визуализация
plt.figure(figsize=(10, 4))
plt.plot(t, signal, 'o-')
plt.title(f"Сигнал {f_signal} Гц при частоте дискретизации {fs} Гц")
plt.xlabel("Время (сек)")
plt.ylabel("Амплитуда")
#plt.legend()
plt.show()
