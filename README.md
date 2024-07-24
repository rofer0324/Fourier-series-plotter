# Fourier-series-plotter

Proyecto Graficador de Series de Fourier - Matemáticas Superiores Para Ingenieros - 2022

En este proyecto se puede introducir la funcion y el periodo con el que se desea trabajar.

Para un caso practico, se tiene ya definido una funcion de Onda Cuadrada.

```python
funcion = sp.Piecewise((1, (t >= 0) & (t < np.pi)), (-1, (t >= np.pi) & (t < 2 * np.pi)))
```

$$\begin{cases} 1 & \text{si } 0 \leq t \leq \pi \\ -1 & \text{si } \pi \leq t \leq 2\pi \end{cases}$$
