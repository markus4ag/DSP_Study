import numpy as np
import matplotlib.pyplot as plt

# Параметры
fs = 1000 # частота дискретизации
f_signal = 5 # частота сигнала 5 Гц
t = np.linspace(0, 0.5, fs) # 0.5 секунды

# создаем комплексный сигнал I - это, cos Q - это sin
# exp(j * 2 * pi * f * t) = cos(...) + j * sin(...)
iq_signal = np.exp(1j * 2 * np.pi * f_signal * t)

# Рисуем
fig = plt.figure(figsize=(12, 5))

# 1. Плоскость IQ (Комплексная плоскость)
ax1 = fig.add_subplot(121)
ax1.plot(iq_signal.real, iq_signal.imag, 'g')
ax1.set_title("IQ Плоскость (Вид сверху)")
ax1.set_xlabel("I (real)")
ax1.set_ylabel("Q (Imag)")
ax1.grid(True)
ax1.axis('equal')

# Сигнал во времени
ax2 = fig.add_subplot(122)
ax2.plot(t, iq_signal.real, label='I (cos)', color='blue')
ax2.plot(t, iq_signal.imag, label='Q (sin)', color='red', linestyle='--')
ax2.set_title("I и Q компоненты во времени")
ax2.set_xlabel("Время (сек)")
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()


