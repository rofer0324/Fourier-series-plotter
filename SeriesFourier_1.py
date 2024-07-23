import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

def calcular_coeficientes(funcion, periodo_min, periodo_max, n_max):
    T = periodo_max - periodo_min
    w = 2 * np.pi / T
    

    # Calculo de a0
    a0 = (2 / T) * sp.integrate(funcion, (t, periodo_min, periodo_max))

    # Calculo de an
    integral_an = funcion * sp.cos(n * w * t)
    an = (2 / T) * sp.integrate(integral_an, (t, periodo_min, periodo_max))
    an = sp.simplify(an)

    # Calculo de bn
    integral_bn = funcion * sp.sin(n * w * t)
    bn = (2 / T) * sp.integrate(integral_bn, (t, periodo_min, periodo_max))
    bn = sp.simplify(bn)

    return a0, an, bn

def serie_fourier(a0, an, bn, w, k, t):
    serie = a0 / 2
    for i in range(1, k + 1):
        an_c = an.subs(n, i)
        bn_c = bn.subs(n, i)
        
        serie += an_c * sp.cos(i * w * t) + bn_c * sp.sin(i * w * t)
    return serie

def imprimir_coeficientes(a0, an, bn):
    print("Coeficiente a0:")
    sp.pretty_print(a0)
    print("\nCoeficiente an:")
    sp.pretty_print(an)
    print("\nCoeficiente bn:")
    sp.pretty_print(bn)

def graficar_series(funcion, serie, periodo_min, periodo_max, num_puntos=200):
    t_vals = np.linspace(periodo_min, periodo_max, num_puntos)
    
    fserie = sp.lambdify(t, serie, modules=['numpy'])
    f = sp.lambdify(t, funcion, modules=['numpy'])

    plt.plot(t_vals, f(t_vals), label='f(t)')
    plt.plot(t_vals, fserie(t_vals), label='Expansión en Series de Fourier')
    plt.legend()
    plt.title('Expansión en Series de Fourier')
    plt.show()

# --- Configuración --- #
t = sp.Symbol('t')
n = sp.Symbol('n')

#--- Periodos comprendido por la funcion ---#
periodo_min = 0
periodo_max = 2 * np.pi

#--- Funcion a evaluar ---#
funcion = funcion = sp.Piecewise((1, (t >= 0) & (t < np.pi)), (-1, (t >= np.pi) & (t < 2 * np.pi)))

k = 30  #Iteraciones para la aproximacion de la serie de fourier

# --- Cálculo de Coeficientes --- #
a0, an, bn = calcular_coeficientes(funcion, periodo_min, periodo_max, k)

# --- Imprimir Coeficientes --- #
imprimir_coeficientes(a0, an, bn)

# --- Cálculo de la Serie de Fourier --- #
T = periodo_max - periodo_min
w = 2 * np.pi / T
serie = serie_fourier(a0, an, bn, w, k, t)

# --- Graficar --- #
graficar_series(funcion, serie, periodo_min, periodo_max)
