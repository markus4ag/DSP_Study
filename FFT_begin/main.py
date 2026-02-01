import numpy as np
import matplotlib.pyplot as plt

# 1. Параметры
fs = 1000  # Частота дискретизации 1000 Гц
t = np.linspace(0, 1, fs, endpoint=False)

# 2. Создаем две "радиостанции" (сигналы на 50 Гц и 120 Гц)
sig1 = 1.0 * np.sin(2 * np.pi * 50 * t)
sig2 = 0.5 * np.sin(2 * np.pi * 120 * t)
noise = np.random.normal(0, 0.8, size=len(t)) # Добавим немного шума

mixed_signal = sig1 + sig2 + noise

# 3. Делаем БПФ (FFT)
fft_values = np.fft.fft(mixed_signal)
frequencies = np.fft.fftfreq(len(t), 1/fs)

# Берем только положительные частоты и считаем амплитуду (модуль комплексного числа)
mask = frequencies > 0
fft_magnitude = np.abs(fft_values)[mask]
fft_freqs = frequencies[mask]

# 4. Визуализация
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t[:200], mixed_signal[:200])
plt.title("Сигнал во временной области (Каша)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(fft_freqs, fft_magnitude)
plt.title("Спектр сигнала (Частотная область)")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда")
plt.xlim(0, 250) # Ограничим для наглядности
plt.grid(True)

plt.tight_layout()
plt.show()