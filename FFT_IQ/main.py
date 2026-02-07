import numpy as np
import matplotlib.pyplot as plt

fs = 1000 # Частота дискретизации
t = np.arange(0, 1, 1/fs)

# Создаем комплексный сигнал: 50 Гц вращается "вправо", 120 Гц "влево"
# (заметь минус у второй частоты)
sig = np.exp(1j * 2 * np.pi * 50 * t) + 0.5 + np.exp(1j * 2 * np.pi * -120 * t)

# Добавим немного шума
sig += 0.2 * (np.random.randn(len(t)) + 1j * np.random.randn(len(t)))

# Вычисляем БПФ
fft_res = np.fft.fft(sig)
fft_freqs = np.fft.fftfreq(len(t), 1/fs)

# Сдвигаем, чтобы 0 Гц был в центре
fft_res_shifted = np.fft.fftshift(fft_res)
fft_freqs_shifted = np.fft.fftshift(fft_freqs)

plt.figure(figsize=(10, 5))
plt.plot(fft_freqs_shifted, 20 * np.log10(np.abs(fft_res_shifted))) # В децибелах
plt.title("Спектр комплексного I/Q сигнала")
plt.xlabel("Частота (Гц)")
plt.ylabel("Амплитуда (дБ)")
plt.grid(True)
plt.show()