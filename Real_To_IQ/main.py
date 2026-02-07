import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import hilbert

# Создаем вещественный сигнал (напримет, АМ-модуляцию)
fs = 1000
t = np.linspace(0, 1, fs)
# Несущая 50 Гц, огибающая 3 Гц
carrier = np.sin(2 * np.pi * 50 * t)
envelope = 1 + 0.5 * np.sin(2 * np.pi * 3 * t)
signal = carrier * envelope

# Применяем преобразование Гильберта
analitic_signal = hilbert(signal)
amplitude_envelope = np.abs(analitic_signal) # Огибающая
isinstantaneous_phase = np.unwrap(np.angle(analitic_signal)) # Мгновенная фаза

plt.figure(figsize=(12, 6))
plt.plot(t, signal, label='Реальный сигнал (Вход)', alpha=0.4)
plt.plot(t, amplitude_envelope, 'r', label='Выделенная огибающая (Амплитуда)', linewidth=2)
plt.title("Преобразование Гильберта в действии")
plt.legend()
plt.grid(True)
plt.show()