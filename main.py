import numpy as np
import matplotlib.pyplot as plt

def mydiff(x, t):
    c = 4  # damper constant
    k = 2  # spring constant
    m = 20 # mass
    F = 5  # force

    dx1dt = x[1]
    dx2dt = (F - c * x[1] - k * x[0]) / m

    return np.array([dx1dt, dx2dt])

# --- Runge-Kutta 4th Order Solver (RK4) ---
def rk4_solver(func, x_init, time):
    
    N = len(time)
    h = time[1] - time[0]
    n_dim = len(x_init)

    # Initialize the solution array
    x_sol = np.zeros((N, n_dim))
    x_sol[0] = np.array(x_init)

    # Main RK4 loop
    for i in range(N - 1):
        t_n = time[i]
        x_n = x_sol[i]

        # RK4 steps
        k1 = h * func(x_n, t_n)
        k2 = h * func(x_n + 0.5 * k1, t_n + 0.5 * h)
        k3 = h * func(x_n + 0.5 * k2, t_n + 0.5 * h)
        k4 = h * func(x_n + k3, t_n + h)

        # Update the state
        x_sol[i+1] = x_n + (k1 + 2*k2 + 2*k3 + k4) / 6.0

    return x_sol

# --- Initialization ---
start_time = 0.0
stop_time = 60.0
increment = 0.1
# Initial conditions: [position, velocity]
x_init = [0.0, 0.0]

time = np.arange(start_time, stop_time + increment/2, increment)

# --- Solve ODE ---
x = rk4_solver(mydiff, x_init, time)

x1 = x[:, 0] # Position
x2 = x[:, 1] # Velocity

plt.figure(figsize=(10, 6))
plt.plot(time, x1, label="Position (x1)")
plt.plot(time, x2, label="Velocity (x2)")
plt.title('Simulation of Mass-Damper-Spring (RK4)')
plt.xlabel('Time (s)')
plt.ylabel('State Variable Value')
plt.legend()
plt.grid(True)
plt.show()
