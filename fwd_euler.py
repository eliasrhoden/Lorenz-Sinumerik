import numpy as np 
import matplotlib.pyplot as plt 

def f(x,u):
    # System equations for a single mass system
    # Extract state vector
    p = x[0] # position
    v = x[1] # speed 

    # System parameters
    M = 10
    d = 5

    acc = (u -d*v)*1/M
    dot_x = np.array([v,acc])
    return dot_x

def simulation():

    Tf = 10 
    dt = 0.1
    N = int(np.ceil(Tf/dt))
    t_vec = np.linspace(0,Tf,N+1)

    x0 = np.array([0,0])

    Us = [0]
    Xs = [x0]

    for i in range(N):
        ti = t_vec[i]

        u = 0
        if ti < 3:
            u = 1
        Us.append(u)

        dot_x = f(Xs[i],u)

        X_plus = Xs[i] + dot_x*dt 
        Xs.append(X_plus)

    Xs = np.array(Xs)
    position = Xs[:,0]
    velocity = Xs[:,1]

    plt.plot(t_vec,Us,label='Input')
    plt.plot(t_vec,position,label='Position')
    plt.plot(t_vec,velocity,label='Velocity')
    plt.legend()
    plt.xlabel('Time [s]')
    #plt.savefig('fwd_euler_sim.png',dpi=400)
    plt.show()

if __name__ == '__main__':
    simulation()

