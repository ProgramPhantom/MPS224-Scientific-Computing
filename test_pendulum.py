import numpy as np
import scipy.integrate

gamma = 1/4
omega = 1
Omega = 2/3
alpha = 1
t0 = 0
t1 = 500
t2 = 1000

def f(t, y):
    theta, eta = y
    dtheta_dt = eta
    deta_dt = -2 * gamma * eta - omega**2 * np.sin(theta) + alpha * np.cos(Omega * t)
    return [dtheta_dt, deta_dt]

T = 2 * np.pi / Omega
n_start = int(np.ceil(t1 / T))
n_end = int(np.floor(t2 / T))
t_eval = np.arange(n_start, n_end + 1) * T

sol = scipy.integrate.solve_ivp(
    f, 
    (t0, t2), 
    [0.0, 0.0], 
    t_eval=t_eval, 
    method='RK45', 
    rtol=1e-8, 
    atol=1e-8
)

theta = sol.y[0]
eta = sol.y[1]
theta_folded = (theta + np.pi) % (2 * np.pi) - np.pi

print("Theta folded standard deviation:", np.std(theta_folded))
print("Eta standard deviation:", np.std(eta))
print("Unique theta_folded values:", len(np.unique(np.round(theta_folded, 5))))
