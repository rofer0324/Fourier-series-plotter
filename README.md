# Fourier-series-plotter

Proyecto Graficador de Series de Fourier - Matemáticas Superiores Para Ingenieros - 2022
En este proyecto se puede introducir el periodo con el que se desea trabajar y la funcion.

Para un caso practico, se tiene ya definido la una funcion de onda cuadrada.

```python
funcion = sp.Piecewise((1, (t >= 0) & (t < np.pi)), (-1, (t >= np.pi) & (t < 2 * np.pi)))
```

$$sin t < 2\pi$$ si $$0 < t < \pi$$
