import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# 1. Загружаем файл
sample_rate, data = wavfile.read("sound.wav")

# Если файл стерео (2 канала), берем только один
if len(data.shape) > 1:
    data = data[:, 0]

# 2. Берем небольшой фрагмент (например, 0,1 секунды), 
# чтобы FFT  не считался вечность
duration = 0.1
n_samples = int(sample_rate * duration)
segment = data[:n_samples]

# применяем FFT
fft_spectrum = np.fft.fft(segment)
freqs = np.fft.fftfreq(len(segment), 1/sample_rate)

# считаем аплитуду (модуть)
magnitude = np.abs(fft_spectrum)

# 4. Визуализация
plt.figure(figsize=(12, 6))

# Временная область (осциллограмма)
plt.subplot(2, 1, 1)
plt.plot(segment)
plt.title("Фрагмент аудио (Временная область)")
plt.grid(True)

# Частотная область (Спектр)
plt.subplot(2, 1, 2)
plt.plot(freqs[:n_samples//2], magnitude[:n_samples//2]) # Только положительные частоты
plt.title("Спектр аудио (Частотная область)")
plt.xlabel("Частота (Гц)")
plt.ylabel("Мощность")
plt.xlim(0, 5000) # Ограничим до 5 кГц, там обычно самое интересное
plt.grid(True)

plt.tight_layout()
plt.show()