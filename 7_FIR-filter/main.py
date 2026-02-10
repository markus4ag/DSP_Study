import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import firwin, lfilter, freqz

# --- 1. Подготовка сигнала ---
fs = 1000               # Частота дискретизации (1000 Гц)
T = 0.2                 # Длительность сигнала (секунды)
t = np.linspace(0, T, int(fs * T), endpoint=False)

# Полезный сигнал: 10 Гц
sig_clean = np.sin(2 * np.pi * 10 * t)

# Помеха (Шум): 150 Гц (довольно сильная, 50% от полезного)
noise = 0.5 * np.sin(2 * np.pi * 150 * t)

# Итоговый "грязный" сигнал с эфира
sig_noisy = sig_clean + noise

# --- 2. Проектирование фильтра (Digital Filter Design) ---
# Мы хотим "убить" всё, что выше 50 Гц.
cutoff_hz = 50.0       # Частота среза
numtaps = 61           # Количество коэффициентов (порядок фильтра + 1)

# Создаем коэффициенты фильтра (импульсную характеристику h)
# Используем окно Хэмминга (по умолчанию в firwin)
h = firwin(numtaps, cutoff_hz, fs=fs)

# --- 3. Применение фильтра (Свертка) ---
# Пропускаем грязный сигнал через наши коэффициенты
sig_filtered = lfilter(h, 1.0, sig_noisy)

# --- 4. Визуализация ---
plt.figure(figsize=(12, 8))

# График 1: Сигналы во времени
plt.subplot(2, 1, 1)
plt.title("Временная область: Очистка сигнала")
plt.plot(t, sig_noisy, 'r-', alpha=0.5, label='Грязный вход (10Гц + 150Гц)')
plt.plot(t, sig_filtered, 'b-', linewidth=2, label='Выход фильтра')
plt.plot(t, sig_clean, 'g--', linewidth=1, alpha=0.7, label='Идеал (без шума)')
plt.legend()
plt.grid(True)
plt.ylabel("Амплитуда")

# График 2: АЧХ фильтра (Что фильтр делает с частотами?)
# Функция freqz считает частотный отклик по коэффициентам h
w, H = freqz(h, 1, fs=fs)

plt.subplot(2, 1, 2)
plt.title(f"АЧХ Фильтра (Low-Pass, срез {cutoff_hz} Гц)")
plt.plot(w, 20 * np.log10(abs(H)), 'b') # Переводим в дБ
plt.axvline(cutoff_hz, color='r', linestyle='--', label='Частота среза')
plt.ylim(-80, 5) # Ограничим ось Y, чтобы было красиво
plt.ylabel("Амплитуда (дБ)")
plt.xlabel("Частота (Гц)")
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()