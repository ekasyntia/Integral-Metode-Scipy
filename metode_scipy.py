# -*- coding: utf-8 -*-
"""Metode Scipy

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1IDvU_-sFfIjaOgGbJ6Mp8jN55WU34M0g
"""

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

#Parameter batas integral dan langkah interval
x_start = 0
x_stop = np.radians (180)
x_steps_interval = 0.01

#mwmbuat array data x dan menghitung nilai x
x_values  = np.arange(x_start, x_stop, x_steps_interval)
y_values = x_values**2 * np.cos(x_values) + 3 * np.sin(2 * x_values)

#Plot kkurva fungsi
plt.plot(x_values, y_values, label=r'${x^2cos(x) + 3sin(2x)}$', color='red')

#Isi area dibawah kurva sebagai hsil integral
plt.fill_between(x_values, y_values, color='skyblue', alpha=0.4)

#mendefinisikan fungsi lambda untuk integrasi
integration_function = lambda x: np.exp(-x ** 2)

#meghitung integral enggunakan quad () (tanpa menampilkan error)
integral, _ = integrate.quad(integration_function, x_start, x_stop)

#menampilkan hasil integarasi
print("Nilai Integral:", integral)

#Menambahkan label dan judul pada grafik
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Grafik Fungsi ${x^2cos(x) + 3sin(2x)}$ dan area di bawah kurva')
plt.legend()

#menampilkan grafik
plt.show()

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plotlib

# Define parameters.
x_start = 0 #Start of the interval
x_stop= 180 #Eend of the interval
x_steps_interval = 0.01 #step size

#Define an rray of data points.
x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = 2 * x_values * np.exp(np.sin(x_values)) + np.cos (np.exp(x_values))

#Plot the function kurve
plotlib.plot(x_values, y_values)

#Define a lambda function for integration
integration_function = lambda x: 2 * x * np.exp(np.sin(x)) + np.cos(np.exp(x))

#calculate the integral(ignoring error)
integral, _ = integrate.quad(integration_function, x_start, x_stop)

#print the integration result
print("Integral Value:")
print(integral)

#Displa the plot
plotlib.xlabel('x')
plotlib.ylabel('f(x)')
plotlib.title('Plot of f(x) = 2x * e^(sin(x)) + cos (e^x)')
plotlib.show()