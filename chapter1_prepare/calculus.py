import numpy as np
from my_d2l import set_figsize,plot
def f(x):
    return (3*x**2 - 4*x)

x = np.arange(0,3,0.1)
plot(x, [f(x), 2*x-3],'x','f(x)',legend=['f(x)', 'tanline(x=1)'])

