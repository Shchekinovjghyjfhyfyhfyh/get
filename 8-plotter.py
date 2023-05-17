import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as tck

with open('settingsInger.txt') as file:
    settings=[float(i) for i in file.read().split('\n')]

data_v  = np.loadtxt('dataInger.txt', dtype=int) * 3.3 / 256
delta_t = settings[1]
data_t  = np.array([i*delta_t for i in range(data_v.size)])

fig, axis = plt.subplots(figsize=(10, 8), dpi=300)

axis.axis([data_v.min(), data_t.max(), data_v.min(), data_v.max()+0.2])

axis.plot(data_t, data_v, c='#34C924', linewidth=0.5, label = 'V(t)')

skip_amnt = 300
axis.scatter(
    data_t[0:data_v.size:skip_amnt],
    data_v[0:data_v.size:skip_amnt],
    marker = 'o', c = '#0A5F38', s=50
)

axis.xaxis.set_major_locator(tck.MultipleLocator(1))
axis.xaxis.set_minor_locator(tck.MultipleLocator(0.25))
axis.yaxis.set_major_locator(tck.MultipleLocator(0.5))
axis.yaxis.set_minor_locator(tck.MultipleLocator(0.1))
axis.minorticks_on()
axis.grid(which='major', color = '#'+'A1'*3)
axis.grid(which='minor', color = '#'+'A7'*3, linestyle = ':')

axis.set_title('Процесс заряжания/разряжания конденсатора', loc = 'center')
axis.set_ylabel("Напряжение, В")
axis.set_xlabel("Время, с")
axis.annotate('Время зарядки  = 6.00 с', xy=(0.2, 0.03), fontsize = 10)
axis.annotate('Время разрядки = 4.00 с', xy=(0.2, 0.1), fontsize = 10)
axis.legend(shadow = False, loc = 'upper right', fontsize = 15)

# fig.savefig('8_result.png')
