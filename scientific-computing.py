import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Define the ODE dy/dt = f(t, y)
def f(t, y):
    return -2 * t * y

# Define initial condition
y0 = 1

# Define time points to solve the ODE for
t_span = (0, 2)
t_eval = np.linspace(*t_span, 100)

# Solve the ODE
sol = solve_ivp(f, t_span, [y0], t_eval=t_eval)

# Plot the solution
plt.figure(figsize=(8, 6))
plt.plot(sol.t, sol.y[0], label='y(t)')
plt.xlabel('Time (t)')
plt.ylabel('y')
plt.title('Solution of dy/dt = -2*t*y')
plt.grid(True)
plt.legend()
plt.show()
