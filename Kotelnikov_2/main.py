import numpy as np
import matplotlib.pyplot as plt

# Параметры
f_signal = 10 # Частота нашего радиосигнала 10 Гц
fs_good = 100 # Хорошая частота дискретизации
fs_bad = 12 # Плохая частота дискретизации

t = np.linspace(0, 1, 1000)
sig_cont = np.sin(2 * np.pi * f_signal * t) # Аналоговый сигнал

# Дискретизация
t_good = np.arange(0, 1, 1/fs_good)
sig_good = np.sin(2 * np.pi * f_signal * t_good)

t_bad = np.arange(0, 1, 1/fs_bad)
sig_bad = np.sin(2 * np.pi * f_signal * t_bad)

plt.figure(figsize=(10, 4))
plt.plot(t, sig_cont, label='Аналоговый сигнал (10 Гц)', alpha=0.3)
plt.stem(t_good, sig_good, 'g', label='Правильная дискретизация (100 Гц)', markerfmt='go')
plt.plot(t_bad, sig_bad, 'r-o', label='Алиасинг (10 Гц)')
plt.legend()
plt.title("Эффект наложения частот")
plt.show()
