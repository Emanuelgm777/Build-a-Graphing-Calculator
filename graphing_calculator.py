import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

# Función para graficar una o más funciones
def graph_functions(functions, x_range=(-10, 10)):
    x = np.linspace(x_range[0], x_range[1], 400)
    
    plt.figure(figsize=(8,6))
    
    for func in functions:
        y = func(x)
        plt.plot(x, y, label=str(func.__name__))
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph of Functions")
    plt.legend()
    plt.grid(True)
    plt.show()

# Crear una tabla de valores (x, y)
def table_of_values(function, x_range=(-10, 10)):
    x = np.linspace(x_range[0], x_range[1], 10)
    y = function(x)
    for xi, yi in zip(x, y):
        print(f"x: {xi:.2f}, y: {yi:.2f}")

# Sombrar la región debajo de la función
def shade_area(function, x_range=(-10, 10)):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = function(x)
    
    plt.figure(figsize=(8,6))
    plt.plot(x, y, label=str(function.__name__))
    plt.fill_between(x, y, color='skyblue', alpha=0.4)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Shading Under the Curve")
    plt.legend()
    plt.grid(True)
    plt.show()

# Resolver y graficar un sistema de ecuaciones
def solve_system_of_equations(eq1, eq2):
    x, y = sp.symbols('x y')
    solutions = sp.solve([eq1, eq2], (x, y))
    print(f"Solutions: {solutions}")
    
    # Graficar el sistema
    x_vals = np.linspace(-10, 10, 400)
    y_vals1 = np.array([float(sp.solve(eq1.subs(x, xi), y)[0]) for xi in x_vals])
    y_vals2 = np.array([float(sp.solve(eq2.subs(x, xi), y)[0]) for xi in x_vals])
    
    plt.figure(figsize=(8,6))
    plt.plot(x_vals, y_vals1, label=str(eq1))
    plt.plot(x_vals, y_vals2, label=str(eq2))
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Graph of the System of Equations")
    plt.legend()
    plt.grid(True)
    plt.show()

# Resolver ecuaciones cuadráticas
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    if discriminant >= 0:
        root1 = (-b + np.sqrt(discriminant)) / (2*a)
        root2 = (-b - np.sqrt(discriminant)) / (2*a)
        return root1, root2
    else:
        return "No real roots"

# Zoom en o fuera en el gráfico
def zoom_in_out(x_range=(-10, 10), y_range=(-10, 10)):
    x = np.linspace(x_range[0], x_range[1], 400)
    y = np.sin(x)
    
    plt.figure(figsize=(8,6))
    plt.plot(x, y)
    plt.xlim(x_range)
    plt.ylim(y_range)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Zoomed In/Out Graph")
    plt.grid(True)
    plt.show()

# Ejemplo de uso
if __name__ == "__main__":
    # Graficar funciones
    graph_functions([np.sin, np.cos])

    # Crear tabla de valores
    print("Table of Values for sin(x):")
    table_of_values(np.sin)

    # Sombrar área debajo de la función
    shade_area(np.sin)

    # Resolver y graficar un sistema de ecuaciones
    x, y = sp.symbols('x y')
    eq1 = sp.Eq(y, 2*x + 3)
    eq2 = sp.Eq(y, -x + 1)
    solve_system_of_equations(eq1, eq2)

    # Resolver ecuación cuadrática
    roots = solve_quadratic(1, -3, 2)
    print(f"Roots of the quadratic equation: {roots}")

    # Zoom en o fuera
    zoom_in_out(x_range=(-5, 5), y_range=(-2, 2))
