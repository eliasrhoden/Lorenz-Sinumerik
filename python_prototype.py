import matplotlib.pyplot as plt 
from mpl_toolkits.mplot3d import Axes3D
import numpy as np 

def lorenz(X):
    x = X[0]
    y = X[1]
    z = X[2]

    sigma = 10 
    beta = 8/3
    rho = 28

    dx = sigma * (y-x)
    dy = x*(rho - z) - y 
    dz = x*y - beta*z

    return np.array([dx,dy,dz])

def ruku4(X,h):
    k_1 = lorenz(X)
    k_2 = lorenz(X + k_1*h/2)
    k_3 = lorenz(X + k_2*h/2)
    k_4 = lorenz(X + h*k_3)

    deltaX = 1/6*h*(k_1 + 2*k_2 + 2*k_3 + k_4)
    x_plus = X + deltaX 

    return x_plus

def main():

    N = 200
    X = np.array([-1,0,22])
    Xs = np.array([X])

    h = 0.02

    fig = plt.figure()

    for i in range(N):

        if i%10==0:
            print(i)

        X = ruku4(X,h)
        Xs = np.vstack((Xs,X))
    
        plt.clf()
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(Xs[:,0],Xs[:,1],Xs[:,2])
        
        ax.set_xlim(-20,20)
        ax.set_ylim(-25,25)
        ax.set_zlim(5,45)

        #plt.savefig(f'pythonScreenshots/plot_{i}.png')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()

if __name__ == '__main__':
    main()
