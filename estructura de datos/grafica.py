import matplotlib.pyplot as plt
import numpy as np

# Definir los rangos para x e y para graficar las curvas
x = np.linspace(0.1, 2, 400)  # Evitar división por cero cerca de x=0
y = np.linspace(0.1, 2, 400)  # Evitar división por cero cerca de y=0
X, Y = np.meshgrid(x, y)

# Definir las ecuaciones de las curvas límite
eq1 = Y - X**2
eq2 = Y - 0.5 * X**2
eq3 = X - Y**2
eq4 = X - 0.5 * Y**2

plt.figure(figsize=(8, 8))
plt.title('Región de integración R (plano xy)')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)

# Graficar las curvas límite
plt.contour(X, Y, eq1, levels=[0], colors='red', linestyles='-', label='$y = x^2$')
plt.contour(X, Y, eq2, levels=[0], colors='green', linestyles='-', label='$y = \frac{1}{2}x^2$')
plt.contour(X, Y, eq3, levels=[0], colors='blue', linestyles='-', label='$x = y^2$')
plt.contour(X, Y, eq4, levels=[0], colors='purple', linestyles='-', label='$x = \frac{1}{2}y^2$')

# Rellenar aproximadamente la región de integración (esto es una aproximación visual)
# Encontrar puntos de intersección sería más preciso para definir la región
x_fill = np.linspace(0.5, 1.5, 100)
y_upper = x_fill**2
y_lower = 0.5 * x_fill**2
plt.fill_between(x_fill, y_lower, y_upper, color='gray', alpha=0.3)

y_fill = np.linspace(0.5, 1.5, 100)
x_right = y_fill**2
x_left = 0.5 * y_fill**2
plt.fill_betweenx(y_fill, x_left, x_right, color='gray', alpha=0.3)

plt.xlim(0, 2)
plt.ylim(0, 2)
plt.legend()
plt.show()