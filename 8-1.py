from matplotlib import pyplot as plt
import numpy as np

# Работа с данными
with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]

data_array = np.loadtxt("data.txt", dtype = int)
data_array = data_array / 256 * 3.3

x_array = []
for i in range(len(data_array)):
    x_array.append(i / tmp[0])

data_array = list(data_array)
x_array = list(x_array)

# Время зарядки
charge_time = 8.25

# Находим ближайшую точку к времени зарядки
idx = np.abs(np.array(x_array) - charge_time).argmin()

# Добавляем вертикальную линию
plt.axvline(x=charge_time, color='black', linestyle='--')

# Строим график с разными цветами слева и справа от вертикальной линии
plt.plot(x_array[:idx], data_array[:idx], "-", c = 'red', linewidth=2)
plt.plot(x_array[idx:], data_array[idx:], "-", c = 'blue', linewidth=2)

# Текст, заголовок, легенда
plt.text(7, 0.6, "Время зарядки: 8.25 с", fontsize=12, ha='right')
plt.text(8.5, 0.6, "Время разрядки: 4.3 с", fontsize=12, ha='left')
plt.title("График напряжения на конденсаторе")
plt.legend ()

# Сетка
plt.minorticks_on()
plt.grid(visible=True, which='major', linestyle='-', linewidth=1.5, color='0.7')
plt.grid(visible=True, which='minor', linestyle='--', linewidth=1, color='0.8')
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage[english, russian]{babel}')

# Оси, подготовка
axis_lw = 2
ax = plt.gca()
ax.set_xlim([0, 13])
ax.set_ylim([0, 3.0])
ax.set_xlabel("Время, c")
ax.set_ylabel("Напряжение, B")

# Оси, продолжение
plt.rc('axes', linewidth=axis_lw)
plt.rc('xtick.major', width=axis_lw)
plt.rc('xtick.minor', width=0)
plt.rc('xtick', direction='in')
plt.rc('axes', labelsize=20)
plt.rc('ytick.major', width=axis_lw)
plt.rc('ytick.minor', width=0)
plt.rc('ytick', direction='in')
plt.rc('xtick', labelsize=18)
plt.rc('ytick', labelsize=18)
plt.rc('xtick.major', pad=10)
plt.rc('ytick.major', pad=10)

#Сохраняем
plt.savefig("test.png")

plt.show()
