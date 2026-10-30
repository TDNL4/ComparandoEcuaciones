import math

def f(t, y):
    """Define la función f(t, y) de la EDO dy/dt = -3y"""
    return -3 * y

def solucion_exacta(t):
    """Solución analítica exacta y(t) = 2 * e^(-3t)"""
    return 2 * math.exp(-3 * t)

def metodo_euler(t_inicial, t_final, h, y_inicial):
    """Aplica el método de Euler para aproximar la solución"""
    t_vals = [t_inicial]
    y_vals = [y_inicial]
    
    t = t_inicial
    y = y_inicial
    
    while t < t_final - 1e-9:  # Evita errores de precisión flotante
        y = y + h * f(t, y)
        t = t + h
        t_vals.append(round(t, 2))
        y_vals.append(y)
        
    return t_vals, y_vals

def main():
    t0 = 0.0
    tf = 1.0
    h = 0.2
    y0 = 2.0
    
    t_euler, y_euler = metodo_euler(t0, tf, h, y0)
    
    print(f"{'t':<6} | {'Euler (Aprox)':<15} | {'Exacta':<15} | {'Error Absoluto':<15}")
    print("-" * 57)
    
    for t, y_e in zip(t_euler, y_euler):
        y_ex = solucion_exacta(t)
        error = abs(y_ex - y_e)
        print(f"{t:<6.1f} | {y_e:<15.5f} | {y_ex:<15.5f} | {error:<15.5f}")

if __name__ == "__main__":
    main()