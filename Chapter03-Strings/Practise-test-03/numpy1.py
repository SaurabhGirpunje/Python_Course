import numpy as np

V = np.array([[1,3,-2],[2,2,1],[1,-1,1]])
print(V)

# X2 = V[1,:] - V[1,:].dot(V[0,:])/(V[0,:].dot(V[0,:]))*V[0,:]