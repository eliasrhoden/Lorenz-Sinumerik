# Lorenz attractor in Sinumerik 

[Lorenz attractor Wikipedia](https://en.wikipedia.org/wiki/Lorenz_system)

$$
\begin{align}
\frac{dx}{dt} &= \sigma (y-x) \\
\frac{dy}{dt} &= x(\rho - z) - y \\
\frac{dz}{dt} &= xy - \beta z
\end{align}
$$


Paramz from Lorenz: $\sigma = 10$, $\beta =  8/3$ and $\rho=28$


## Runke-Kutta 4th order 

[Runge Kutta methods Wikipedia](https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta_methods)

$$
\frac{d \theta}{dt} = f(\theta,t)
$$

$$
\theta^+ = \theta + \frac{1}{6}h(k1 + 2 k_2 + 2k_3 + k_4)
$$

$$
t^+ = t + h
$$

$$
\begin{align}
k_1 &= f(\theta,t) \\
k_2 &= f(\theta + h \frac{k_1}{2},t + \frac{h}{2}) \\
k_3 &= f(\theta + h \frac{k_2}{2},t + \frac{h}{2}) \\
k_4 &= f(\theta + h k_3,t)
\end{align}
$$



