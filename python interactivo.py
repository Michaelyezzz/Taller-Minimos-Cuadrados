import numpy as np
import matplotlib.pyplot as plt

# Puntos iniciales
p1 = [5.4, 3.2]
p2 = [9.5, 0.7]
p3 = [12.3, -3.6]

fig, ax = plt.subplots()
plt.title("Interpolación parabólica interactiva")
plt.xlabel("x")
plt.ylabel("y")

# Dibujar p1 y p3 (no movibles)
ax.plot(p1[0], p1[1], 'ro', markersize=8, label="p1")
ax.plot(p3[0], p3[1], 'ro', markersize=8, label="p3")
# Dibujar p2 (movible)
p2_point, = ax.plot(p2[0], p2[1], 'go', markersize=12, label="p2 movible")

# Dibujar parábola inicial
x_parab = np.linspace(min(p1[0], p2[0], p3[0])-1, max(p1[0], p2[0], p3[0])+1, 200)

def parabola(x, y, xp):
    # Interpolación cuadrática: y = ax^2 + bx + c
    A = np.vstack([np.power(x,2), x, np.ones(3)]).T
    a, b, c = np.linalg.solve(A, y)
    return a*xp**2 + b*xp + c

def update_plot():
    # Actualizar punto p2
    p2_point.set_data(p2[0], p2[1])
    # Actualizar parábola
    y_parab = parabola(np.array([p1[0], p2[0], p3[0]]),
                       np.array([p1[1], p2[1], p3[1]]), x_parab)
    parab_line.set_ydata(y_parab)
    fig.canvas.draw_idle()

y_parab = parabola(np.array([p1[0], p2[0], p3[0]]),
                   np.array([p1[1], p2[1], p3[1]]), x_parab)
parab_line, = ax.plot(x_parab, y_parab, 'b-', lw=2)

dragging = False

def on_press(event):
    global dragging
    # Solo activar si se hace click cerca de p2
    if event.inaxes != ax:
        return
    contains, _ = p2_point.contains(event)
    if contains:
        dragging = True

def on_release(event):
    global dragging
    dragging = False

def on_motion(event):
    global p2, dragging
    if dragging and event.inaxes == ax and event.xdata and event.ydata:
        p2[0], p2[1] = event.xdata, event.ydata
        update_plot()

fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('button_release_event', on_release)
fig.canvas.mpl_connect('motion_notify_event', on_motion)

plt.legend()
plt.show()
