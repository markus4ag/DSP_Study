import numpy as np
import matplotlib.pyplot as plt

# 1. Генерация чистого сигнала (очень тихая синусоида)
fs = 44100
t = np.linspace(0, 0.01, int(fs * 0.01))
amplitude = 0.8  # Амплитуда близка к порогу одного шага квантования
signal = amplitude * np.sin(2 * np.pi * 440 * t)

# 2. Обычное квантование (Truncation)
# Округляем до целых чисел (симулируем низкую разрядность)
quantized_simple = np.round(signal)

# 3. Квантование с Дитерингом
# Добавляем случайный шум (размером в 1 шаг квантования) ПЕРЕД округлением
dither_noise = np.random.uniform(-0.5, 0.5, len(signal))
quantized_dither = np.round(signal + dither_noise)

# Визуализация
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.step(t, quantized_simple, label='Простое квантование (ступеньки)', color='red')
plt.plot(t, signal, '--', label='Исходный сигнал', alpha=0.5)
plt.title("Ошибка квантования (сигнал превратился в прямоугольник)")
plt.legend()

plt.subplot(2, 1, 2)
plt.step(t, quantized_dither, label='Дитеринг (шумный, но точный)', color='green')
plt.plot(t, signal, '--', label='Исходный сигнал', alpha=0.5)
plt.title("Дитеринг (сохраняет форму волны за счет шума)")
plt.legend()

plt.tight_layout()
plt.show()