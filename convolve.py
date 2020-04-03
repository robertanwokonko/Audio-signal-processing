from datetime import datetime
import numpy as np

def convlove2D(x, w):
    t0 = datetime.now()
    n1, n2 = x.shape()
    m1, m2 = w.shape()
    Y = np.zeros((n1 + m1 - 1, n2 + m2 - 1))

    for i in range(n1):
        for j in range(n2):
            Y[i:i + m1, j:j+m1] += x[i,j]*w
    print "elapsed time:", (datetime.now() - t0)
    return Y

