import numpy as np
import matplotlib.pyplot as plt

# Генерируем чистый сигнал
fs = 1000
t = np.linspace(0, 0.1, fs)
signal = np.sin(2 * np.pi * 50 * t)

def quantize(data, bits):
    levels = 2**bits
    # Масштабируем сигнал в диапазон от 0 до levels-1
    quantized = np.round((data + 1) * (levels - 1) / 2)
    # Возвращаем обратно в диапазон [-1, 1] для сравнения
    return (quantized / (levels - 1) * 2) - 1

# Квантуем (например, до 3 бит — всего 8 уровней)
bits = 3
signal_q = quantize(signal, bits)
error = signal - signal_q

plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(t, signal, 'g', label='Оригинал', alpha=0.5)
plt.step(t, signal_q, 'r', label=f'Квантование ({bits} бит)')
plt.title(f"Эффект квантования: {2**bits} уровней")
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, error, 'orange', label='Ошибка (Шум)')
plt.title("Ошибка квантования (разница между оригиналом и цифрой)")
plt.legend()

plt.tight_layout()
plt.show()